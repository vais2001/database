from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd

import psycopg2

class CSVUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        # try:
            csv_file = request.FILES['file']

            if not csv_file.name.endswith('.csv'):
                return Response({'error': 'File must be a CSV file'}, status=status.HTTP_400_BAD_REQUEST)

            data_frame = pd.read_csv('/home/ongraph/Downloads/nba.csv')
        
            print(data_frame,111111111111111111111)

            conn = psycopg2.connect(
                        host='127.0.0.1',
                        dbname='learningbase',
                        user='ongraph1',
                        password=1999,
                        port=5432,
                     )
            cur = conn.cursor()
            
            for row in data_frame.itertuples():
                query = """
                     INSERT INTO professor (name, team, number, position, age, height, weight, college, salary)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                 """
                values = (
                        row.Name, row.Team, row.Number, row.Position,
                        row.Age, row.Height, row.Weight, row.College, row.Salary
                      )
                cur.execute(query, values)
            conn.commit()
            cur.close()
            conn.close()

            return Response({'message': 'Data inserted successfully'}, status=status.HTTP_201_CREATED)

class DatabaseDeleteView(APIView):
    def post(self, request, *args, **kwargs):
            host = request.data.get('host')
            database = request.data.get('database')
            user = request.data.get('user')
            password = request.data.get('password')
            port = request.data.get('port')

            params = {
                'host': host,
                'database': database,
                'user': user,
                'password': password,
                'port': port
            }
            
            conn = psycopg2.connect(**params)
            print(conn,22222222222222222222)
            cur=conn.cursor()
            tableName=cur.execute("""
                SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'
            """)
            print(tableName,1111111111111111111111111111111111111)
            table_names = [row[0] for row in cur.fetchall()]
            print(table_names,22222222222222222222222222222222222222)
            # return Response("done")
            if table_names:
                for table_name in table_names:
                    delete_query = f"DELETE FROM professor"
                    cur.execute(delete_query)
                print(f'All rows deleted from table {table_name}')
                print(table_name,444444444444444444444444444)    
                conn.commit()
            else:  
                cur.execute("""
                CREATE TABLE professor (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    team VARCHAR(100) NOT NULL,
                    number FLOAT NOT NULL,
                    position VARCHAR(100) NOT NULL,
                    age FLOAT NOT NULL,
                    height VARCHAR(100) NOT NULL,
                    weight FLOAT NOT NULL,
                    college VARCHAR(100),
                    salary FLOAT
                )
            """)
                conn.commit()
  
            cur.close()
            conn.close()
            return Response("created successfuly")
        
        
class CSVUploadAndCreateView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
            csv_file = request.FILES['file']

            if not csv_file.name.endswith('.csv'):
                return Response({'error': 'File must be a CSV file'}, status=status.HTTP_400_BAD_REQUEST)

            data_frame = pd.read_csv('/home/ongraph/Downloads/nba.csv')
            print(data_frame,888888888)
            conn = psycopg2.connect(
                        host='127.0.0.1',
                        dbname='learningbase',
                        user='ongraph1',
                        password=1999,
                        port=5432,
                     )
            cur = conn.cursor()
            print(conn,22222222222222222222)
            print(cur,333333333333333333333333)

            cur.execute("""
                SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'professor')
            """)
            table_exists = cur.fetchone()[0]
            print(00000000000000000000000,type(table_exists))

            if not table_exists:
                cur.execute("""
                    CREATE TABLE professor (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        team VARCHAR(100) NOT NULL,
                        number FLOAT NOT NULL,
                        position VARCHAR(100) NOT NULL,
                        age FLOAT NOT NULL,
                        height VARCHAR(100) NOT NULL,
                        weight FLOAT NOT NULL,
                        college VARCHAR(100),
                        salary FLOAT
                    )
                """)
                conn.commit()

            for row in data_frame.itertuples():
                query = """
                    INSERT INTO professor (name, team, number, position, age, height, weight, college, salary)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    row.Name, row.Team, row.Number, row.Position,
                    row.Age, row.Height, row.Weight, row.College, row.Salary
                )
                cur.execute(query, values)

            conn.commit()
            cur.close()
            conn.close()

            return Response({'message': 'Data inserted successfully'}, status=status.HTTP_201_CREATED)

       

# from django.shortcuts import render

# # Create your views here.
# from django.http import JsonResponse
# from django.db import connections
# from django.views.decorators.csrf import csrf_exempt
# import json
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# import pandas as pd
# from .serializers import ProfessorSerializerDefault
# import psycopg2




# class DatabaseConnectionView(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             host = request.data.get('host')
#             database = request.data.get('database')
#             user = request.data.get('user')
#             password = request.data.get('password')
#             port = request.data.get('port')

#             params = {
#                 'host': host,
#                 'database': database,
#                 'user': user,
#                 'password': password,
#                 'port': port
#             }
            
#             conn = psycopg2.connect(**params)
#             print(params)
#             print('DataBase connnected successfully')
#             cur = conn.cursor()
#             cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
#             table_names = [row[0] for row in cur.fetchall()]
#             print(table_names,33333333333333333333333333333333)
#             if 'professor' not in table_names:
#                 cur.execute("""
#                     CREATE TABLE professor(
#                             id SERIAL PRIMARY KEY,
#                             name VARCHAR(100) NOT NULL,
#                             team VARCHAR(100) NOT NULL,
#                             number FLOAT NOT NULL,
#                             position VARCHAR(100) NOT NULL,
#                             age FLOAT NOT NULL,
#                             height VARCHAR(100) NOT NULL,
#                             weight FLOAT NOT NULL,
#                             college VARCHAR(100),
#                             salary FLOAT
                            
#                     )
#                 """)
#                 conn.commit()
#                 # msg='table created'
#                 return Response('Table created')
#             else:
#                 msg="table already exits"    
#                 # return Response('Table already exists')
#             print(cur.fetchall(),type(cur.fetchall()),888888888888888888888)
#             cur.close()    
#             conn.close()    
#             return Response({'msg':msg,"tableName":table_names}, status=status.HTTP_200_OK)
#         except (Exception, psycopg2.DatabaseError) as error:
#             return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class ClearTableDataView(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             host = request.data.get('host')
#             database = request.data.get('database')
#             user = request.data.get('user')
#             password = request.data.get('password')
#             port = request.data.get('port')

#             params = {
#                 'host': host,
#                 'database': database,
#                 'user': user,
#                 'password': password,
#                 'port': port
#             }
            
#             conn = psycopg2.connect(**params)
#             print('Database connected successfully')
#             cur = conn.cursor()

#             # Get the list of existing table names
#             cur.execute("""
#                 SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'
#             """)
#             table_names = [row[0] for row in cur.fetchall()]

#             professor = {
#                 'professor': ['id', 'name', 'team', 'number', 'position', 'age', 'height', 'weight', 'college', 'salary'],
#                 # Add more tables and their column names as needed
#             }

#             for table_name in table_names:
#                 if table_name in professor:
#                     columns = professor[table_name]
#                     columns_str = ', '.join(columns)

#                     # Delete all rows from the table
#                     cur.execute(f"DELETE FROM {table_name}")

#                     conn.commit()
#                     print(f'All rows deleted from table {table_name}')

#             # Close the cursor and connection
#             cur.close()
#             conn.close()

#             return Response({'msg': 'Rows deleted from tables'}, status=status.HTTP_200_OK)
#         except (Exception, psycopg2.DatabaseError) as error:
#             return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# MyAPI/views.py
# import csv
# import psycopg2
# from django.http import JsonResponse
# from rest_framework.views import APIView
# from rest_framework import status

# class DatabaseManagementView(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             host = request.data.get('host')
#             database = request.data.get('database')
#             user = request.data.get('user')
#             password = request.data.get('password')
#             port = request.data.get('port')

#             params = {
#                 'host': host,
#                 'database': database,
#                 'user': user,
#                 'password': password,
#                 'port': port
#             }
            
#             conn = psycopg2.connect(**params)
#             print('Database connected successfully',conn)
#             # return Response("done")

#             # Get the list of existing table names
#             cur=conn.cursor()
#             cur.execute("""
#                 SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'
#             """)
#             table_names = [row[0] for row in cur.fetchall()]
#             print(table_names,22222222222222222222222222222222222222)#return all tables name
#             # return Response("done")
#             if table_names:
#                 for table_name in table_names:
#                     delete_query = f"DELETE FROM {table_name}"
#                     cur.execute(delete_query)
#                     print(f'All rows deleted from table {table_name}')
#                 print(table_names,444444444444444444444444444)    
#                 conn.commit()
#                 cur.close()
#                 conn.close()
#                 return Response("All rows deleted from tables", status=status.HTTP_200_OK)
#             else:  
#                 cur.execute("""
#                     CREATE TABLE professor(
#                             id SERIAL PRIMARY KEY,
#                             name VARCHAR(100) NOT NULL,
#                             team VARCHAR(100) NOT NULL,
#                             number FLOAT NOT NULL,
#                             position VARCHAR(100) NOT NULL,
#                             age FLOAT NOT NULL,
#                             height VARCHAR(100) NOT NULL,
#                             weight FLOAT NOT NULL,
#                             college VARCHAR(100),
#                             salary FLOAT
                            
#                     )
#                 """)  
#             conn.commit()
#             cur.close()
#             conn.close()
#             return Response("Table 'professor' created", status=status.HTTP_200_OK)
            # csv_file_path = '/home/vaishali/Desktop/database/nba.csv'


            # with open(csv_file_path, 'r') as csv_file:
            #     csv_reader = csv.reader(csv_file)
            #     next(csv_reader)  # Skip the header row

            #     data_to_insert = [row for row in csv_reader]
            #     for row in data_to_insert:
            #         insert_query = """
            #         INSERT INTO professor (name, team, number, position, age, height, weight, college, salary)
            #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            #         """
            #         cur.execute(insert_query, row)

            #     conn.commit()  # Commit the inserted data
            #     cur.close()
            #     conn.close()
 

        # except (Exception, psycopg2.DatabaseError) as error:
        #     return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
          

    #         if not table_names:
    #     #             # Create tables and populate with data from CSV
    #             self.create_tables_and_populate_from_csv(cur, conn)

    #         else:
    #             # Delete data from existing tables
    #             self.clear_data_from_tables(cur)

    #         cur.close()
    #         conn.close()

    #         return JsonResponse({'msg': 'Database management completed'}, status=status.HTTP_200_OK)

    #     except (Exception, psycopg2.DatabaseError) as error:
    #         return JsonResponse({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def create_tables_and_populate_from_csv(self, cur, conn):
    #     # Define table creation queries
    #     table_creation_query = """
    #         CREATE TABLE professor(
    #             id SERIAL PRIMARY KEY,
    #             name VARCHAR(100) NOT NULL,
    #             team VARCHAR(100) NOT NULL,
    #             number FLOAT NOT NULL,
    #             position VARCHAR(100) NOT NULL,
    #             age FLOAT NOT NULL,
    #             height VARCHAR(100) NOT NULL,
    #             weight FLOAT NOT NULL,
    #             college VARCHAR(100),
    #             salary FLOAT
    #         )
    #     """
    #     cur.execute(table_creation_query)
    #     conn.commit()

    #     # Read CSV and insert data into the table
    #     with open('data.csv', 'r') as csv_file:
    #         csv_reader = csv.reader(csv_file)
    #         next(csv_reader)  # Skip header
    #         for row in csv_reader:
    #             insert_query = f"INSERT INTO professor (name, team, number, position, age, height, weight, college, salary) VALUES ({','.join(['%s']*10)})"
    #             cur.execute(insert_query, row)

    #     conn.commit()
    #     print('Table created and data inserted')

    # def clear_data_from_tables(self, cur):
    #     # Delete data from tables
    #     table_names = ['professor']  # Add more table names if needed
    #     for table_name in table_names:
    #         cur.execute(f"DELETE FROM {table_name}")
    #         print(f'All rows deleted from table {table_name}')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
import psycopg2

class CSVDataInsertionView(APIView):
    def post(self, request, *args, **kwargs):
        try:
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
            cur = conn.cursor()

            csv_file_path = '/home/vaishali/Desktop/database/nba.csv'

            with open(csv_file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Skip the header row

                for row in csv_reader:
                    insert_query = """
                        INSERT INTO professor (name, team, number, position, age, height, weight, college, salary)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cur.execute(insert_query, row)

                conn.commit()  # Commit the inserted data

            cur.close()
            conn.close()

            return Response("Data inserted from CSV", status=status.HTTP_201_CREATED)

        except (Exception, psycopg2.DatabaseError) as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

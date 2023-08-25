from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.db import connections
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
from .serializers import ProfessorSerializerDefault
import psycopg2


# class RawSQLView(APIView):
#     def get(self, request, *args, **kwargs):
#         # Get the connection to the "learningbase" database
#         connection_learningbase = connections['default']

#         # Open a cursor
#         with connection_learningbase.cursor() as cursor:
#             # Execute the raw SQL query
#             cursor.execute("SELECT * FROM professor;")
#             results = cursor.fetchall()

#         return Response(results)
# class RawSQLView(APIView):
#     def get(self, request, *args, **kwargs):
#         # Get the connection to the "learningbase" database
#         connection_learningbase = connections['postgres']

#         # Open a cursor
#         with connection_learningbase.cursor() as cursor:
#             # Execute the raw SQL query
#             cursor.execute("SELECT * FROM student;")
#             results = cursor.fetchall()

#         return Response(results)




# class CSVUploadView(APIView):
#     # parser_classes = (FileUploadParser,)

#     def post(self, request, *args, **kwargs):
#         data=request.data
#         print(data)
#         host=data.get('HOST')
#         print(host)
#         # print(request.get('HOST'))
#         # print(request.get('PORT'))
#         return Response({"msg":"done"})
        # pass
        # csv_file = request.FILES['file']
        # print(csv_file)

        # if not csv_file.name.endswith('.csv'):
        #     print(11111111111111111111111111111)
        #     return Response({'error': 'File must be a CSV file'}, status=status.HTTP_400_BAD_REQUEST)

        # data_frame = pd.read_csv(csv_file,delimiter=';')
        # serializer = ProfessorSerializerDefault(data=data_frame.to_dict(orient='records'), many=True)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import psycopg2

class DatabaseConnectionView(APIView):
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
            print('DataBase connnected successfully')
            cur = conn.cursor()
            print(cur,1111111111111111111111111111111111111111111)

            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            print(db_version,222222222222222222222222222222222222222222222)

            # cur.close()
            # cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
            # for table in :
            #   print(table)
            
            # print(cur.fetchall(),type(cur.fetchall()))
            
            # tablename=cur.fetchall()
            # print(tablename)
            # conn.close()

            return Response({'db_version': db_version[0],"tableName":tablename}, status=status.HTTP_200_OK)
        except (Exception, psycopg2.DatabaseError) as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

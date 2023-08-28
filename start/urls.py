from django.urls import path
from .views import*
urlpatterns = [

#      path('upload-csv', DatabaseConnectionView.as_view(), name='csv-upload'),
#      path('items',ClearTableDataView.as_view(), name='create_item'),
#       path('items1',CSVUploadView.as_view(), name='create_item')
    #   path('items',DatabaseManagementView.as_view(), name='create_item')
      path('insert-csv-data', CSVDataInsertionView.as_view(), name='insert-csv-data')
]

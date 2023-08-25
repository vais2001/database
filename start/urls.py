from django.urls import path
from .views import*
urlpatterns = [

    #  path('items',RawSQLView.as_view(), name='create_item')
     path('upload-csv', DatabaseConnectionView.as_view(), name='csv-upload')
]
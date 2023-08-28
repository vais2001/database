from django.urls import path
from .views import*
urlpatterns = [
      path('items',DatabaseDeleteView.as_view(), name='create_item'),
      path('items1',CSVUploadView.as_view(), name='create_item'),
      path('items2',CSVUploadAndCreateView.as_view(), name='create_item')
]


from rest_framework import serializers
from .models import ProfessorStudent




class ProfessorSerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = ProfessorStudent
        fields = '__all__'

class StudentSerializerLearningBase(serializers.ModelSerializer):
    class Meta:
        model = ProfessorStudent
        fields = '__all__'

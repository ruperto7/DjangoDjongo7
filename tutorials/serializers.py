from rest_framework import serializers
from tutorials.models import Tutorial
from tutorials.models import Notes27Jan
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

class Notes27JanSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Notes27Jan
        fields = ('id',
                  'title',
                  'desc',
                  'date')

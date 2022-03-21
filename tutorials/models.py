from django.db import models
#from .models  import RawRequest
import uuid
from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model

class ExtendedEncoder(DjangoJSONEncoder):

    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)
        return super().default(o)

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    t_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)
    
class Notes27Jan(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    desc = models.CharField(max_length=200, blank=False, default='')
    comment = models.CharField(max_length=200, blank=False, default='')
    comment1 = models.CharField(max_length=200, blank=False, default='')
    comment2 = models.CharField(max_length=200, blank=False, default='')
    comment3 = models.CharField(max_length=200, blank=False, default='')
    comment4 = models.CharField(max_length=200, blank=False, default='')  
    keywords = models.CharField(max_length=200, blank=False, default='')
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True) #models.IntegerField((max_length=200, blank=False, default=''))
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.id + ' ' + (self.title if (self.title) else "") + ': ' + (self.desc if (self.desc) else "")

class Todo(models.Model):
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True) #models.IntegerField((max_length=200, blank=False, default=''))
    date = models.DateTimeField(auto_now=True)    
    What = models.CharField(max_length=70, blank=False, default='')
    Why = models.CharField(max_length=70, blank=False, default='')
    When = models.CharField(max_length=70, blank=False, default='')
    Who = models.CharField(max_length=70, blank=False, default='')
    Where = models.CharField(max_length=70, blank=False, default='')
    keywords = models.CharField(max_length=200, blank=False, default='')

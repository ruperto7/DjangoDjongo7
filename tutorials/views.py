from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
import logging, logging.config #LOGGER
from pprint import pprint
#from rest_framework import serializers #totoa gritty fool
import django
#from django.core import serializers
##from django.db  import connections
from django.shortcuts import render #TO SEE A WEB PAGE
from tutorials.models import Notes27Jan
#from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from rest_framework.response import Response
#from django.template.context_processors import csrf
#from django.contrib.sitemaps.views import sitemap
from tutorials.forms import ContactForm
from django.views.generic.edit import FormView
#from tutorials.serializers import Notes27JanSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST','GET'])
def misc(request):
    v,k=allNotes()
    return render(request, './misc.html', {"about_message":main_content(), "allNotesV" : v, "allNotesK" : k}) 

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

def index(request):
    return render(request, './index.html', { }) 

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all() # .objects.all()
        pprint(tutorials)
        pprint(django.db.connections)
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

@api_view(['POST','GET'])
def root(request):
    return render(request, './root.html', {"about_message":main_content() })     
    
@api_view(['GET'])
def base(request):
    return render(request, './base.html', { }) 
 
#    logging.info('views.py function home(request )') # 
#    return JsonResponse({'message': 'wazzup?!'} )
@api_view(['POST','GET'])
def home(request):
    return render(request, './home.html', {"about_message":main_content() }) 
    #return render(request, './home.html', { }) 

def main_content():
    return "Notes27Jan and Todo Notes 2021"
@csrf_exempt
@api_view(['POST','GET'])
@login_required(login_url='/accounts/login/') #views.login_request
def misc2(request):
    logging.info('Hello from views.misc2, BASE_DIR is'+globals()['__name__'] ) #+csrf.get_token(request)
    v,k=allNotes()
    return render(request, './misc2.html', {"about_message":main_content(), "allNotesV" : v, "allNotesK" : k})   

def allNotes():
    #return Notes27Jan.objects.all(),   Notes27Jan.objects.all()
    return Notes27Jan.objects.all().order_by('-date'),  Notes27Jan.objects.all().order_by('-date')

@api_view(['POST','GET'])
def login_request(request):
    logging.info('Hello from views login_request') #+csrf.get_token(request)
    if request.method == 'POST':#name = form.cleaned_data['name']

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')       
        msg='POST DETECTED Hello from views login_request from username'+username+' password: '+password
        logging.info(msg) #+csrf.get_token(request)
    return render(request, './registration/login.html', { 'ContactForm':ContactForm}) 
 
 
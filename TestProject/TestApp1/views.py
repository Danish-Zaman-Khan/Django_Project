from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testapp(request):
    return HttpResponse("This is the Test project")
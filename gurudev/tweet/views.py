from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tweetindex(request):
    return render(request , 'tweet/index.html')
    
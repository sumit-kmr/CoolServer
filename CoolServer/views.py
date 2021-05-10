from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import RequestContext
import json
import os
def page(key):
    f=open(os.path.join(os.path.dirname(os.path.dirname(__file__)),"CoolServer/Backend_Script/"+key+".json"))
    #cont = {}
    #cont['articles'] =
    content = json.load(f)
    #print(cont) 
    return content

def index(request):
    return HttpResponse("<h1>Hello World</h1>")

def edu(request):
    return JsonResponse({'article':page('Edu')})
def ent(request):
    return JsonResponse({'article':page('Ent')})

def india(request):
    return JsonResponse({'article':page('India')})

def life(request):
    return JsonResponse({'article':page('Life')})

def trending(request):
    return JsonResponse({'article':page('Trending')})

def business(request):
    return JsonResponse({'article':page('Business')})

def auto(request):
    return JsonResponse({'article':page('Auto')})

def tech(request):
    return JsonResponse({'article':page('Tech')})

def sport(request):
    return JsonResponse({'article':page('Sport')})

def world(request):
    return JsonResponse({'article':page('World')})


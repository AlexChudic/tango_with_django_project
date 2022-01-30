from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	html= '<p>Rango says hey there partner!</p><a href="/rango/about/">About</a>'
	return HttpResponse(html)

def about(index):
	html= '<p>Rango says here is the about page.</p><a href="/rango/">Home</a>'
	return HttpResponse(html)
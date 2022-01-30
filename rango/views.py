from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context=context_dict)

def about(index):
	html= '<p>Rango says here is the about page.</p><a href="/rango/">Home</a>'
	return HttpResponse(html)
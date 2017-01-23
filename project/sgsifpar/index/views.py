from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader

# INDEX
def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

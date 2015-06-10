from django.shortcuts import render
from django.http import HttpResponse
import pymongo

# Create your views here.
def doc(request, doc_id):
	return HttpResponse('get doc %s OK' % doc_id)

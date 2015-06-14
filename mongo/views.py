from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient 
import json
import dict

# Create your views here.
def doc(request, col_id, doc_id):
    client = MongoClient('localhost', 27017)
    db = client['kkoma']
    col = db[col_id]

    if request.method == "GET":
        doc = col.find_one({"_id": doc_id})
        return HttpResponse(doc)
    elif request.method == "POST":
        doc = json.loads(request.POST['data'])
        col.insert(doc)
        result = dict()
        result['result'] = 0
        result['message'] = 'insert ' + doc_id + ' success'
        return HttpResponse(json.dumps(result), content_type='application/json')
    else :
        return HttpResponse('not support method')

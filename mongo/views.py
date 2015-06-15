from django.shortcuts import render
from django.http import HttpResponse
import logging
from pymongo import MongoClient 
import json

# Create your views here.
logger = logging.getLogger(__name__)

def doc(request, col_id, doc_id):
    client = MongoClient('localhost', 27017)
    db = client['kkoma']
    col = db[col_id]

    if request.method == "GET":
        logger.debug("get doc %s:%s" % (col_id, doc_id))
        doc = col.find_one({"_id": doc_id})
        return HttpResponse(doc)
    elif request.method == "POST":
        logger.debug("post doc %s:%s" % (col_id, doc_id))
        doc = json.loads(request.POST['data'])
        col.insert(doc)
        result = dict()
        result['result'] = 0
        result['message'] = 'insert ' + doc_id + ' success'
        return HttpResponse(json.dumps(result), content_type='application/json')
    else :
        logger.warn("not support method %s" % (request.method))
        return HttpResponse('not support method')

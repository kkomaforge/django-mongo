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

    if request.method == 'GET':
        logger.debug('get doc [%s] %s' % (col_id, doc_id))
        doc = col.find_one({"_id": doc_id})
        logger.debug('<- ' + json.dumps(doc))
        result = {}
        result['result'] = 0
        result['message'] = 'get %s success' % (doc_id)
        result['doc'] = doc
        return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')
    elif request.method == 'POST':
        logger.debug('insert doc [%s] %s' % (col_id, doc_id))
        doc = json.loads(request.body)
        doc['_id'] = doc_id
        logger.debug('-> ' + json.dumps(doc))
        col.insert(doc)
        result = {}
        result['result'] = 0
        result['message'] = 'insert %s success' % (doc_id)
        return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')
    elif request.method == 'PUT':
        logger.debug('update doc [%s] %s' % (col_id, doc_id))
        doc = json.loads(request.body)
        logger.debug('-> ' + json.dumps(doc))
        set = {}
        set['$set'] = doc
        col.update({'_id':doc_id}, set, upsert=False)
        result = {}
        result['result'] = 0
        result['message'] = 'update %s success' % (doc_id)
        return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')
    elif request.method == 'DELETE':
        logger.debug('delete doc [%s] %s' % (col_id, doc_id))
        col.remove({"_id":doc_id})
        result = {}
        result['result'] = 0
        result['message'] = 'delete %s success' % (doc_id)
        return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')
    else :
        logger.warn('not support method %s' % (request.method))
        return HttpResponse('not support method')


def query(request, col_id):
    logger.debug('query [%s]' % (col_id))
    q = request.GET.get('q')
    client = MongoClient('localhost', 27017)
    db = client['kkoma']
    col = db[col_id]
    result = {}
    result['result'] = 0
    result['message'] = 'query %s success' % (q)
    result['docs'] = []
    count = 0
    for doc in col.find():
        logger.debug('-> ' + doc)
        result['docs'].append(doc)
        count += 1
    result['count'] = count
    return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')
    
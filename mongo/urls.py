from django.conf.urls import include, url

urlpatterns = [
    url(r'^(?P<col_id>\w+)/(?P<doc_id>\w+)', 'mongo.views.doc'),
]

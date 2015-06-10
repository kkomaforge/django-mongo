from django.conf.urls import include, url

urlpatterns = [
    url(r'^doc/(?P<doc_id>\w+)', 'mongo.views.doc'),
]

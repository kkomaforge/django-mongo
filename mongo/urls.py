from django.conf.urls import include, url

urlpatterns = [
    url(r'^get/', 'mongo.views.get_doc'),
]

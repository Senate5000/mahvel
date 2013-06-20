from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
(r'test', 'combodb.views.test_view')
)
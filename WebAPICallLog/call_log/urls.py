from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from call_log import views

urlpatterns = [
    url(r'^calls/$', views.CallList.as_view()),
    url(r'^calls/(?P<number>[\w\-]+)/$', views.CallBill.as_view()),   
    url(r'^calls/(?P<number>[\w\-]+)/(?P<date>\d{4}-\d{2}-\d{2})/$', views.CallBill.as_view()),
]

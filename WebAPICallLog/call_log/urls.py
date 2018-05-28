from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from call_log import views

urlpatterns = [
    url(r'^calls/$', views.CallList.as_view()),
]

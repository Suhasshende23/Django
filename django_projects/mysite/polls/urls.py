from django.urls import path
from .views import *
app_name="poll"
urlpatterns=[
path('first/',index,name="index"),
path('<int:question_id>/',detail,name="details"),

path('<int:question_id>/results',results,name="results"),
path('<int:question_id>/vote',vote,name="vote")
]

# question_id instead of pk in the url pattern
# 

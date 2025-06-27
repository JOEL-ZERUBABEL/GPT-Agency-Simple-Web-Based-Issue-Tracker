from django.urls import path
from .views import *

urlpatterns=[
    path('issue/list/',issue_list,name='issue_list'),
    path('issue/create/',issue_create,name='issue_create'),
    path('issue/update/<int:id>/',issue_update,name='update_issue'),
]
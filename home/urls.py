from django.urls import path
from home import views
urlpatterns=[
path('',views.home,name='home'),
path('worker/<slug:slug>',views.workers_detail,name='workers_detail')
]
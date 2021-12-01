from django.urls import path 
from . import views
urlpatterns=[
    path('sample',views.fnsample,name='sample'),
    path('abhi',views.fn1,name='abhi'),
    path('login',views.fn2,name='login')
]
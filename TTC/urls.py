from django.urls import path
from . import views
#Adding
urlpatterns=[
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('form_Employee',views.form_Employee,name="form"),
    path('EmployeePage',views.employee,name="employee"),
    path('EmployerPage',views.employer,name="employer")
]
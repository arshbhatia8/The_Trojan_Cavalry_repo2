from django.urls import path
from . import views
#Adding
urlpatterns=[
    path('',views.index,name="index"),
    path('midway',views.midway,name="midway"),
    path('sampleSearch',views.searchRequest,name="Search"),
    path('sampleSearch_Employer',views.searchRequest_Employer,name="SearchEmployer"),
    path('home',views.home,name="home"),
    path('form_Employee',views.form_Employee,name="formE"),
    path('form_Employer',views.form_Employer,name="formEmployer"),
    path('EmployeePage',views.employee,name="employee"),
    path('EmployerPage',views.employer,name="employer")
]
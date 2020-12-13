from django.shortcuts import render
from TTC.models import Employee, Employer
from TTC.form_Employee import NewUser
from django.db import models
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request,'base.html')
def home(request):
    e=Employee.objects.order_by('Employee_Name')
    dict1={'employee':e}
    return render(request,'home.html',context=dict1)

def employee(request):
    return render(request,'employee.html')

def employer(request):
    return render(request,'employee.html')

def form_Employee(request):

    form = NewUser()

    if request.method == "POST":
        form=NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM INVALID')

    return render(request, 'form_Employee.html',{'form':form})

def searchRequest(request):
    if request.method == 'POST':
        Entered_Request=request.POST.get('JobReqdfield',None)
        # for employees in Employee:
        #     if employee.Emp_ID == Entered_ID:
        #         return HttpResponse('employee.Employee_Name')
        try:
            user=Employee.objects.filter(Emp_Job_Requirement=Entered_Request)
            dict_2 = {'items':user}
            return render(request, 'sampleSearch.html', context=dict_2)
        except Employee.DoesNotExist:
            return HttpResponse("No object")
    else:
        return render(request, 'sampleSearch.html')

def form_Employer(request):

    form = NewEmployer()

    if request.method == "POST":
        form=NewEmployer(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM INVALID')
#'Form' is the dictionary of the Employer elements
    return render(request, 'form_Employer.html',{'form':form})



def searchRequest_Employer(request):
    if request.method == 'POST':
        Entered_Request=request.POST.get('BizModelField',None)
        # for employees in Employee:
        #     if employee.Emp_ID == Entered_ID:
        #         return HttpResponse('employee.Employee_Name')
        try:
            user=Employer.objects.filter(BizModel=Entered_Request)
            dict_2 = {'items':user}
            return render(request, 'sampleSearch.html', context=dict_2)
        except Employer.DoesNotExist:
            return HttpResponse("No object")
    else:
        return render(request, 'sampleSearch_Employer.html')

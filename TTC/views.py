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
        Entered_ID=request.POST.get('IDfield',None)
        # for employees in Employee:
        #     if employee.Emp_ID == Entered_ID:
        #         return HttpResponse('employee.Employee_Name')
        try:
            user=Employee.objects.get(Emp_ID=Entered_ID)
            html=("<h1> HELLO1 <h1>", user)
            return HttpResponse(html)
        except Employee.DoesNotExist:
            return HttpResponse("No object")
    else:
        return render(request, 'sampleSearch.html')
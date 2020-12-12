from django.shortcuts import render
from TTC.models import Employee, Employer
from TTC.form_Employee import NewUser
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

def query_result_form(request):
    
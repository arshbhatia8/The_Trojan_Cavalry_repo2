from TTC.models import Employee, Employer
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','The_Trojan_Cavalry.settings')

import django
django.setup()


if __name__ == '__main__':
    
Employee1 = Employee.objects.get_or_create(Employee_Name=fakegen.name(),Employee_PhNo=fakegen.name())

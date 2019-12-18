import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Employee.settings')

import django
django.setup()

from empapp.models import EmployeeModel
from faker import Faker
from random import *

fake=Faker()

def populate(n):
    for i in range(n):
        feno=randint(101,9999)
        fename=fake.name()
        fesal=randint(30000,100000)
        feaddr=fake.city()
        e_rcd=EmployeeModel.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
populate(20)        

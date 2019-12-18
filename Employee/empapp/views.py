from django.shortcuts import render,redirect
from empapp.forms import EmployeeForm
from empapp.models import EmployeeModel


# Create your views here.
def retrive_view(request):
    emp_data=EmployeeModel.objects.all()
    return render(request, 'html/home.html',{'emp_data':emp_data})

def insert_view(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')

    return render(request,"html/insert.html", {'form':form})

def delete_view(request,id):
    emp=EmployeeModel.objects.get(id=id)
    emp.delete()
    return redirect('/')

def update_view(request,id):
    emp=EmployeeModel.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'html/update.html',{'emp':emp})

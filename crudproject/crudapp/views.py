from django.shortcuts import render, redirect
from crudapp.forms import EmployeeForm
from .models import Employee

# Create your views here.

#CREATE
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})


#READ
def show(request):
    employees=Employee.objects.all()
    return render(request, "show.html", {'employees':employees})

#DELETE, EDIT/UPDATE
def destroy(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')

#UPDATE--> EDIT -> UPDATE

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'employee':employee})




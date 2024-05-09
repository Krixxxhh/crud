from django.shortcuts import render,redirect
from .models import Department,Employee
from.forms import DepartmentForm,EmployeeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']

        if (cp == p):
            user = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            user.save()
            return redirect('employee:home')
        else:
            return HttpResponse("passwords are not the same")
    return render(request, 'register.html')



def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('employee:home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')


def department_list(request):
    d=Department.objects.all()
    return render(request,'department.html',{'d':d})

def create_dep(request):
    if(request.method=="POST"):
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return department_list(request)
    form=DepartmentForm()
    return render(request,'create_dep.html',{'form':form})

def dep_detail(request,n):
    d=Department.objects.get(id=n)
    return render (request,'dep_detail.html',{'d':d})




def create_emp(request):
    if(request.method=="POST"):
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return employee_list(request)
    form=EmployeeForm()
    return render(request,'create_emp.html',{'form':form})

# def create_emp(request):
#     if request.method == "POST":
#         n = request.POST['n']
#         dep_name = request.POST.get('department')  # Assuming you collect department name from form
#         department = Department.objects.get(dep_name=dep_name)
#         e = request.POST['e']
#         p = request.POST['p']
#         a = request.POST['a']
#         b = request.POST['b']
#         em = Employee.objects.create(
#             name=n, department=department,email=e,contact_number=p,address=a,date_of_birth=b)
#         em.save()
#         return employee_list(request)
#     return render(request, 'create_emp.html')



def employee_list(request):
    e=Employee.objects.all()
    return render(request,'employee.html',{'e':e})

def get_emp(request,n):
    e=Employee.objects.get(id=n)
    return render(request,'get_emp.html',{'e':e})


def edit_emp(request,n):
    b=Employee.objects.get(id=n)
    if (request.method == "POST"):
        form=EmployeeForm(request.POST,instance=b)
        if form.is_valid():
            form.save()
            return employee_list(request)
    form=EmployeeForm(instance=b)
    return render(request,'edit_emp.html',{'form':form})

def delete(request,n):
    b=Employee.objects.get(id=n)
    b.delete()
    return employee_list(request)


def user_logout(request):
    logout(request)
    return user_login(request)




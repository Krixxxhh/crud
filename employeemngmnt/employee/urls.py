"""
URL configuration for employeemngmnt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee import views
app_name = 'employee'
urlpatterns = [
    path('',views.home,name="home"),
    path('department/', views.department_list, name="department"),
    path('login', views.user_login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.user_logout, name="logout"),

    path('employee_list/', views.employee_list, name="employee_list"),
    path('create_emp/', views.create_emp, name="create_emp"),
    path('get_emp/<int:n>', views.get_emp, name="get_emp"),
    path('edit/<int:n>', views.edit_emp, name="edit"),
    path('delete/<int:n>', views.delete, name="delete"),

]

from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('<str:value>/employeeview/', views.employeeview, name="employeeview"),
    path('<int:company_id>/', views.display, name="display"),
    path('<int:id>/employeename/', views.employeename, name="employeename"),
    path('<int:id>/id_number/', views.get_employee_id_number, name="id_number"),
    path('<int:company_id>/ename/', views.get_company_employees, name="ename"),
    path('<int:company_id>/employeeid/', views.get_employees_ids, name="employeeid"),
    path('<int:company_id>/name/', views.get_company_name , name="name")

]
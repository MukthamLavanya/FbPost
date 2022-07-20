from django.shortcuts import render

from django.http import HttpResponse

from .models import Companies, Employee


def display(request, company_id):
    return HttpResponse("Employee Id is {}".format(company_id))


def index(request):
    latest_company_list = Companies.objects.order_by('-company_started')[:5]
    output = ', '.join([q.name for q in latest_company_list])
    return HttpResponse(output)


def employeeview(request, value):
    latest_employee_list = Employee.objects.all()
    output = ', '.join([q.name for q in latest_employee_list])
    return HttpResponse(output)

def employeename(request, id):
    employee_obj = Employee.objects.get(id=id)
    name = employee_obj.name
    return HttpResponse(name)


def get_employee_id_number(request, id):
    get_id_number = Employee.objects.get(id = id)
    number = get_id_number.id_number
    return HttpResponse(number)


def get_company_employees(request, company_id):
    employees = Employee.objects.filter(company_id=company_id)
    """
    [Employee obj1, employee obj2...]
    """
    employees_names = []
    for i in employees:
        employees_names.append(i.name)

    return HttpResponse(employees_names)


"""
Q1: 

1. Request: company_id 
2. Response: company_id respective employees ids.
"""


def get_employees_ids(request, company_id):
    get_employee_obj = Employee.objects.filter(company_id = company_id)

    employee_id = []
    for i in get_employee_obj:
        employee_id.append(i.id_number)
    return HttpResponse(employee_id)


"""
Q2:

1. Request: company_id
2. Response: company_name
"""

def get_company_name(request, company_id):
    get_company_obj = Companies.objects.get(id = company_id)

    company_name = get_company_obj.name
    return HttpResponse(company_name)

from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
# def hello(request):
#     my_list = [1,2,3,4 "String"]
#     return HttpResponse(my_list)

# def hello(request):
#     body = """ 
#     <h1>Привет</h1>
#     <p>Параграф</p>
#     """
#     return HttpResponse(body)
# # передача словаря, приходит только ключ

# def hello(request):
#     my_dict = {"name": "Alex"}
#     return HttpResponse(my_dict)

# передача заголовков и статуса ответа
def hello(request):
    headers = {"name": "Chyngyz"}
    return HttpResponse("GeekTech", status=200, headers=headers)

def time(request):
    dt_now = datetime.datetime.now()
    return HttpResponse(dt_now)

def goodbye(request):
    return HttpResponse("Goodbye")
import hashlib, json, datetime, os, MySQLdb, random, requests
from . import models
from django.db.models import Count, Q,Sum
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder # This is use for encode json with date field, ex student date of birth
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils.dateparse import parse_date, parse_datetime

def student_list(request):
    if models.Student.objects.filter(status = True):
        student_list      = models.Student.objects.values().order_by("-id")
        data = {
            'status': True,
            'msg': "Student successfully loaded.",
            'student_list' : list(student_list),
        }
    else:    
        data = {
            'status': False,
            'msg': "Unauthorized User"
        }
    return JsonResponse(data,  safe=False, content_type='application/json; charset=utf8') 


from django.shortcuts import render
from django.http import JsonResponse


def disease_detection_view(request):
    return JsonResponse({"message": "This is the plant disease detection API!"})
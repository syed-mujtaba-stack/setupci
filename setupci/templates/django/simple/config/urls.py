from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to your simple Django app!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

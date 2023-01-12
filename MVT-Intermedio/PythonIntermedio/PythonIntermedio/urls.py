from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name = 'index view'),
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls'), name = 'including AppCoder urls.py'),
]

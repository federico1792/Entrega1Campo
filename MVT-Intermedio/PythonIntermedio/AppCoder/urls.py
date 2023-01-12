from django.urls import path
from AppCoder.views import create_group, list_group, create_student, list_student, create_professor, list_professor

urlpatterns = [
    path('create_group/', create_group),
    path('list_group/', list_group),
    path('create_student/', create_student),
    path('list_student/', list_student),
    path('create_professor/', create_professor),
    path('list_professor/', list_professor),
]

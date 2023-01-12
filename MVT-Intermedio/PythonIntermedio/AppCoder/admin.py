from django.contrib import admin
from AppCoder.models import Group, Student, Professor
# Register your models here.

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'group',)
    list_filter = ('group',)
    search_fields = ('name', 'group',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email',)
    list_filter = ('name',)
    search_fields = ('name', 'lastname', 'email',)    

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'profession',)
    list_filter = ('name', 'profession',)
    search_fields = ('name', 'lastname', 'email', 'profession',)   
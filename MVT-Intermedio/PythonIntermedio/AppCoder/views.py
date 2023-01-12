from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Group, Student, Professor
from AppCoder.forms import GroupForm, StudentForm, ProfessorForm

def create_group(request):
    if request.method == 'GET':
        context = {
            'form': GroupForm()
        }
        return render(request, 'AppCoder/create_group.html', context=context)
    elif request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            Group.objects.create(
                name = form.cleaned_data['name'],
                group = form.cleaned_data['group'],
            )
            context = {
                'message': 'Producto creado exitosamente',
            }
            return render(request, 'AppCoder/create_group.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': GroupForm()
            }
            return render(request, 'AppCoder/create_group.html', context=context)
def list_group(request):
    if 'search' in request.GET:
        search = request.GET['search']
        group = Group.objects.filter(group__contains = search).order_by('group')
    else:
        group = Group.objects.all()

    context = {
        'group': group,
    }
    return render(request, 'AppCoder/list_group.html', context = context)

def create_student(request):
    if request.method == 'GET':
        context = {
            'form': StudentForm()
        }
        return render(request, 'AppCoder/create_student.html', context=context)
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(
                name = form.cleaned_data['name'],
                lastname = form.cleaned_data['lastname'],
                email = form.cleaned_data['email'],
            )
            context = {
                'message': 'El estudiante fue creado exitosamente',
            }
            return render(request, 'AppCoder/create_student.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': StudentForm()
            }
            return render(request, 'AppCoder/create_student.html', context=context)
def list_student(request):
    if 'search' in request.GET:
        search = request.GET['search']
        student = Student.objects.filter(name__contains = search).order_by('name')
    else:
        student = Student.objects.all()

    context = {
        'student': student,
    }
    return render(request, 'AppCoder/list_student.html', context = context)

def create_professor(request):
    if request.method == 'GET':
        context = {
            'form': ProfessorForm()
        }
        return render(request, 'AppCoder/create_professor.html', context=context)
    elif request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            Professor.objects.create(
                name = form.cleaned_data['name'],
                lastname = form.cleaned_data['lastname'],
                email = form.cleaned_data['email'],
                profession = form.cleaned_data['profession'],
            )
            context = {
                'message': 'Profesor creado exitosamente',
            }
            return render(request, 'AppCoder/create_professor.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProfessorForm()
            }
            return render(request, 'AppCoder/create_professor.html', context=context)

def list_professor(request):
    if 'search' in request.GET:
        search = request.GET['search']
        professor = Professor.objects.filter(profession__contains = search).order_by('profession')
    else:
        professor = Professor.objects.all()

    context = {
        'professor': professor,
    }
    return render(request, 'AppCoder/list_professor.html', context = context)

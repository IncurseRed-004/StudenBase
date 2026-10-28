from django.shortcuts import render

from Studen_app.forms import studentForm
from Studen_app.models import Students


# registration

def register_students(request):
    if request.method =='POST':
        form = studentForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = studentForm()

    return render(request,'students/register.html',{'form':form})

#student list
def student_list(request):
    students = Students.objects.all()
    return render(request,'students/student_list.html',{'students':students})

# edit students


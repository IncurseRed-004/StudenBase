from django.shortcuts import render, get_object_or_404, redirect

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
def edit_student(request,id):
    student = get_object_or_404(Students, id=id)

    if request.method =="POST":
        form = studentForm(request.POST,instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = studentForm(instance=student)
    return render(request,'students/edit_student.html',{'form':form})

#delete student
def delete_student(request,id):
    student = get_object_or_404(Students, id =id)
    student.delete()
    return redirect('student_list')
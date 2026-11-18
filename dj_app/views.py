
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .forms import StudentForm
from .models import StudentData


# Display All Students
def AllStudents(request):
    all_students = StudentData.objects.all().order_by('id')

    return render(request, "allstudents.html", {
        "all_students": all_students
    })


# Add New Student
def AddStudent(request):
    if request.method == "POST":
        add_form = StudentForm(request.POST)

        if add_form.is_valid():
            try:
                student = add_form.save(commit=False)

                used_ids = set(
                    StudentData.objects.values_list('id', flat=True)
                )

                next_id = 1
                while next_id in used_ids:
                    next_id += 1

                student.id = next_id
                student.save()

                return redirect("allstudents")

            except IntegrityError:
                add_form.add_error(
                    None,
                    "Unable to assign student ID. Please try again."
                )
    else:
        add_form = StudentForm()

    return render(request, "addstudent.html", {
        "add_form": add_form
    })


# Edit Student
def EditStudent(request, id):
    student = get_object_or_404(StudentData, id=id)

    if request.method == "POST":
        editForm = StudentForm(request.POST, instance=student)

        if editForm.is_valid():
            editForm.save()
            return redirect("allstudents")
    else:
        editForm = StudentForm(instance=student)

    return render(request, "editstudent.html", {
        "editForm": editForm
    })


# Delete Student
def DeleteStudent(request, id):
    student = get_object_or_404(StudentData, id=id)

    if request.method == "POST":
        student.delete()

    return redirect("allstudents")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import CustomUser, Standard, Session_Year, Student
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Hod/home.html')


@login_required(login_url='/')
def ADD_STUDENT(request):
    standard = Standard.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        standard_id = request.POST.get('standard_id')
        session_year_id = request.POST.get('session_year_id')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email Is Already Taken")
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username Is Already Taken")
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            standard = Standard.objects.get(id=standard_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                standard_id=standard,
                gender=gender,
            )
            student.save()
            messages.success(request, user.first_name + ' ' +
                             user.last_name + ' is Successfully Added.')
            return redirect('add_student')

    context = {
        'standard': standard,
        'session_year': session_year,
    }
    return render(request, 'Hod/add_student.html', context)


@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student': student,
    }

    return render(request, 'Hod/view_students.html', context)


@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id=id)
    standard = Standard.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student': student,
        'standard': standard,
        'session_year': session_year,
    }
    return render(request, 'Hod/edit_student.html', context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        standard_id = request.POST.get('standard_id')
        session_year_id = request.POST.get('session_year_id')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')

        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        if password != None and password != "":
            user.set_password(password)

        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        standard = Standard.objects.get(id=standard_id)
        student.standard_id = standard

        session_year = Session_Year.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save()

        messages.success(request, 'Record Is Successfully Updated!')
        return redirect('view_student')

    return render(request, 'Hod/edit_student.html')


@login_required(login_url='/')
def DELETE_STUDENT(request, admin_id):
    student = CustomUser.objects.get(id=admin_id)
    student.delete()
    messages.success(request, 'Record Is Successfully Deleted.')
    return redirect('view_student')


@login_required(login_url='/')
def ADD_STANDARD(request):
    if request.method == "POST":
        standard_name = request.POST.get('standard_name')

        standard = Standard(
            name=standard_name,
        )
        standard.save()
        messages.success(request, 'Standard Is Successfully Created.')
        return redirect('add_standard')

    return render(request, 'Hod/add_standard.html')


@login_required(login_url='/')
def ADD_STANDARD(request):
    if request.method == "POST":
        standard_name = request.POST.get('standard_name')

        standard = Standard(
            name=standard_name,
        )
        standard.save()

        messages.success(request, 'Standard Is Successfully Created.')
        return redirect('add_standard')

    return render(request, 'Hod/add_standard.html')


@login_required(login_url='/')
def VIEW_STANDARD(request):
    standard = Standard.objects.all()

    context = {
        'standard': standard,
    }

    return render(request, 'Hod/view_standards.html', context)


@login_required(login_url='/')
def EDIT_STANDARD(request, standard_id):
    standard = Standard.objects.get(id=standard_id)

    context = {
        'standard': standard,
    }
    return render(request, 'Hod/edit_standard.html', context)


@login_required(login_url='/')
def UPDATE_STANDARD(request):
    if request.method == "POST":
        standard_id = request.POST.get('standard_id')
        name = request.POST.get('standard_name')

        standard = Standard.objects.get(id=standard_id)
        standard.name = name
        standard.save()

        messages.success(request, 'Course Is Successfully Updated.')
        return redirect('view_standard')

    return render(request, 'Hod/view_standards.html')


@login_required(login_url='/')
def DELETE_STANDARD(request, standard_id):
    standard = Standard.objects.get(id=standard_id)
    standard.delete()

    messages.success(request, 'Course Is Successfully Deleted.')
    return redirect('view_standard')

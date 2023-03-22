from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from app.models import CustomUser, Session_Year, Staff, Standard, Student


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


@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email Is Already Taken")
            return redirect('add_staff')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username Is Already Taken")
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=2,
            )

            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
            )

            staff.save()

            messages.success(request, 'Staff Is Successfully Added.')
            return redirect('add_staff')

    return render(request, 'Hod/add_staff.html')


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff,
    }

    return render(request, 'Hod/view_staff.html', context)


@login_required(login_url='/')
def EDIT_STAFF(request, staff_id):
    staff = Staff.objects.get(id=staff_id)

    context = {
        'staff': staff,
    }
    return render(request, 'Hod/edit_staff.html', context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        staff_id = request.POST.get('staff_id')

        user = CustomUser.objects.get(id=staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        if password != None and password != "":
            user.set_password(password)

        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address
        staff.save()

        messages.success(request, 'Staff Is Successfully Updated.')
        return redirect('view_staff')

    return redirect('view_staff')


@login_required(login_url='/')
def DELETE_STAFF(request, staff_id):
    staff = CustomUser.objects.get(id=staff_id)
    staff.delete()

    messages.success(request, 'Staff is Deleted')
    return redirect('view_staff')

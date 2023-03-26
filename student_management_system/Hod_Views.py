from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from app.models import (Attendance, Attendance_Report, CustomUser, Session_Year,
                        Staff, Staff_Feedback, Staff_Leave, Staff_Notification,
                        Standard, Student, Student_Feedback, Student_Leave,
                        Student_Notification, Subject)


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    standard_count = Standard.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()

    context = {
        'student_count': student_count,
        'staff_count': staff_count,
        'standard_count': standard_count,
        'subject_count': subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }
    return render(request, 'Hod/home.html', context)


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


@login_required(login_url='/')
def ADD_SUBJECT(request):
    standard = Standard.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        standard_id = request.POST.get('standard_id')
        staff_id = request.POST.get('staff_id')

        standard = Standard.objects.get(id=standard_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name=subject_name,
            standard=standard,
            staff=staff,
        )

        subject.save()
        messages.success(request, subject_name + ' Is Successfully Added.')
        return redirect('add_subject')

    context = {
        'standard': standard,
        'staff': staff,
    }

    return render(request, 'Hod/add_subject.html', context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()

    context = {
        'subject': subject,
    }

    return render(request, 'Hod/view_subject.html', context)


@login_required(login_url='/')
def EDIT_SUBJECT(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    standard = Standard.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject': subject,
        'standard': standard,
        'staff': staff,
    }

    return render(request, 'Hod/edit_subject.html', context)


@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        standard_id = request.POST.get('standard_id')
        staff_id = request.POST.get('staff_id')

        standard = Standard.objects.get(id=standard_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject.objects.get(id=subject_id)
        subject.name = subject_name
        subject.staff = staff
        subject.standard = standard

        subject.save()
        messages.success(request, 'Subject Is Successfully Updated')
        return redirect('view_subject')

        return None
    return redirect('view_subject')


@login_required(login_url='/')
def DELETE_SUBJECT(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()

    messages.success(request, 'Subject Is Successfully Deleted.')
    return redirect('view_subject')


@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            session_start=session_year_start,
            session_end=session_year_end,
        )

        session.save()
        messages.success(request, 'Session Year Is Successfully Added.')
        return redirect('add_session')
    return render(request, 'Hod/add_session.html')


@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session_Year.objects.all()

    context = {
        'session': session,
    }

    return render(request, 'Hod/view_session.html', context)


@login_required(login_url='/')
def EDIT_SESSION(request, session_id):
    session = Session_Year.objects.get(id=session_id)

    context = {
        'session': session,
    }

    return render(request, 'Hod/edit_session.html', context)


@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year.objects.get(id=session_id)
        session.session_start = session_year_start
        session.session_end = session_year_end

        session.save()

        messages.success(request, 'Session Year Successfully Updated.')
        return redirect('view_session')
    return redirect('view_session')


@login_required(login_url='/')
def DELETE_SESSION(request, session_id):
    session = Session_Year.objects.get(id=session_id)
    session.delete()

    messages.success(request, 'Session Year Is Successfully Deleted.')
    return redirect('view_session')


@login_required(login_url='/')
def SEND_STAFF_NOTIFICATION(request):
    staff = Staff.objects.all()
    seen_notification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'staff': staff,
        'seen_notification': seen_notification,
    }

    return render(request, 'Hod/send_staff_notification.html', context)


def SEND_STUDENT_NOTIFICATION(request):
    student = Student.objects.all()
    seen_notification = Student_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'student': student,
        'seen_notification': seen_notification,
    }

    return render(request, 'Hod/send_student_notification.html', context)


def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)
        notification = Staff_Notification(
            staff_id=staff,
            message=message,
        )

        notification.save()
        messages.success(request, 'Notifiation is Succesfully Sent.')
        return redirect('send_staff_notification')


def SAVE_STUDENT_NOTIFICATION(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')

        student = Student.objects.get(admin=student_id)
        notification = Student_Notification(
            student_id=student,
            message=message,
        )

        notification.save()
        messages.success(request, 'Notifiation is Succesfully Sent.')
        return redirect('send_student_notification')


def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()

    context = {
        'staff_leave': staff_leave,
    }

    return render(request, 'Hod/staff_leave.html', context)


def STAFF_APPROVE_LEAVE(request, id):
    leave_id = Staff_Leave.objects.get(id=id)
    leave_id.status = 1
    leave_id.save()
    return redirect('staff_leave_view')


def STAFF_DISAPPROVE_LEAVE(request, id):
    leave_id = Staff_Leave.objects.get(id=id)
    leave_id.status = 2
    leave_id.save()
    return redirect('staff_leave_view')


def STUDENT_LEAVE_VIEW(request):
    student_leave = Student_Leave.objects.all()

    context = {
        'student_leave': student_leave,
    }

    return render(request, 'Hod/student_leave.html', context)


def STUDENT_APPROVE_LEAVE(request, id):
    leave_id = Student_Leave.objects.get(id=id)
    leave_id.status = 1
    leave_id.save()
    return redirect('student_leave_view')


def STUDENT_DISAPPROVE_LEAVE(request, id):
    leave_id = Student_Leave.objects.get(id=id)
    leave_id.status = 2
    leave_id.save()
    return redirect('student_leave_view')


def STAFF_FEEDBACK_REPLY(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all()
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history,
    }
    return render(request, 'Hod/staff_feedback.html', context)


def STUDENT_FEEDBACK_REPLY(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all()

    context = {
        'feedback': feedback,
        'feedback_history': feedback_history,
    }
    return render(request, 'Hod/student_feedback.html', context)


def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1

        feedback.save()
        messages.success(request, 'Reply Successfully Sent')
        return redirect('staff_feedback_reply')


def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1

        feedback.save()
        messages.success(request, 'Reply Successfully Sent')
        return redirect('student_feedback_reply')


def VIEW_ATTENDANCE(request):
    subject = Subject.objects.all()
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            attendance = Attendance.objects.filter(
                subject_id=get_subject,
                attendance_date=attendance_date,
            )

            for i in attendance:
                attendance_id = i.id

                attendance_report = Attendance_Report.objects.filter(
                    attendance_id=attendance_id)

    context = {
        'subject': subject,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }

    return render(request, 'Hod/view_attendance.html', context)

from django.contrib import messages
from django.shortcuts import redirect, render

from app.models import Staff, Staff_Feedback, Staff_Leave, Staff_Notification


def HOME(request):
    return render(request, 'Staff/home.html')


def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id=staff_id)
        context = {
            'notification': notification,
        }

        return render(request, 'Staff/notification.html', context)


def STAFF_NOTIFICATION_MARK_AS_DONE(request, staff_notification_id):
    notification = Staff_Notification.objects.get(id=staff_notification_id)
    notification.status = 1
    notification.save()
    return redirect('notifications')


def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)

        context = {
            'staff_leave_history': staff_leave_history,
        }
    return render(request, 'Staff/apply_leave.html', context)


def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff = Staff.objects.get(admin=request.user.id)

        leave = Staff_Leave(
            staff_id=staff,
            date=leave_date,
            message=leave_message,
        )

        leave.save()
        messages.success(request, 'Leave Application Is Successfully Sent.')
        return redirect('staff_apply_leave')


def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history': feedback_history,
    }

    return render(request, 'Staff/feedback.html', context)


def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        staff_id = Staff.objects.get(admin=request.user.id)

        feedback = Staff_Feedback(
            staff_id=staff_id,
            feedback=feedback,
            feedback_reply='',
        )
        feedback.save()
        messages.success(request, 'Feedback Successfully Sent.')
        return redirect('staff_feedback')

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import Hod_Views, Staff_Views, Student_Views, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # Login Path
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # Profile Update
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # This is HOD Panel Url
    # Student Functions Path
    path('Hod/Home', Hod_Views.HOME, name='hod_home'),
    path('Hod/Student/Add', Hod_Views.ADD_STUDENT, name='add_student'),
    path('Hod/Student/View', Hod_Views.VIEW_STUDENT, name='view_student'),
    path('Hod/Student/Edit/<str:id>', Hod_Views.EDIT_STUDENT, name='edit_student'),
    path('Hod/Student/Update', Hod_Views.UPDATE_STUDENT, name='update_student'),
    path('Hod/Student/Delete/<str:admin_id>',
         Hod_Views.DELETE_STUDENT, name='delete_student'),

    # Staff Functions Path
    path('Hod/Staff/Add', Hod_Views.ADD_STAFF, name='add_staff'),
    path('Hod/Staff/View', Hod_Views.VIEW_STAFF, name='view_staff'),
    path('Hod/Staff/Edit/<str:staff_id>',
         Hod_Views.EDIT_STAFF, name='edit_staff'),
    path('Hod/Staff/Update', Hod_Views.UPDATE_STAFF, name='update_staff'),
    path('Hod/Staff/Delete/<str:staff_id>',
         Hod_Views.DELETE_STAFF, name='delete_staff'),

    # Standard Functions Path
    path('Hod/Standard/Add', Hod_Views.ADD_STANDARD, name='add_standard'),
    path('Hod/Standard/View', Hod_Views.VIEW_STANDARD, name='view_standard'),
    path('Hod/Standard/Edit/<str:standard_id>',
         Hod_Views.EDIT_STANDARD, name='edit_standard'),
    path('Hod/Standard/Update', Hod_Views.UPDATE_STANDARD, name='update_standard'),
    path('Hod/Standard/Delete/<str:standard_id>',
         Hod_Views.DELETE_STANDARD, name='delete_standard'),

    # Subject Functions Path
    path('Hod/Subject/Add', Hod_Views.ADD_SUBJECT, name='add_subject'),
    path('Hod/Subject/View', Hod_Views.VIEW_SUBJECT, name='view_subject'),
    path('Hod/Subject/Edit/<str:subject_id>',
         Hod_Views.EDIT_SUBJECT, name='edit_subject'),
    path('Hod/Subject/Update', Hod_Views.UPDATE_SUBJECT, name='update_subject'),
    path('Hod/Subject/Delete/<str:subject_id>',
         Hod_Views.DELETE_SUBJECT, name='delete_subject'),

    # Session
    path('Hod/Session/Add', Hod_Views.ADD_SESSION, name='add_session'),
    path('Hod/Session/View', Hod_Views.VIEW_SESSION, name='view_session'),
    path('Hod/Session/Edit/<str:session_id>',
         Hod_Views.EDIT_SESSION, name='edit_session'),
    path('Hod/Session/Update', Hod_Views.UPDATE_SESSION, name='update_session'),
    path('Hod/Session/Delete/<str:session_id>',
         Hod_Views.DELETE_SESSION, name='delete_session'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

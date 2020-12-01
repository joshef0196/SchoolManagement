
from django.urls import path
from . import views, test_api as obj
urlpatterns = [
    path('', views.index_page),
    path('our-history/', views.our_history),
    path('institute-message/', views.institute_message),
    path('chairman-message/', views.chairman_message),
    path('principal-message/', views.principal_message),
    path('institute/teachers/', views.teacher_info),
    path('institute/managemeng-committee/', views.committee_info),
    path('institute/at-glance/', views.at_a_glance),
    path('institute/why-study/', views.why_study_here),
    path('institute/facility/', views.institute_facility),
    path('all-notices/', views.all_notices),
    path('gallery/photo-gallery/', views.photo_gallery),
    path('gallery/video-gallery/', views.video_gallery),
    path('notice/<int:id>/view/', views.view_notices),
    path('all-events/', views.all_events),
    path('events/<int:id>/view/', views.view_events),
    path('institute/eiin-number/', views.eiin_number),
    path('institute/library/', views.library_page),
    path('institute/hostel/', views.hostel_page),
    path('institute/lab/', views.lab_page),
    path('institute/idcard/', views.idcard_page),
    path('institute/quran-class/', views.quran_class),
    path('institute/bncc/', views.bncc_page),
    path('institute/scout/', views.scout_page),
    path('admission/', views.admission_form),
    path('exam-regulations/', views.exam_regulations),
    path('admission-suspension/', views.admission_suspension),
    path('admission-information/', views.admission_information),
    path('job-vacancy/', views.job_vacancy),
    path('contact-us/', views.contact_us),
    path('result-history/', views.result_history),
    path('login/', views.login),
    path('logout/', views.admin_logout),
    path('search-result/', views.search_result),
    # path('student/class-load/',views.load_student_class),
    # Api
    # path('api/', views.test_api),

    # Dashboard
    path('dashboard/', views.dashboard),
    path('student-registration/', views.student_reg),
    path('quick-admission/', views.quick_admission),
    path('quick-admission-list/', views.quick_admission_list),
    path('student-list/', views.student_list),
    path('remove-student/<int:id>/', views.remove_student),
    path('student-photos-list/', views.student_photos_list),
    path('parents-list/', views.parents_list),
    path('parents-photos-list/', views.parents_photos_list),
    path('guardian-list/', views.guardian_list),
    path('guardian-photo-list/', views.guardian_photos_list),
    path('scholarship-student-list/', views.scholarship_student_list),
    path('inactive-student-list/', views.inactive_student_list),
    path('employee-registration/', views.employee_reg),
    path('employee-list/', views.employee_list),
    path('remove-employee/<int:id>', views.remove_employee),
    path('add-class-teacher/', views.add_class_teacher),
    path('teacher-list/', views.teacher_list),
    path('class-teacher-assign-delete/<int:id>/', views.delete_teacher),

    path('student-exam-marks-entry/', views.student_exam_mark),
    path('mark-distribution/', views.mark_distribution),
    path('mark-distribution-list/', views.mark_distribution_list),
    path('remove-mark-distribution/<int:id>', views.delete_mark_distribution),
    

    path('api/', views.apiTest),

    # Export in Excel
    path('export-student-sheet/', views.export_student_list),

    # report 
    path('class-wise-report/', views.class_wise_report),

    # API
    path('apps/student-list', obj.student_list),
    
]

from django.contrib import admin
from . import models

class HomeContentAdmin(admin.ModelAdmin):
    list_display    = ['content_for', 'pub_date', 'status',]
    search_fields   = [ 'pub_date', 'status',]
    list_filter     = ['status',]

class SliderInfoAdmin(admin.ModelAdmin):
    list_display    = [ 'slider_for','slider_title', 'slider_order', 'slider_images', 'upload_date', 'status',]
    search_fields   = ['slider_title', 'slider_order', 'status',]
    list_filter     = ['status',]

class ActivitiesAdmin(admin.ModelAdmin):
    list_display    = ['activites_name', 'icon', 'order', 'status',]
    search_fields   = ['activites_name', 'status',]
    list_filter     = ['status',]

class FacilityItemAdmin(admin.ModelAdmin):
    list_display    = ['facility_title', 'facility_type', 'status',]
    search_fields   = ['facility_title', 'status',]
    list_filter     = ['status',]

class SchoolProfileAdmin(admin.ModelAdmin):
    list_display    = ['school_name', 'email', 'phone',  'mobile', 'web_address', 'status',]
    search_fields   = ['school_name', 'email', 'phone',  'mobile', 'status',]
    list_filter     = ['status',]

class GalleryInfoAdmin(admin.ModelAdmin):
    list_display    = ['gallery_type', 'gallery_title','gallery_for',  'gallery_order', 'gallery_images', 'status',]
    search_fields   = ['gallery_title',]
    list_filter     = ['status',]

class AcademicTeamAdmin(admin.ModelAdmin):
    list_display    = ['academic_member','member_name','designation', 'qualification', 'email', 'team_order', 'status']
    search_fields   = ['member_name', 'email', 'mobile',]
    list_filter     = ['status',]

class AcademicMessageAdmin(admin.ModelAdmin):
    list_display    = ['message_for', 'upload_date', 'status']
    search_fields   = ['message_for', 'upload_date', 'status']
    list_filter     = ['status',]


class NoticeAndEventAdmin(admin.ModelAdmin):
    list_display    = ['notice_or_event','title', 'upload_date', 'status']
    search_fields   = ['notice_or_event','title', 'upload_date', 'status']
    list_filter     = ['status',]

class ImportantLinkAdmin(admin.ModelAdmin):
    list_display    = ['link_name','link_url', 'order', 'status']
    search_fields   = ['link_name', 'status']
    list_filter     = ['status',]

class JobCircularAdmin(admin.ModelAdmin):
    list_display    = ['job_title', 'deadline', 'publish_date', 'status']
    search_fields   = ['job_title', 'deadline',]
    list_filter     = ['status',]

class ContactAdmin(admin.ModelAdmin):
    list_display    = ['name', 'email','subject','message_date','status']
    search_fields   = ['email']
    date_hierarchy = 'message_date'

class StudentAdmin(admin.ModelAdmin):
    list_display    = ['st_first_name', 'student_id','status']


class AdminSubject(admin.ModelAdmin):
    list_display    = ['sub_name', 'sub_code','ordering','status']


admin.site.register(models.HomeContent, HomeContentAdmin)
admin.site.register(models.SliderInfo, SliderInfoAdmin)
admin.site.register(models.Activities, ActivitiesAdmin)
admin.site.register(models.FacilityItem, FacilityItemAdmin)
admin.site.register(models.SchoolProfile, SchoolProfileAdmin)
admin.site.register(models.GalleryInfo, GalleryInfoAdmin)
admin.site.register(models.AcademicTeam, AcademicTeamAdmin)
admin.site.register(models.AcademicMessage, AcademicMessageAdmin)
admin.site.register(models.NoticeAndEvent, NoticeAndEventAdmin)
admin.site.register(models.ImportantLink, ImportantLinkAdmin)
admin.site.register(models.JobCircular, JobCircularAdmin)
admin.site.register(models.ExamAdvice)
admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.AdmissionRequest)
admin.site.register(models.ExamInfo)
admin.site.register(models.GroupTypeList)
admin.site.register(models.Department)
admin.site.register(models.Shift)
admin.site.register(models.Section)
admin.site.register(models.SessionInfo)
admin.site.register(models.ClassInfo)
admin.site.register(models.Years)
admin.site.register(models.Subject, AdminSubject)
# admin.site.register(models.ClassSubject)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.EmployeeList)
admin.site.register(models.TeacherList)
admin.site.register(models.MarkDistribution)
admin.site.register(models.Result)



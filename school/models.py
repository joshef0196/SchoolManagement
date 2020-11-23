import os
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField    
from datetime import datetime
from django.utils import timezone

    

class HomeContent(models.Model):
    content_type = (
        ('1',  'Academic History'),
        ('2',  'At a Glance'),
        ('3',  'Why Study'),
    )
    content_for  = models.CharField(max_length=1, choices = content_type)
    details      = RichTextField(blank=True)
    pub_date     = models.DateField(auto_now_add = True)
    status       = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.content_for)
    
    class Meta:
        verbose_name = 'Home Content'
        verbose_name_plural = 'Home Contents'

class SliderInfo(models.Model):
    type = (
        ('1',  'Slider'),
        ('2',  'Corner Message'),
    )
    slider_for     = models.CharField(max_length=3, choices=type)
    slider_title   = models.CharField(max_length=100, blank=True)
    details        = models.TextField(max_length=5000, blank=True)
    slider_images  = models.ImageField(upload_to='images/slider')
    slider_order   = models.IntegerField()
    status         = models.BooleanField(default=True)
    upload_date    = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.slider_title

    class Meta:
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'

class Activities(models.Model):
    activites_name      = models.CharField(max_length=60)
    icon                = models.CharField(max_length=60, blank=True)
    details             = RichTextField()
    order               = models.IntegerField()
    status              = models.BooleanField(default=True)
    
    def __str__(self):
        return self.activites_name

    class Meta:
        verbose_name = 'Activities'
        verbose_name_plural = 'Activities'

class FacilityItem(models.Model):
    type = (
        ('1',  'Library'),
        ('2',  'Hostel'),
        ('3',  'Lab'),
        ('4',  'ID Card'),
    )
    facility_type       = models.CharField(max_length=1, choices=type)
    facility_title      = models.CharField(max_length=260)
    details             = RichTextField()
    facility_images     = models.ImageField(upload_to='images/facility_images')
    upload_date         = models.DateTimeField(auto_now_add=True)
    status              = models.BooleanField(default=True)
    
    def __str__(self):
        return self.facility_title

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facility Items'

class SchoolProfile(models.Model):
    school_name       = models.CharField(max_length=160)
    slugan            = models.CharField(max_length=100, blank=True)
    email             = models.EmailField(max_length=70,blank=True)
    phone             = models.CharField(max_length=20)
    mobile            = models.CharField(max_length=15)
    address           = models.CharField(max_length=200)
    web_address       = models.CharField(max_length=200,blank=True)
    logo              = models.ImageField(upload_to='images/company_info')
    facebook_id       = models.CharField(max_length=200,blank=True)
    twitter_id        = models.CharField(max_length=200,blank=True)
    google_id         = models.CharField(max_length=200,blank=True)
    youtube_id        = models.CharField(max_length=200,blank=True)
    linkedin_id       = models.CharField(max_length=200,blank=True)
    copyright_name    = models.CharField(max_length=200,blank=True)
    status            = models.BooleanField(default=True)
    
    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name = 'School Profile'
        verbose_name_plural = 'School Info'


class GalleryInfo(models.Model):
    type = (
        ('1',  'Video Gallery'),
        ('2',  'Photo Gallery'),
    )
    gallery_type  = models.CharField(max_length=3, choices=type)
    image_choice = (
        ('1',  'Hostel'),
        ('2',  'Library'),
        ('3',  'Lab'),
        ('5',  'ID Card'),
    )
    gallery_for  = models.CharField(max_length=3, choices=image_choice, blank=True)
    gallery_title   = models.CharField(max_length=100, blank=True)
    gallery_images  = models.ImageField(upload_to='images/gallery', blank=True)
    gallery_link    = models.TextField(blank=True)
    gallery_order   = models.IntegerField()
    status          = models.BooleanField(default=True)
    upload_date     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery_title

    class Meta:
        verbose_name = 'Gallery Info'
        verbose_name_plural = 'Add Gallery'


class AcademicTeam(models.Model):
    academic_member_type = (
        ('1',  'Management Committee '),
        ('2',  'Teacher'),
        ('4',  'Hostel Staff'),
       
    )
    academic_member  = models.CharField(max_length=3, choices=academic_member_type)
    member_name      = models.CharField(max_length=200)
    email            = models.EmailField(max_length=60,blank=True)
    mobile           = models.CharField(max_length=20,blank=True)
    designation      = models.CharField(max_length=50,blank=True)
    qualification    = models.CharField(max_length=40,blank=True)
    date_of_birth    = models.DateField(auto_now_add = False)
    genders = (
        ('1',  'Male'),
        ('2',  'Female'),
        ('3',  'Others'),
    )
    gender           = models.CharField(max_length=1, choices = genders)
    address          = models.CharField(max_length=500,blank=True)
    member_image     = models.FileField(upload_to='images/team',blank=True)
    message          = models.TextField(max_length=5000, blank=True)
    team_order       = models.IntegerField(default=0)
    facebook_id      = models.CharField(max_length=100,blank=True)
    twitter_id       = models.CharField(max_length=100,blank=True)
    youtube_id       = models.CharField(max_length=100,blank=True)
    linkedin_id      = models.CharField(max_length=100,blank=True)
    add_date         = models.DateField(auto_now_add = True)
    status           = models.BooleanField(default=True) 

    def __str__(self):
        return str(self.member_name)

    class Meta:
        verbose_name = 'Academic Member'
        verbose_name_plural = 'Academic Teams'


class AcademicMessage(models.Model):
    message_type = (
        ('1',  'Welcome Message'),
        ('2',  'Chairman Message'),
        ('3',  'Principal Message'),
        
    )
    message_for     = models.CharField(max_length=1, choices=message_type)
    # message_title   = models.CharField(max_length=100, blank=True)
    details         = RichTextField(blank=True)
    persion_images  = models.ImageField(upload_to='images/institute', blank=True)
    status          = models.BooleanField(default=True)
    upload_date     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message_for)

    class Meta:
        verbose_name = 'Academic Message'
        verbose_name_plural = 'Academic Message'


class ExamAdvice(models.Model):
    name             = models.CharField(max_length=100, blank=True)
    email            = models.EmailField(max_length=60,blank=True)
    mobile           = models.CharField(max_length=20,blank=True)
    designation      = models.CharField(max_length=50,blank=True)
    persion_images   = models.ImageField(upload_to='images/advisor', blank=True)
    status           = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Exam Advice'
        verbose_name_plural = 'Exam Advices'



class NoticeAndEvent(models.Model):
    type = (
        ('1',  'Notice'),
        ('2',  'Events'),
    )
    notice_or_event  = models.CharField(max_length=3, choices=type)
    title            = models.CharField(max_length=100, blank=True)
    details          = RichTextField(blank=True)
    upload_images    = models.ImageField(upload_to='images/notice_event_image', blank=True)
    notice_file      = models.FileField(upload_to='images/notice_file', blank=True)
    upload_date      = models.DateField(auto_now_add=True)
    status           = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Notice Event'
        verbose_name_plural = 'Add Notice and Event'



class ImportantLink(models.Model):
    link_name      = models.CharField(max_length=100)
    link_url       = models.CharField(max_length=60, blank=True)
    order          = models.IntegerField()
    status         = models.BooleanField(default=True)

    def __str__(self):
        return self.link_name

    class Meta:
        verbose_name = 'Important Link'
        verbose_name_plural = 'Add Important Link'

class JobCircular(models.Model):
    job_title       = models.CharField(max_length=100, blank=True)
    deadline        = models.DateField(auto_now_add = False)
    publish_date    = models.DateField(auto_now_add = True)
    location        = models.CharField(max_length=100, blank=True)
    vancancy_images = models.FileField(upload_to='images/vancancy_images')
    status          = models.BooleanField(default=True)

    
    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Job Circular'
        verbose_name_plural = 'Jobs Circulars'


class Contact(models.Model):
    name             = models.CharField(max_length = 100)
    email            = models.EmailField(max_length = 100,blank = True)
    subject          = models.CharField(max_length = 150)
    phone            = models.CharField(max_length = 20)
    message          = RichTextField()
    message_date     = models.DateTimeField(auto_now_add=True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts' 

class AdmissionRequest(models.Model):
    student_name             = models.CharField(max_length = 100)
    father_name             = models.CharField(max_length = 100)
    mother_name             = models.CharField(max_length = 100)
    class_list = (
        ('1',  'প্রথম শ্রেণী'),
        ('2',  'দ্বিতীয় শ্রেণী'),
        ('3',  'তৃতীয় শ্রেণী'),
        ('4',  'চতুর্থ শ্রেণী'),
        ('5',  'পঞ্চম শ্রেণী'),
        ('6',  'ষষ্ঠ শ্রেণী'),
        ('7',  'সপ্তম শ্রেণী'),
        ('8',  'অষ্টম শ্রেণী'),
        ('9',  'নবম শ্রেণী'),
    )
    class_for        = models.CharField(max_length=1, choices = class_list)
    group_list = (
        ('1',  'Science'),
        ('2',  'Business'),
        ('3',  'Humanities'),
    )
    group_for        = models.CharField(max_length=1, choices = group_list, blank = True, null=True)
    email            = models.EmailField(max_length = 100, blank = True)
    phone            = models.CharField(max_length = 20)
    address          = models.CharField(max_length = 150)
    request_date     = models.DateTimeField(auto_now_add=True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.student_name   

    class Meta:
        verbose_name = 'Admission Request'
        verbose_name_plural = 'Admission Requests' 


# .....................................admin.....................................................



class ExamInfo(models.Model):
    exam_name              = models.CharField(max_length=50, unique=True)
    exam_short_name        = models.CharField(max_length=10, blank=True)
    detail                 = models.CharField(max_length=100, blank=True)
    dependency             = models.BooleanField(default = 0)
    marks_entry_last_date  = models.DateField(auto_now_add = False, null=True, blank = True)
    insert_date            = models.DateTimeField(auto_now_add=True)
    last_update            = models.DateTimeField(auto_now=True)
    insert_by              = models.IntegerField(default=0)
    update_by              = models.IntegerField(default=0)
    status                 = models.BooleanField(default = 1)
    def __str__(self):
        return self.exam_name

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Examinations"   


class GroupTypeList(models.Model):
    group_type    = models.CharField(max_length=50, unique=True)
    insert_date   = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    insert_by     = models.IntegerField(default=0)
    update_by     = models.IntegerField(default=0)
    status        = models.BooleanField(default=1)

    def __str__(self):
        return self.group_type

    class Meta:
        verbose_name = "Group Type"
        verbose_name_plural = "Group Types"    

class Department(models.Model):
    dpt_name    = models.CharField(max_length=50, unique=True)
    dpt_code    = models.CharField(max_length=10, blank=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    insert_by   = models.IntegerField(default=0)
    update_by   = models.IntegerField(default=0)
    status      = models.BooleanField(default=1)

    def __str__(self):
        return self.dpt_name

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"   

class Shift(models.Model):
    shift_name    = models.CharField(max_length=20, unique=True)
    insert_date   = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    insert_by     = models.IntegerField(default=0)
    update_by     = models.IntegerField(default=0)
    status        = models.BooleanField(default=1)

    def __str__(self):
        return self.shift_name

    class Meta:
        verbose_name = "Shift"
        verbose_name_plural = "Shifts"   

class Section(models.Model):
    section_name  = models.CharField(max_length=20, unique=True)
    insert_date   = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    insert_by     = models.IntegerField(default=0)
    update_by     = models.IntegerField(default=0)
    status        = models.BooleanField(default=1)

    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"   

class SessionInfo(models.Model):
    session_name  = models.CharField(max_length=20, unique=True)
    insert_date   = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    insert_by     = models.IntegerField(default=0)
    update_by     = models.IntegerField(default=0)
    status        = models.BooleanField(default=1)

    def __str__(self):
        return self.session_name

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"   

class ClassInfo(models.Model):
    class_name    = models.CharField(max_length=20, unique=True)
    class_code    = models.IntegerField(default=0)
    insert_date   = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(default = timezone.now)
    insert_by     = models.IntegerField(default=0)
    update_by     = models.IntegerField(default=0)
    status        = models.BooleanField(default=1)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

class Years(models.Model):
    year          = models.IntegerField(default=0, unique=True)
    insert_date   = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    insert_by     = models.IntegerField(default=0)
    update_by     = models.IntegerField(default=0)
    status        = models.BooleanField(default=1)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Year"
        verbose_name_plural = "Years" 
        
class Subject(models.Model):
    sub_name      = models.CharField(max_length=50, unique=True)
    sub_code      = models.CharField(max_length=10)
    insert_date   = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    ordering      = models.IntegerField(default=0)
    status        = models.BooleanField(default=1)

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"   

class ClassSubject(models.Model):
    class_name      = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    sub_name        = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year            = models.ForeignKey(Years, on_delete=models.CASCADE)
    sub_type = (
        ('1', 'Compulsory'),
        ('2', 'Religion'),
        ('3', 'Optional'),
        ('4', 'Pair Subject'),
        ('5', 'Group Subject'),
    )
    sub_type         = models.CharField(max_length = 1, choices=sub_type)
    pair_sub         = models.IntegerField(default = 0)
    # group_type       = models.ForeignKey(GroupTypeList, on_delete = models.CASCADE, blank = True, null = True)
    group_list = (
        ('1',  'Science'),
        ('2',  'Business'),
        ('3',  'Humanities'),
    )
    group_for        = models.CharField(max_length=1, choices = group_list, blank = True, null=True)    
    subject_priority = models.IntegerField(default = 0)
    ordering         = models.IntegerField(default = 0)
    insert_date      = models.DateTimeField(auto_now_add=True)
    last_update      = models.DateTimeField(auto_now=True)
    insert_by        = models.IntegerField(default=0)
    update_by        = models.IntegerField(default=0)
    status           = models.BooleanField(default = 1)
    
    def __str__(self):
        return "{} {} {}".format(self.class_name," - ",self.sub_name)   

    class Meta:
        verbose_name = "Class Subject"
        verbose_name_plural = "Class Subjects"   


class Student(models.Model):
    student_id            = models.IntegerField(default=0, unique=True)
    student_img           = models.ImageField(upload_to='student_img',blank=True)
    st_first_name         = models.CharField('Student First Name',max_length=40)
    st_last_name          = models.CharField(max_length=30, blank=True)
    st_bangla_name        = models.CharField(max_length=50, blank=True)
    # st_religion           = models.ForeignKey(Religion, on_delete=models.CASCADE)
    
    genders_types         = (
        ('1',  'Male'),
        ('2',  'Female'),
        ('3',  'Others'),
    )
    st_gender             = models.CharField(max_length=1, choices = genders_types)
    religion_types        = (
        ('1',  'Islam'),
        ('2',  'Christianity'),
        ('3',  'Hinduism'),
        ('4',  'Buddhism'),
        ('5',  'Chinese traditional religion'),
        ('6',  'African traditional religions'),
    )
    st_religion             = models.CharField(max_length=1, choices = religion_types)   
    date_of_birth           = models.DateField(auto_now_add=False)
    birth_certificate_no    = models.CharField(max_length=30, blank=True)    
    # nationality             = models.CharField(max_length=30, blank=True)
    st_mobile               = models.CharField(max_length=15, blank=True)
    group_type = (
        ('1', 'N/A'),
        ('2', 'A+'),
        ('3', 'A-'),
        ('4', 'B+'),
        ('5', 'B-'),
        ('6', 'AB+'),
        ('7', 'AB-'),
        ('8', 'O+'),
        ('9', 'O-'),
    )
    st_blood_group          = models.CharField(max_length=2, choices=group_type,blank=True) 
    st_email                = models.EmailField(max_length=90, blank=True)
    st_roll                 = models.IntegerField(default=0)
    st_reg                  = models.IntegerField(default=0)
    psc_roll                = models.IntegerField(default=0, blank=True)
    jsc_roll                = models.IntegerField(default=0, blank=True)
    class_name              = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    shift_name              = models.ForeignKey(Shift, on_delete=models.CASCADE)
    section_name            = models.ForeignKey(Section, on_delete=models.CASCADE)
    session_name            = models.ForeignKey(SessionInfo, on_delete=models.CASCADE)
    running_year            = models.ForeignKey(Years, on_delete=models.CASCADE)
    fitness_details         = models.TextField(blank=True)
    medical_certificate     = models.ImageField(upload_to='medical_certificate', blank=True)
    group_type              = models.ForeignKey(GroupTypeList, on_delete = models.CASCADE, blank=True, null=True)
    admission_date          = models.DateField(auto_now_add=True)
    admission_year          = models.IntegerField(default= datetime.now().year)
    father_name             = models.CharField(max_length=40, blank=True)
    father_photo            = models.ImageField(upload_to='father_photo',blank=True)
    father_bangla_name      = models.CharField(max_length=40, blank=True)
    father_occupation       = models.CharField(max_length=40, blank=True)
    mother_name             = models.CharField(max_length=40, blank=True)
    mother_photo            = models.ImageField(upload_to='mother_photo',blank=True)
    mother_bangla_name      = models.CharField(max_length=40, blank=True)
    mother_occupation       = models.CharField(max_length=40, blank=True)
    guardian_name           = models.CharField(max_length=40, blank=True)
    guardian_relation       = models.CharField(max_length=40, blank=True)
    father_mobile           = models.CharField(max_length=15, blank=True)
    mother_mobile           = models.CharField(max_length=15, blank=True)
    guardian_mobile         = models.CharField(max_length=15, blank=True)
    guardian_monthly_income = models.CharField(max_length=15, blank=True)
    guardian_photo          = models.ImageField(upload_to='guardian_photo',blank=True)
    present_address         = models.TextField(max_length=200, blank=True)
    # address_in_bangla       = models.TextField(max_length=200, blank=True)
    parmanent_address       = models.TextField(max_length=200, blank=True)
    previous_school_name    = models.TextField(max_length=100, blank=True)
    previous_school_address = models.TextField(max_length=200, blank=True)
    tc_no                   = models.CharField(max_length=50,null=True, blank=True)
    tc_date                 = models.DateField(auto_now_add=False, null=True, blank=True)
    new_student             = models.BooleanField(default=1)
    student_types = (
        ('1', 'General student'),
        ('2', 'Full fee scholarship'),
        ('3', 'Half fee scholarship'),
        ('4', 'Old student'),
    )
    student_type            = models.CharField(max_length=1, choices=student_types, blank=True)   
    insert_date             = models.DateTimeField(auto_now_add=True)
    last_update             = models.DateTimeField(auto_now=True)
    insert_by               = models.IntegerField(default=0)
    update_by               = models.IntegerField(default=0) 
    status                  = models.BooleanField(default=1)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Student Information"

    def __str__(self):
        return "{} {}".format(self.st_first_name,self.st_last_name)

    def url(self):
        return os.path.join('/static/school/images/student_img/', os.path.basename(str(self.student_img)))

    def photo(self):
        return mark_safe('<img src = "{}" width="60"/>'.format(self.url()))




class EmployeeList(models.Model):
    employee_id             = models.IntegerField(unique = True)
    employee_name           = models.CharField(max_length=40)
    short_name              = models.CharField(max_length=7, blank=True)
    father_name             = models.CharField(max_length=40, blank=True)
    mother_name             = models.CharField(max_length=40, blank=True)
    emp_img                 = models.ImageField(upload_to='emp_img', blank=True)
    emp_password            = models.CharField(max_length=100, blank=True)
    qualification           = models.CharField(max_length=70, blank=True)
    blood_group_type = (
        ('1', 'N/A'),
        ('2', 'A+'),
        ('3', 'A-'),
        ('4', 'B+'),
        ('5', 'B-'),
        ('6', 'AB+'),
        ('7', 'AB-'),
        ('8', 'O+'),
        ('9', 'O-'),
    )
    blood_group             = models.CharField(max_length=2, choices=blood_group_type,blank=True)
    religion_types        = (
        ('1',  'Islam'),
        ('2',  'Christianity'),
        ('3',  'Hinduism'),
        ('4',  'Buddhism'),
        ('5',  'Chinese traditional religion'),
        ('6',  'African traditional religions'),
    )
    emp_religion            = models.CharField(max_length=1, choices = religion_types)
    genders_types           = (
        ('1',  'Male'),
        ('2',  'Female'),
        ('3',  'Others'),
    )
    emp_gender              = models.CharField(max_length=1, choices = genders_types)
    desig_types           = (
        ('1',  'Principal'),
        ('2',  'Employee'),
        ('3',  'IT Officer'),
        ('4',  'Vice Principal'),
    )
    desig_name              = models.CharField(max_length=1, choices = desig_types)
    dpt_name                = models.ForeignKey(Department, on_delete=models.CASCADE)
    fitness_details         = models.TextField(blank=True)
    medical_certificate     = models.ImageField(upload_to='medical_certificate', blank=True)    
    emp_mobile              = models.CharField(max_length=15, blank=True)
    email_address           = models.EmailField(max_length=80, blank = True)
    join_date               = models.DateField(auto_now_add=False)
    resign_date             = models.DateField(auto_now_add=True)
    date_of_birth           = models.DateField(auto_now_add=False)
    national_id             = models.CharField(max_length=40, blank=True)
    basic_salary            = models.FloatField(default=0)
    starting_salary         = models.FloatField(default=0, blank=True)
    present_address         = models.TextField(blank=True)
    permanent_address       = models.TextField(blank=True)
    added_by                = models.CharField(max_length=80, blank=True)
    is_teacher              = models.BooleanField(default=0)
    insert_date             = models.DateTimeField(auto_now_add=True)
    last_update             = models.DateTimeField(auto_now=True)
    insert_by               = models.IntegerField(default=0)
    update_by               = models.IntegerField(default=0)    
    status                  = models.BooleanField(default=1)

    def __str__(self):
        return self.employee_name

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

class TeacherList(models.Model):
    teacher_name            = models.ForeignKey(EmployeeList, on_delete=models.CASCADE)
    class_name              = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    shift_name              = models.ForeignKey(Shift, on_delete=models.CASCADE)
    section_name            = models.ForeignKey(Section, on_delete=models.CASCADE)
    running_year            = models.ForeignKey(Years, on_delete=models.CASCADE)
    Version_type = (
        ('1', 'Bangla Medium'),
        ('2', 'English Version'),
    )
    Version                 = models.CharField(max_length=1, choices=Version_type, blank=True)   
    group_type              = models.ForeignKey(GroupTypeList, on_delete = models.CASCADE, blank=True, null=True)
    status                  = models.BooleanField(default=1)

    def __str__(self):
        return str(self.teacher_name)

    class Meta:
        verbose_name = "Teacher List"
        verbose_name_plural = "Teacher List"



class MarkDistribution(models.Model):
    class_name              = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    class_subject           = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark_types = (
        ('1', 'Written'),
        ('2', 'MCQ')
    )
    mark_type               = models.CharField(max_length=1, choices = mark_types)   
    total_mark              = models.IntegerField(default=0)
    pass_mark               = models.IntegerField(default=0)
    status                  = models.BooleanField(default=1)

    def __str__(self):
        return str(self.mark_type)

    class Meta:
        verbose_name = "Mark Distribution"
        verbose_name_plural = "Mark Distributions"



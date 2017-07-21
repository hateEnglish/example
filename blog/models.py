from django.db import models


# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField(name='stu_id', primary_key=True, null=False, auto_created=True)
    stu_name = models.CharField(name='stu_name', max_length=20, null=False)
    stu_old_name = models.CharField(name='stu_old_name',max_length=20,default=None)
    stu_sex = models.CharField(name='stu_sex',max_length=4,null=False,default='男')
    stu_birthday = models.CharField(name='stu_birthday',max_length=20,default=None)
    stu_nation = models.CharField(name='stu_nation',max_length=30,default=None)
    stu_native_place = models.CharField(name='stu_native_place',max_length=100,default=None)
    stu_politics_statuss = models.CharField(name='stu_politics_status',max_length=20,default='未知')
    stu_academy = models.CharField(name='stu_academy',max_length=30,null=True,default=None)
    stu_major = models.CharField(name='stu_major',max_length=30,default=None)
    stu_major_field = models.CharField(name='stu_major_field',max_length=30,default=None)
    stu_grade = models.CharField(name='stu_grade',max_length=30,default=None)
    stu_start_sch_time = models.CharField(name='stu_start_sch_time',max_length=20,default=None)
    stu_class = models.CharField(name='stu_class',max_length=20,default=None)
    stu_training_level = models.CharField(name='stu_training_level',max_length=10,default=None)
    stu_length_of_school = models.CharField(name='stu_length_of_school',max_length=10,default=None)
    stu_lengthest_of_schooling = models.CharField(name='stu_lengthest_of_schooling',max_length=10,default=None)
    stu_exam_numb = models.CharField(name='stu_exam_numb',max_length=30,default=None)
    stu_study_state = models.CharField(name='stu_study_state',max_length=20,default='在校')
    stu_image = models.CharField(name='stu_image',max_length=100,default=None)

    class Meta:
        db_table = 'stu_info'


class Teacher(models.Model):
    id = models.IntegerField(name="tea_id", primary_key=True, auto_created=True)
    name = models.CharField(name='tea_name', max_length=50)


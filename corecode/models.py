from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
import uuid 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class SiteConfig(models.Model):
    """ Site Configurations """
    key = models.SlugField()
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key


class AcademicSession(models.Model):
    """ Academic Session """
    name = models.CharField(max_length=200, unique=True)
    current = models.BooleanField()

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class AcademicTerm(models.Model):
    """ Academic Term """
    name = models.CharField(max_length=20, unique=True)
    current = models.BooleanField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Subject(models.Model):
    """ Subject """
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ['name']

    def __str__(self):
        return self.name


class Educations(models.Model):
    Deparment = [
        ('default', 'Choose Option'),
        ('school', 'School Name'),
        ('collage', 'Collage Name'),
        ('tution', 'Tution Name'),
        ('course', 'Course Name')
    ]
    department = models.CharField(max_length=80, choices=Deparment, default='default')
    logo = models.ImageField(upload_to='school/logo', default='default.jpg')
    bg_image = models.ImageField(upload_to='school/bg', default='default.jpg')
    name = models.CharField(max_length=200, unique=True)
    discription = models.TextField()

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "School Name"
        ordering = ['name']

    def __str__(self):
        return self.name


class Video(models.Model):
    video_id = models.UUIDField(unique=True, default = uuid.uuid4, editable = False)
    choice_school = models.ForeignKey(
        Educations, on_delete=models.SET_NULL, null=True)
    choice_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, null=True)
    choice_subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True)
    video_link = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=300)
    discription = RichTextUploadingField(config_name='awesome_ckeditor', external_plugin_resources=[('youtube', 
                                            '/static/ckeditor/ckeditor/plugins/youtube/youtube/',
                                             'plugin.js',)],)

    class Meta:
        verbose_name = "subjectvideo"
        verbose_name_plural = "Subject video"
        ordering = ['choice_school']

    def __str__(self):
        return self.name
    
   


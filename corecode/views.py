from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
import os
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import SiteConfig, AcademicSession, AcademicTerm, StudentClass, Subject, Educations, Video
from .forms import  SiteConfigForm, AcademicTermForm, AcademicSessionForm, StudentClassForm, SubjectForm, CurrentSessionForm



class SchoolCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Educations
    fields = '__all__'
    success_message = "Record successfully added."
    success_url = reverse_lazy('home')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

@login_required
class SchoolUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Educations
    fields = '__all__'
    success_message = "Record successfully updated."
    success_url = reverse_lazy('home')


class VideoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Video
    fields = '__all__'
    success_message = "Video successfully added."
    success_url = reverse_lazy('home')


class VideoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Video
    fields = '__all__'
    success_message = "video successfully updated."
    success_url = reverse_lazy('home')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def index_view(request):
  home_video=Video.objects.all()
  scount = Educations.objects.filter(department="school").count()
  print(scount)
  ccount = Educations.objects.filter(department="collage").count()
  print(ccount)
  tcount = Educations.objects.filter(department="tution").count()
  print(tcount)
  crcount = Educations.objects.filter(department="course").count()
  print(crcount)
  con = {'video':home_video, 'scount':scount, 'ccount':ccount, 'tcount':tcount, 'crcount':crcount}
  return render(request, 'corecode/index.html', con)

@login_required
def video_view(request, videoid):
  video= Video.objects.all().filter(video_id=videoid)
  video_all= Video.objects.all()
  print(video_all)
  context= {'videodetail': video, 'videoall':video_all}
  return render(request, 'corecode/videodetail.html', context)
  
  def get_absolute_url(self):
        return reverse('watch', kwargs={'video_id': self.video_id})


def school_view(request):
  school_name= Educations.objects.all().filter(department='school')
  context= {'school':school_name}
  return render(request, 'corecode/school.html', context)


def school_detail(request, school):
    school_name = Educations.objects.filter(pk=school)
    school_video= Video.objects.filter(choice_school=school)
    print(school_name)
    context = {'school': school_name, 'video': school_video}
    return render(request, 'corecode/schooldetail.html', context)


def course_view(request):
  course_name= Educations.objects.all().filter(department='course')
  context= {'course':course_name}
  return render(request, 'corecode/course.html', context)

def course_detail(request, course):
    course_name = Educations.objects.filter(pk=course)
    course_video= Video.objects.filter(choice_school=course)
    context = {'course': course_name, 'video': course_video}
    return render(request, 'corecode/course_detail.html', context)


def collage_view(request):
  collage_name = Educations.objects.all().filter(department='collage')
  context = {'collage': collage_name}
  return render(request, 'corecode/collage.html', context)


def collage_detail(request, collage):
    school_name = Educations.objects.filter(pk=collage)
    school_video= Video.objects.filter(choice_school=collage)
    school_video.filter()
    context = {'collage': school_name, 'video': school_video}
    return render(request, 'corecode/collagedetail.html', context)


def coaching_view(request):
  tution_name = Educations.objects.all().filter(department='tution')
  context = {'tution': tution_name}
  return render(request, 'corecode/coaching.html', context)


def tution_detail(request, tution):
    school_name = Educations.objects.filter(pk=tution)
    school_video= Video.objects.filter(choice_school=tution)
    school_video.filter()
    context = {'tution': school_name, 'video': school_video}
    return render(request, 'corecode/coachingdetail.html', context)

@login_required
def siteconfig_view(request):
  """ Site Config View """
  if request.method == 'POST':
    form = SiteConfigForm(request.POST)
    print(form.errors)
    if form.is_valid():
      form.save()
      messages.success(request, 'Configurations successfully updated')
      return HttpResponseRedirect('site-config')
  else:
    form = SiteConfigForm(queryset=SiteConfig.objects.all())

  context = {"formset": form, "title": "Configuration"}
  return render(request, 'corecode/siteconfig.html', context)

@login_required
def academic_terms_view(request):
  """ Academic Terms View """
  if request.method == 'POST':
    form = AcademicTermForm(request.POST)
    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Terms successfully saved')
      return HttpResponseRedirect('terms')
  else:
    form = AcademicTermForm(queryset=AcademicTerm.objects.all())

  context = {"formset": form, "title": "Terms"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def academic_sessions_view(request, PermissionRequiredMixin):
  """ Academic Sessions View """
  if request.method == 'POST':
    form = AcademicSessionForm(request.POST)
    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Terms successfully saved')
      return HttpResponseRedirect('sessions')
  else:
    form = AcademicSessionForm(queryset=AcademicSession.objects.all())

  context = {"formset": form, "title": "Sessions"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def student_classes_view(request):
  """ Classes View """
  if request.method == 'POST':
    form = StudentClassForm(request.POST)
    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Terms successfully saved')
      return HttpResponseRedirect('classes')

  else:
    form = StudentClassForm(queryset=StudentClass.objects.all())

  context = {"formset": form, "title": "Classes"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def subject_view(request):
  """ Subject View """
  if request.method == 'POST':
    form = SubjectForm(request.POST)

    if form.is_valid() and form.has_changed():
      form.save()
      messages.success(request, 'Terms successfully saved')
      return HttpResponseRedirect('subjects')

  else:
    form = SubjectForm(queryset=Subject.objects.all())

  context = {"formset": form, "title": "Subjects"}
  return render(request, 'corecode/mgt_form.html', context)

@login_required
def current_session_view(request):
  """ Current SEssion and Term """
  if request.method == 'POST':
    form = CurrentSessionForm(request.POST)
    if form.is_valid():
      session = form.cleaned_data['current_session']
      term = form.cleaned_data['current_term']
      AcademicSession.objects.filter(name=session).update(current=True)
      AcademicSession.objects.exclude(name=session).update(current=False)
      AcademicTerm.objects.filter(name=term).update(current=True)
      AcademicTerm.objects.exclude(name=term).update(current=False)

  else:
    form = CurrentSessionForm(initial={
      "current_session": AcademicSession.objects.get(current=True),
      "current_term": AcademicTerm.objects.get(current=True)
    })


  return render(request, 'corecode/current_session.html', {"form":form})

@login_required
def developer(request):
  """ Developer """
  return render(request, 'corecode/developer.html')




from django.urls import path

from corecode.views import * 

urlpatterns = [
  path('upload=<int:pk>/', VideoUpdateView, name='video-update'),
  path('upload/', VideoCreateView.as_view(), name='upload'),
  path('update/<slug:videoid>/', SchoolUpdateView, name='update'),
  path('create/', SchoolCreateView.as_view(), name='create'),
  path('', index_view, name='home'),
  path('watch=<slug:videoid>/', video_view, name='watch'),
  path('school/<int:school>', school_detail, name='school_detail'),
  path('school/', school_view, name='school'),
  path('courses/<int:course>', course_detail, name='course_detail'),
  path('courses/', course_view, name='course'),
  path('collage/<int:collage>', collage_detail, name='collage_detail'),
  path('collage/', collage_view, name='collage'),
  path('coaching/<int:tution>', tution_detail, name='tution_detail'),
  path('coaching/', coaching_view, name='tution'),
  path('site-config', siteconfig_view, name='configs'),
  path('terms', academic_terms_view, name='terms'),
  path('sessions', academic_sessions_view, name='sessions'),
  path('classes', student_classes_view, name='classes'),
  path('subjects', subject_view, name='subjects'),
  path('current-session', current_session_view, name='current-session'),
  path('developer', developer, name='developer'),
]

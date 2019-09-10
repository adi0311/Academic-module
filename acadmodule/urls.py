from django.conf.urls import url,include
from django.contrib import admin
from acadmodule.views import add_course,add_btech_curriculum,add_batch_semester,add_curriculum_course

urlpatterns = [
    url(r'^add_course/', add_course,name="add_courses"),
    url(r'^add_btech_curriculum/', add_btech_curriculum,name="add_btech_curriculums"),
    url(r'^add_batch_semester/', add_batch_semester,name="add_batch_semester"),
    url(r'^add_curriculum_course/', add_curriculum_course,name="add_curriculum_courses"),
]

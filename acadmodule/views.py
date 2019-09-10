from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from acadmodule.models import BatchSemester,Course,CurriculumCourse,CurriculumInstructor,BtechCurriculum
# Create your views here.

# class Homepage(TemplateView):
#     template_name = 'home.html'

def add_course(request):
    if request.method =='POST':
        course_name = request.POST['course_name']
        course_detail = request.POST['course_detail']

        courses = Course.objects.create(course_name=course_name,course_details=course_detail)
    return render(request,'add_course.html')

def get_course_list(request):
    obj = Course.objects.all().filter()
    print(obj)
    context ={'course_list':obj}
    return context


def add_btech_curriculum(request):
    if request.method =='POST':
        programme = request.POST['programme']
        batch =request.POST['batch']
        professional_core_credit =request.POST['prof_core_credit']
        professional_elective_credit = request.POST['prof_elective_credit']
        professional_project_credit = request.POST['prof_project_credit']
        professional_lab_credit = request.POST['prof_lab_credit']
        Core_engineering_science_credit = request.POST['core_engineering_science_credit']
        Core_natural_science_credit = request.POST['core_natural_science_credit']
        Core_humanities_credit = request.POST['core_humanities_credit']
        Core_design_credit = request.POST['core_design_credit']
        Core_manufacturing_credit = request.POST['core_manufacturing_credit']
        Core_management_science_credit = request.POST['core_management_science_credit']
        pbi = request.POST['pbi']
        pr =request.POST['pr']

        print(programme,batch,pbi,pr)
        btech_curr = BtechCurriculum.objects.create(
        programme=programme,
        batch=batch,
        professional_core_credit=professional_core_credit,
        professional_elective_credit=professional_elective_credit,
        professional_project_credit=professional_project_credit,
        professional_lab_credit=professional_lab_credit,
        Core_engineering_science_credit=Core_engineering_science_credit,
        Core_natural_science_credit=Core_natural_science_credit,
        Core_humanities_credit=Core_humanities_credit,
        Core_design_credit=Core_design_credit,
        Core_manufacturing_credit=Core_manufacturing_credit,
        Core_management_science_credit=Core_management_science_credit,
        pbi=pbi,
        pr=pr)
        print(btech_curr)
    return render(request,'add_btech_curriculum.html')


def add_batch_semester(request):
    if request.method=='POST':
        programme = request.POST['programme']
        batch = request.POST['batch']
        sem = request.POST['semester']
        total_courses = request.POST['total_number_of_courses']
        prof_core_courses = request.POST['professional_core_courses']
        prof_elective_courses = request.POST['professional_elective_courses']
        prof_project_courses = request.POST['professional_project_courses']
        prof_lab_courses = request.POST['professional_lab_courses']
        es_courses = request.POST['escourses']
        ns_courses = request.POST['nscourses']
        hs_courses = request.POST['hscourses']
        ds_courses = request.POST['dscourses']
        mn_courses = request.POST['mncourses']
        ms_courses = request.POST['mscourses']
        pbi = request.POST['pbi']

        print(es_courses,mn_courses)
        batch_sem = BatchSemester.objects.create(
        programme=programme,
        batch=batch,
        semester=sem,
        total_number_of_courses=total_courses,
        professional_core_courses=prof_core_courses,
        professional_elective_courses=prof_elective_courses,
        professional_project_courses=prof_project_courses,
        professional_lab_courses=prof_lab_courses,
        Core_engineering_science_courses=es_courses,
        Core_natural_science_courses=ns_courses,
        Core_humanities_courses=hs_courses,
        Core_design_courses=ds_courses,
        Core_manufacturing_courses=mn_courses,
        Core_management_science_courses=ms_courses,
        pbi=pbi)
        print(batch_sem)
        find_sem = 'sem'+ str(sem)
        print(find_sem)
        if int(sem)==1 :
            obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem1=batch_sem)
        elif int(sem)==2:
            obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem2=batch_sem)
        elif int(sem)==3:
            obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem3=batch_sem)
        elif int(sem)==4:
            obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem4=batch_sem)
        elif int(sem)==5:
            obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem5=batch_sem)
        elif int(sem)==6:
            obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem6=batch_sem)
        elif int(sem)==7:
            obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem7=batch_sem)
        elif int(sem)==8:
            obj = BtechCurriculum.objects.all().filter(batch=batch).update(sem8=batch_sem)
        # obj.save()

    return render(request,"add_batch_semester.html")

# def get_course_list(request):
#
#     print(context)
#     return render(request,'add_curriculum_course.html',context)

def add_curriculum_course(request):
    if request.method=='POST':
        sem = request.POST['semester']
        course = request.POST['course']
        course_id = request.POST['course_id']
        course_type = request.POST['course_type']
        course_credits=request.POST['course_credits']
        course_lecture = request.POST['course_lecture']
        course_tutorials = request.POST['course_tutorials']
        course_practical = request.POST['course_practical']
        course_discussion= request.POST['course_discussion']
        obj = BatchSemester.objects.all().filter(semester=sem).filter(batch=2018).first()
        print(obj)
        CurriculumCourse.objects.create(
        semester=obj,
        course_id=course_id,
        course_type=course_type,
        course_credits=course_credits,
        course_lecture=course_lecture,
        course_tutorial=course_tutorials,
        course_practical=course_practical,
        course_discussion=course_discussion
        )


        # obj2 = Course.objects.filter(course_name = course)
        # CurriculumCourse.objects.all().filter(semester=sem).order_by('batch').update(curr_course=obj2)
        # obj = BatchSemester.objects.all().filter(semester=sem).order_by('batch')
        # obj1 = obj.first()
        # # print(obj)
        # CurriculumCourse.objects.all().filter(semester=sem).order_by('batch').update(semester=obj1)
        # # courses = Course.objects.all()
        # context = get_course_list(request)
    return render(request,'add_curriculum_course.html',get_course_list(request))

def view_curriculum(request):
    if request.method == 'POST':
        batch = request.POST['batch']
        semester = request.POST['semester']
        programme = request.POST['programme']
        print(programme)
        obj = BtechCurriculum.objects.filter(batch=batch).first()
        if semester == "all":
            obj1 = obj.sem1
            obj2 = obj.sem2
            obj3 = obj.sem3
            obj4 = obj.sem4
            obj5 = obj.sem5
            obj6 = obj.sem6
            obj7 = obj.sem7
            obj8 = obj.sem8
            sem1 = CurriculumCourse.objects.all().filter(semester=obj1)
            sem2 = CurriculumCourse.objects.all().filter(semester=obj2)
            sem3 = CurriculumCourse.objects.all().filter(semester=obj3)
            sem4 = CurriculumCourse.objects.all().filter(semester=obj4)
            sem5 = CurriculumCourse.objects.all().filter(semester=obj5)
            sem6 = CurriculumCourse.objects.all().filter(semester=obj6)
            sem7 = CurriculumCourse.objects.all().filter(semester=obj7)
            sem8 = CurriculumCourse.objects.all().filter(semester=obj8)
            context = {'semester1':sem1,
            'semester2':sem2,
            'semester3':sem3,
            'semester4':sem4,
            'semester5':sem5,
            'semester6':sem6,
            'semester7':sem7,
            'semester8':sem8,
            'tab':9}
        elif semester == 1 :
            obj1 = obj.sem1
            sem1 = CurriculumCourse.objects.all().filter(semester=obj1)
            context = {'semester1':sem1,'tab':1}
        elif semester == 2 :
            obj2 = obj.sem2
            sem2 = CurriculumCourse.objects.all().filter(semester=obj2)
            context = {'semester2':sem2,'tab':2}
        elif semester == 3 :
            obj3 = obj.sem3
            sem3 = CurriculumCourse.objects.all().filter(semester=obj3)
            context = {'semester3':sem3,'tab':3}
        elif semester == 4 :
            obj4 = obj.sem4
            sem4 = CurriculumCourse.objects.all().filter(semester=obj4)
            context = {'semester4':sem4,'tab':4}
        elif semester == 5 :
            obj5 = obj.sem5
            sem5 = CurriculumCourse.objects.all().filter(semester=obj5)
            context = {'semester5':sem5,'tab':5}
        elif semester == 6 :
            obj6 = obj.sem6
            sem6 = CurriculumCourse.objects.all().filter(semester=obj6)
            context = {'semester6':sem6,'tab':6}
        elif semester == 7 :
            obj7 = obj.sem7
            sem7 = CurriculumCourse.objects.all().filter(semester=obj7)
            context = {'semester7':sem7,'tab':7}
        elif semester == 8 :
            obj8 = obj.sem8
            sem8 = CurriculumCourse.objects.all().filter(semester=obj8)
            context = {'semester8':sem8,'tab':8}

    return render(request,'get_curriculum.html',context)













# sdgv

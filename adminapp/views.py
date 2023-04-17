# from django.shortcuts import redirect, render

# from adminapp.forms import CourseForm, CourseTypeForm, LanguageForm, PriceForm
# from userapp.models import coursetype

# # Create your views here.
# def Home(request):
#     return render(request,"adminhome.html")
# def AddCourse(request):
#     courseform = CourseForm()
#     languageform = LanguageForm()
#     priceform = PriceForm()
#     coursetypeform = CourseTypeForm()
#     if request.method == 'POST':
#         courseform = CourseForm(request.POST, request.FILES)
#         languageform = LanguageForm(request.POST)
#         priceform = PriceForm(request.POST)
#         coursetypeform = CourseTypeForm(request.POST)
#         if courseform.is_valid() and languageform.is_valid() and priceform.is_valid() and coursetypeform.is_valid():
#             # Save the language instance
#             language_instance = languageform.save()

#             # Save the course type instance
#             coursetype_instance = coursetypeform.save()

#             # Save the course instance and set the language and course type foreign keys
#             course_instance = courseform.save(commit=False)
#             course_instance.language = language_instance
#             course_instance.coursetype = coursetype_instance
#             course_instance.save()

#             # Save the price instance and set the course foreign key
#             price_instance = priceform.save(commit=False)
#             price_instance.course = course_instance
#             price_instance.save()

#             # Redirect to the addcourse page
#             return redirect('addcourse')
#     return render(request, "addcourse.html", {'courseform': courseform, 'languageform': languageform, 'priceform': priceform, 'coursetypeform': coursetypeform})

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from adminapp.forms import CourseForm, CourseTypeForm, LanguageForm, PriceForm
from userapp.models import course, coursetype, language
from django.contrib.auth.decorators import login_required


# Create your views here.
def AdminLogin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password) 
        if user is not None:
            login(request,user)
            return render(request,"adminhome.html")
    return render(request,"adminlogin.html")

@login_required(login_url='alogin')
def Home(request):
    return render(request,"adminhome.html")

def AddCourse(request):
    courseform = CourseForm()
    languageform = LanguageForm()
    priceform = PriceForm()
    coursetypeform = CourseTypeForm()

    if request.method == 'POST':
        courseform = CourseForm(request.POST, request.FILES)
        languageform = LanguageForm(request.POST)
        priceform = PriceForm(request.POST)
        coursetypeform = CourseTypeForm(request.POST)

        if courseform.is_valid() and languageform.is_valid() and priceform.is_valid() and coursetypeform.is_valid():
            # Save the language instance
            language_instance, _ = language.objects.get_or_create(language=languageform.cleaned_data['language'])

            # Save the course type instance
            coursetype_instance, _ = coursetype.objects.get_or_create(type=coursetypeform.cleaned_data['type'])

            # Save the course instance and set the language and course type foreign keys
            course_instance = courseform.save(commit=False)
            course_instance.language = language_instance
            course_instance.coursetype = coursetype_instance
            course_instance.save()

            # Save the price instance and set the course foreign key
            price_instance = priceform.save(commit=False)
            price_instance.course = course_instance
            price_instance.save()

            # Redirect to the addcourse page
            return redirect('addcourse')

    return render(request, "addcourse.html", {'courseform': courseform, 'languageform': languageform, 'priceform': priceform, 'coursetypeform': coursetypeform})

def AddLanguage(request):
    if request.method == 'POST':
        lang = language()
        lang.language = request.POST.get('language')
        lang.save()
        return render(request, 'addlanguage.html')
    else:
        return render(request, 'addlanguage.html')
    
def DeleteCourse(request):
    data=course.objects.all()
    return render(request,"delete.html",{'data':data})

def DeleteRow(request,id):
    data=course.objects.all()
    row = course.objects.get(id=id)
    row.delete()
    return render(request,"delete.html",{'data':data})

def EditRow(request, id):
    data = course.objects.get(id=id)
    types = coursetype.objects.all()
    
    if request.method == 'POST':
        data.name = request.POST['name']
        data.duration = request.POST['duration']
        data.description = request.POST['description']
        data.image = request.FILES['image']
        # data.language = request.POST['language']
        # data.type = request.POST['type']
        # data.type = coursetype.objects.get(id=request.POST['type'])
        data.save()
        return redirect("delete")
    
    return render(request, "edit.html", {'data': data, 'types': types})

# def AdminLog(request):
#     return render(request,"adminlogin.html")
def AdminLogout(request):
    logout(request)
    return redirect("alogin")
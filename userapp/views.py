from django.shortcuts import render, redirect
from userapp.forms import CreateUserForm, RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from userapp.models import cart, price, registration, course
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def home(request):
    data=price.objects.all()
    # data=course.objects.all()
    return render(request,"home.html",{'data':data})

def UserSignup(request):
    if request.method=="POST":
        userform=CreateUserForm(request.POST)
        regform=RegistrationForm(request.POST,request.FILES)
        if userform.is_valid() and regform.is_valid():
            user =userform.save()
            reg=regform.save(commit=False)
            reg.user=user
            reg.save()
            return redirect('/login')
    else:
        userform=CreateUserForm()
        regform=RegistrationForm()
    return render(request,"userhome.html",{'userform':userform,'regform':regform})

def UserLogin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password) 
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
        else:
            messages.error(request, "Incorrect Username or password")
            return redirect('/login')
    return render(request,"userlogin.html")

@login_required(login_url='/login')
def UserDash(request):
    # stdetail=registration.objects.get(user=request.user)
    data=price.objects.all()
    return render(request,"userdash.html",{'data':data})

def UserLogout(request):
    logout(request)
    return redirect('/')

def Courses(request):
    courses=course.objects.all()
    return render(request,"course.html",{'courses':courses})

def Cart(request):
    return render(request,"cart.html")

def Passcomplete(request):
    return redirect('/login')

def search_data(request):
        query = request.GET.get('searchbox')
        if query:
            search = course.objects.filter(Q(name__icontains=query))

        else:
            search = course.objects.none()
        return render(request, "course.html",{'search':search})

def CourseDetails(request):
    return render(request,"coursedetails.html")

def ViewCart(request):
     if request.user.is_authenticated:
        p_data=price.objects.all()
        c_data = cart.objects.filter(user=request.user)
        return render(request, "cart.html", {'data': c_data,'p_data':p_data})

def AddCart(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Login to continue.")
        return redirect("/")
    p_data=price.objects.all()
    course_data = course.objects.all()
    c_data = cart.objects.filter(user=request.user)
    data = price.objects.get(id=id)
    course_id = data.course.id

    for item in c_data:
        if item.course.id == course_id:
            messages.error(request, "Already added to cart")
            break
    else:
        user_cart = cart(course_id=course_id, user=request.user)
        user_cart.save()
        return render(request, "cart.html", {'data': c_data,'p_data':p_data})

    return render(request, "cart.html", {'data': c_data,'p_data':p_data})

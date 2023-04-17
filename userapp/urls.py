from django.urls import path
from userapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.UserSignup,name="signup"),
    path('login',views.UserLogin,name="login"),
    path('dashboard',views.UserDash,name='dashboard'),
    path('logout',views.UserLogout,name="logout"),
    path('courses',views.Courses,name="courses"),
    path('cart',views.Cart,name="cart"),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="userlogin.html"), name="password_reset_complete"),
    path('userapp/reset/done/',views.Passcomplete),
    path('course',views.search_data,name="course"),
    path('coursedetails',views.CourseDetails,name="coursedetails"),
    path('cart/<int:id>',views.AddCart,name="cart"),
    path('cartview',views.ViewCart,name="cartview"),
]

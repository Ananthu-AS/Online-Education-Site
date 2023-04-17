from adminapp import views
from django.urls import path


urlpatterns = [
    path('home',views.Home,name="adminhome"),
    path('alogin',views.AdminLogin,name="alogin"),
    path('addcourse',views.AddCourse,name='addcourse'),
    path('addlanguage',views.AddLanguage,name="addlanguage"),
    path('delete',views.DeleteCourse,name="delete"),
    path('deleteRow/<int:id>',views.DeleteRow,name="deleteRow"),
    path('editRow/<int:id>',views.EditRow,name="editRow"),
    path('logout',views.AdminLogout,name="alogout")
]

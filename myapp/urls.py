from django.urls import path
from myapp import views


urlpatterns = [
    path('razorpay/<int:id>', views.app_create, name='app_create'),
    path('charge/<int:id>', views.app_charge, name='app_charge'),
]

from django.urls import path
from . import views
from .views import SignUpView,Dashboard,About,Contact,LoginView,logoutview,edit_user

# app_name = "core"

urlpatterns = [
     path('', views.my_view, name='my_view'),
     path("signup/",SignUpView.as_view(),name = 'signup'),
     path("dashboard",Dashboard.as_view(),name = 'dashboard'),
     path("about", About.as_view(),name = 'about'),
     path("services", views.services,name = 'services'),
     path("contact", Contact.as_view(), name = 'contact'),
     path("create_order",views.create_order,name = 'create_order'),
     path('login/', views.login_page, name='login'),
     path('edit_user/', views.edit_user, name='edit_user'),
     path("order/delete/<int:id>",views.delete_order , name = 'delete_order'),
     path('logout/', logoutview , name='logout'),

]

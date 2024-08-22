from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from .forms import SignUpForm,OrderForm
from django.contrib.auth import authenticate,login,logout
from .models import User,Order,RiderProfile
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from . import forms
from django.contrib import messages
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required



def logoutview(request):
    logout(request)
    return redirect("login")



def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('dashboard'))

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('dashboard'))
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', context={'form': form})



@login_required
def edit_user(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'dashboard.html', {'user_form': form})



def my_view(request):
    return render(request, "index.html")

def services(request):
    return render(request, "user/services.html")

class About(TemplateView):
     template_name = 'user/about.html'


class Contact(TemplateView):
    template_name = "user/contact.html"



class SignUpView(TemplateView):
    template_name = 'user/signup.html'
    
    def get(self, request):

        form = SignUpForm()
        del form.fields["usable_password"]
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data.get("email",None),
                first_name = form.cleaned_data.get("first_name",None),
                last_name = form.cleaned_data.get("last_name",None),
                password = form.cleaned_data.get("password1",None)
        
            )
            login(request,user)

            return redirect("login")
        return render(request,self.template_name,{'form':form})


class Dashboard(LoginRequiredMixin,TemplateView):
    login_url = '/signup'
    template_name = 'user/dashboard.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        orders = Order.objects.filter(customer =self.request.user).filter(completed = False)
        history = Order.objects.filter(customer =self.request.user).filter(completed = True)
        user_form = UserEditForm(instance=self.request.user)
        
        form = OrderForm()
        context['form'] = form 
        context['orders'] = orders
        context['history'] = history
        context['user_form'] = user_form

        return context
    
    

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
           item_description = form.cleaned_data['item_description']
           senders_phone_number = form.cleaned_data['senders_phonenumber']
           pickup_location = form.cleaned_data['pickup_location']
           receivers_phone_number = form.cleaned_data['receivers_phonenumber']
           delivery_location = form.cleaned_data['delivery_location']

           rider = RiderProfile.objects.order_by("?").all()[0]
           order = Order.objects.create(pickup_location = pickup_location, senders_phone_number = senders_phone_number , item_description = item_description, delivery_location = delivery_location,
           receivers_phone_number = receivers_phone_number,customer = request.user,driver = rider)

           return redirect("dashboard")
    else:
        form = OrderForm()
        
    return render(request, 'create_order.html', {'form': form})



def delete_order(request,id = None):
    obj  = get_object_or_404(Order,id = id)
    obj.delete()
    return redirect(
        reverse_lazy("dashboard")
    )
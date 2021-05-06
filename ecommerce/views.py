from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .forms import ContactForm, RegistrationForm, LoginForm
from django.views.generic import ListView, DetailView
from products.models import Product
from django.contrib.auth import login, authenticate, get_user_model


def about_page(request):
    context = {
        'title': 'About us'
    }
    return render(request, "about.html", context )


class ProductList(ListView):
    model = Product
    template_name='products.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)


class ProductDetail(DetailView):
    model = Product
    template_name='detail.html'


def post_detail(request, pk):
      return render(request, 'detail.html', {
    'post': get_object_or_404(Post, pk=id)
  })



User = get_user_model()

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
        "cleaned_email": LoginForm.clean_email,
        "title":"Home page"
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(form.cleaned_data)
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect("/login")
            
    return render(request, "auth/login.html", context)
 
def reg_page(request):
    form = RegistrationForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        form.save()
    return render(request, "auth/reg.html", context)


def homepage(request):
    return render(request, "home.html")



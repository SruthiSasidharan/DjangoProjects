from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,ListView,UpdateView
from GUEST.models import Review
from GUEST.forms import ReviewCreateForm
from .models import MyUser,Library
from .forms import RegForm,LoginForm,LibraryForm

# Create your views here.
class RegistrationView(TemplateView):
    model=MyUser
    form_class=RegForm
    template_name ="register.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

class LoginView(TemplateView):
    form_class=LoginForm
    template_name = "login.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=email,password=password)
            if user:
                print("sucess")
                login(request, user)
                return redirect("home")
            else:
                form=self.form_class()
                self.context["form"] = form
                return render(request, self.template_name, self.context)

class CreateLibrary(CreateView):
    model = Library
    template_name = "addrev.html"
    form_class = LibraryForm
    success_url = reverse_lazy("list")

class ListLibrary(ListView):
    model = Library
    template_name = "listrev.html"
    context_object_name = "reviews"

class UpdateLibrary(UpdateView):
    model = Library
    template_name = "editlib.html"
    form_class = LibraryForm
    success_url = reverse_lazy("list")

class Deletelibrary(TemplateView):
    model = Library
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        lib=self.model.objects.get(id=id)
        lib.delete()
        return redirect("list")


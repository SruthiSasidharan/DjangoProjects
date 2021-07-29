from django.shortcuts import render,redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView

from GUEST.forms import ReviewCreateForm
from Guest.models import Library
from .models import Review

class ReviewCreateView(TemplateView):
    model = Review
    template_name ="rev.html"
    form_class = ReviewCreateForm
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    # def post(self, request, *args, **kwargs):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect("log")



from django.shortcuts import render, redirect
from django.views import View
from django.views import generic

class main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'main/index.html'
        return render(request, template_name)
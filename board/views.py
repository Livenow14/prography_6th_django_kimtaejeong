from django.shortcuts import render, redirect
from django.views import generic
from .models import List

#board view
class board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        #Reserved.objects.filter(client=client_id).order_by('-check_in')
        template_name = 'board/board_list.html'
        list=List.objects.all();
        return render(request, template_name,{"list":list})



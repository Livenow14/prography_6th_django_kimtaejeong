from django.shortcuts import render, redirect
from django.views import generic


#board view
class board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        #Reserved.objects.filter(client=client_id).order_by('-check_in')
        template_name = 'board/board_list.html'
        #기한 없는 일정, 마감 안된 애들

        return render(request, template_name)



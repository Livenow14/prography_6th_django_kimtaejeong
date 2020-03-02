from django.shortcuts import render, redirect
from django.views import generic
from .models import List
from .forms import Form

#board view
class board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        #Reserved.objects.filter(client=client_id).order_by('-check_in')
        template_name = 'board/board_list.html'
        list=List.objects.all();
        return render(request, template_name,{"list":list})


# when write new todo_list
# post -> when click "save"
# get -> just view a template
def check_post(request):
    template_name = 'board/board_success.html'
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            tmp = form.save(commit=False)
            tmp.save()
            message = "일정을 추가하였습니다."
            return render(request, template_name, {"message": message})

    else:
        template_name = 'board/board_insert.html'
        form = Form
        return render(request, template_name, {"form" : form})
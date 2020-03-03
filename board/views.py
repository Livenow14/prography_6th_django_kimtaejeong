from django.shortcuts import render, redirect
from django.views import generic
from .models import List
from .forms import Form

# delete view
class board_delete(generic.DeleteView):
    model = List
    success_url = '/board/'
    context_object_name = 'list'
#board view
class board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        #Reserved.objects.filter(client=client_id).order_by('-check_in')
        template_name = 'board/board_list.html'
        list=List.objects.all();
        return render(request, template_name,{"list":list})
#update view
class board_update(generic.UpdateView):
    model =List
    form_class =Form
    template_name = 'board/board_update.html'
    success_url = '/board/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'board/board_success.html', {"message": "일정을 업데이트 했습니다"})

    def get(self, request, *args, **kwargs):
        #오브젝트를 받아와서 폼 클래스를 받아온 후 이것을 return 해줘야한다.
        self.object=self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)


#detail view
class board_detail(generic.DetailView):
    model = List
    template_name = 'board/board_detail.html'
    context_object_name = 'list'

# when write new list
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
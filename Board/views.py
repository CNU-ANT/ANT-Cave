from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView

from Board.forms import PostForm, CommentForm
from ANTCave.settings import LOGIN_URL


# Create your views here.
from Board.models import PedigreePost
from Profile.models import UserInfo


def upload_file(file):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


@login_required(login_url=LOGIN_URL)
def main_page(request):
    return render(request, 'main.html')


class IndexView(ListView):
    template_name = 'board/board.html'
    paginate_by = 15

    def get_queryset(self):
        return self.kwargs['post'].__class__.objects.order_by('-id')[:15]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['b_name'] = self.kwargs['b_name']
        context['b_name_e'] = self.kwargs['b_name_e']
        context['count'] = self.kwargs['post'].__class__.objects.all().count()

        context['detail'] = reverse(self.kwargs['namespace']+':board')
        context['new'] = reverse(self.kwargs['namespace']+':new')
        return context


class NewView(FormView):
    template_name = 'board/edit_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse(self.kwargs['namespace']+':board')

    def get_context_data(self, **kwargs):
        context = super(NewView, self).get_context_data(**kwargs)
        context['b_name'] = self.kwargs['b_name']
        context['b_name_e'] = self.kwargs['b_name_e']
        return context

    def form_valid(self, form):
        post = self.kwargs['post']
        post.title = form.cleaned_data.get('title')
        post.text = form.cleaned_data.get('text')
        post.file = form.cleaned_data.get('file') #
        post.writer = UserInfo.objects.get(user=self.request.user)

        post.save()
        return super(NewView, self).form_valid(form)


class EditView(FormView):
    template_name = 'board/edit_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse(self.kwargs['namespace']+':board')

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context['b_name'] = self.kwargs['b_name']
        context['b_name_e'] = self.kwargs['b_name_e']
        return context

    def form_valid(self, form):
        post = self.kwargs['post']
        post.title = form.cleaned_data.get('title')
        post.text = form.cleaned_data.get('text')
        post.file = form.cleaned_data.get('file') #
        post.save()
        return super(EditView, self).form_valid(form)


class ContentView(FormView):
    template_name = 'board/detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(ContentView, self).get_context_data(**kwargs)
        context['b_name'] = self.kwargs['b_name']
        context['b_name_e'] = self.kwargs['b_name_e']

        context['content'] = self.kwargs['post'].__class__.objects.get(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        return super(ContentView, self).form_valid(form)


@csrf_exempt
@login_required(login_url=LOGIN_URL)
def pedigree_page(request):
    if request.method == "POST":
        b_name = '족보 게시판'
        b_name_e = 'Pedigree page'
        new = reverse('pedigree:new')
        return render(request, 'board/board.html', locals())
    return render(request, 'board/pedigree.html')


# @login_required(login_url=LOGIN_URL)
# def pedigree_detail_page(request, pk):
#     # TODO : 입력으로 줄 모델을 만들어야 합니다.
#     return render(request, 'board/pedigree_detail.html', locals())


# @login_required(login_url=LOGIN_URL)
# def pedigree_edit_page(request):
#     return render(request, 'board/pedigree_edit.html', locals())
#
#
# @login_required(login_url=LOGIN_URL)
# def pedigree_new_page(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             TeamPostFile(file=request.FILES.get('file'))
#             upload_file(request.FILES.get('file'))
#         return redirect('pedigree/')
#     form = PostForm()
#     return render(request, 'board/pedigree_new.html', locals())

#
# @login_required(login_url=LOGIN_URL)
# def greetings_page(request):
#     return render(request, 'board/greetings.html')
#
#
# @login_required(login_url=LOGIN_URL)
# def greetings_detail_page(request, pk):
#     # TODO : 입력으로 줄 모델을 만들어야 합니다.
#     return render(request, 'board/greetings_detail.html', locals())
#
#
# @login_required(login_url=LOGIN_URL)
# def team_page(request):
#     return render(request, 'board/team.html')
#
#
# @login_required(login_url=LOGIN_URL)
# def team_detail_page(request, pk):
#     # TODO : 입력으로 줄 모델을 만들어야 합니다.
#     return render(request, 'board/team_detail.html', locals())
#
#
# @login_required(login_url=LOGIN_URL)
# def share_info_page(request):
#     return render(request, 'board/share.html')
#
#
# @login_required(login_url=LOGIN_URL)
# def share_detail_page(request, pk):
#     # TODO : 입력으로 줄 모델을 만들어야 합니다.
#     return render(request, 'board/share_detail.html', locals())
#
#
# @login_required(login_url=LOGIN_URL)
# def ant_algo_page(request):
#     return render(request, 'board/ant_algo.html')
#
#
# @login_required(login_url=LOGIN_URL)
# def ant_algo_detail_page(request, pk):
#     # TODO : 입력으로 줄 모델을 만들어야 합니다.
#     return render(request, 'board/ant_algo_detail.html', locals())
#
#
# @login_required(login_url=LOGIN_URL)
# def competition_algo_page(request):
#     return render(request, 'board/competition_algo.html')
#
#
# @login_required(login_url=LOGIN_URL)
# def competition_algo_detail_page(request, pk):
#     # TODO : 입력으로 줄 모델을 만들어야 합니다.
#     return render(request, 'board/competition_algo_detail.html', locals())

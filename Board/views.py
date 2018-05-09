from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView

from Board.forms import PostForm, CommentForm
from ANTCave.settings import LOGIN_URL, BASE_URL

# Create your views here.
from Board.models import PedigreePost
from Profile.models import UserInfo


def main_page(request):
    return render(request, 'main.html')


class IndexView(ListView):
    template_name = 'board/board.html'
    paginate_by = 15

    def get_queryset(self):
        return self.kwargs['post'].__class__.objects.order_by('-id')[:]

    def get_paginator(self, queryset, per_page, orphans=0,
                      allow_empty_first_page=True, **kwargs):
        return Paginator(queryset, self.paginate_by)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['b_name'] = self.kwargs['b_name']
        context['b_name_e'] = self.kwargs['b_name_e']
        context['namespace'] = self.kwargs['namespace']
        context['board'] = reverse(self.kwargs['namespace']+':board')
        context['new'] = reverse(self.kwargs['namespace']+':new')
        return context


class NewView(FormView):
    template_name = 'board/edit_post.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super(NewView, self).get_context_data(**kwargs)
        context['b_name'] = self.kwargs['b_name']
        context['b_name_e'] = self.kwargs['b_name_e']
        context['board'] = reverse(self.kwargs['namespace'] + ':board')
        return context

    def form_valid(self, form):
        post = self.kwargs['post']
        post.title = form.cleaned_data.get('title')
        post.text = form.cleaned_data.get('text')
        post.writer = UserInfo.objects.get(user=self.request.user)
        post.save()

        for file in self.request.FILES.getlist('file'):
            self.kwargs['file'].__class__.objects.create(post=post, file=file)

        self.success_url = reverse(self.kwargs['namespace']+':detail', kwargs={'pk':post.id})
        return super(NewView, self).form_valid(form)


class EditView(FormView):
    template_name = 'board/edit_post.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context['b_name'] = self.kwargs['b_name']
        context['b_name_e'] = self.kwargs['b_name_e']
        context['board'] = reverse(self.kwargs['namespace'] + ':board')
        return context

    def form_valid(self, form):
        try:
            post = self.kwargs['post'].__class__.objects.get()
            post_file = self.kwargs['file'].__class__.objects.get(post=post)
        except:
            post = self.kwargs['post']
            post_file = self.kwargs['file']

        post.title = form.cleaned_data.get('title')
        post.text = form.cleaned_data.get('text')
        post.save()

        # TODO : Edit 은 New 와 처리할 것이 다름.

        post_file.file = form.cleaned_data.get('file')
        post_file.save()

        self.success_url = reverse(self.kwargs['namespace'] + ':detail', kwargs={'pk': post.id})
        return super(EditView, self).form_valid(form)


class ContentView(FormView):
    template_name = 'board/detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(ContentView, self).get_context_data(**kwargs)
        context['b_name'] = self.kwargs['b_name']
        context['b_name_e'] = self.kwargs['b_name_e']
        context['namespace'] = self.kwargs['namespace']
        context['edit'] = reverse(self.kwargs['namespace'] + ':edit')
        context['content'] = self.kwargs['post'].__class__.objects.get(id=self.kwargs['pk'])
        try:
            context['comments'] = self.kwargs['comment'].__class__.objects.filter(post=context['content'])
        except:
            pass
        try:
            context['files'] = self.kwargs['file'].__class__.objects.filter(post=context['content'])
        except:
            pass
        return context

    def get_success_url(self):
        return reverse(self.kwargs['namespace']+':detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        self.kwargs['comment'].__class__.objects.create(
            post=self.kwargs['post'].__class__.objects.get(id=self.kwargs['pk']),
            writer=UserInfo.objects.get(user=self.request.user),
            text=form.cleaned_data.get('text')
        )
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

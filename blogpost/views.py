from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import DetailView
from .models import BlogModel

# Create your views here.
class BlogList(ListView):
  template_name = 'list.html'
  model = BlogModel

class BlogDetail(DetailView):
  template_name = 'detail.html'
  model = BlogModel

class BlogCreate(CreateView):
  template_name = 'create.html'
  model = BlogModel 
  # （model = BlogModel）ユーザーが入力した情報をどのテーブルに保存するか指定
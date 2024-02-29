from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product, Lesson

class ProductsList(ListView):
    model = Product
    ordering = 'product_name'
    template_name = 'products.html'
    context_object_name = 'product'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class LessonList(ListView):
    model = Lesson
    ordering = 'product_name'
    template_name = 'lesson.html'
    context_object_name = 'lesson'

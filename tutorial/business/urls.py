from django.urls import path
from .views import ProductsList , ProductDetail, LessonList

urlpatterns = [
    path('products/', ProductsList.as_view()),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('lesson/<int:pk>', LessonList.as_view(), name='lesson_list'),
]
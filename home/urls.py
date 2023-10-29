from django.urls import path

from . import views
from .views import *

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename = 'todo')

urlpatterns = [
  # path('',views.get_appi,name='home'),
  # path('post-todo/', views.post_todo,name='post_todo'),
  # path('patch-todo/', views.patch_todo, name='patch_todo'),
   path('todo/', TodoView.as_view())

]

urlpatterns += router.urls
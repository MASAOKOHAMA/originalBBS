from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/detail', views.detail, name='detail'),
    path('new', views.new, name='new'),
    # path('create', views.create, name='create'),
    path('create', views.BoardCreate.as_view(), name='create'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>', views.good, name='good'),
    path('<int:id>/favo', views.favo, name='favo'),
]

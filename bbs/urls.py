from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'bbs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/detail', views.detail, name='detail'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:pk>', views.good, name='good'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

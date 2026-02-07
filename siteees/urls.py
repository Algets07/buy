from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('result/', views.result, name='result'),
    path('dele/<int:id>',views.delete,name='delete'),
    path('details/<int:id>',views.view_detail,name='detail'),
    path('buy',views.buy,name='buy'),
    path('b',views.profile,name='profile'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

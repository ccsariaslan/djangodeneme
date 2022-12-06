from django.contrib import admin
from django.urls import path
from . import views



app_name = "article"


urlpatterns = [
    path('kontrolpaneli/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addarticle,name="addarticle"),
    path('makale/<int:id>',views.detail,name="detail"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name='update'),
    path('',views.Makaleler,name="Makaleler"),
    path('comment/<int:id>',views.addcomment,name="comment")
]


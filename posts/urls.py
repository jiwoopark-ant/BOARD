from django.urls import path
from . import views

app_name='posts'

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:id>/',views.detail, name='detail'),

    #create
    path('new/', views.new, name='new') ,
    path('create/', views.create, name='create') ,
    
    #delete
    path('<int:id>/delete/', views.delete, name='delete') ,
    #update
    path('<int:id>/edit/',views.edit, name='edit'),
    path('<int:id>/update/',views.update, name='update'),

]
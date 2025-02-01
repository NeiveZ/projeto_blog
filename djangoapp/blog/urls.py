from django.urls import path
form blog.views import index

app_name = 'blog'
urlpatterns = [
    path('',index, name='index'),
]


from django.contrib import admin
from django.urls import path
from platzigram import views as local_views

from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.helloWorld),
    path('numbers/', local_views.numbers),
    path('hi/<str:name>/<int:age>/', local_views.hi),
    path('posts/', posts_views.list_posts),
]

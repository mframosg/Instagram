
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from platzigram import views as local_views
from users import views as user_views

from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.helloWorld, name='hello_world'),
    path('numbers/', local_views.numbers, name='numbers'),
    path('hi/<str:name>/<int:age>/', local_views.hi, name='hi'),
    path('posts/', posts_views.list_posts, name='feed'),
    
    path('users/login/', user_views.login_view, name='login'),
    path('users/logout/', user_views.logout_view, name='logout'),
    path('users/signup/', user_views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

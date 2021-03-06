"""newpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include

from newapp.views import CrudView, DeleteCrudUser, update
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', CrudView.as_view(), name='list'),
    path('form/', views.newform, name='form'),
    path('register/', views.register, name='register'),
    path('update/<int:id>', views.update, name='update'),

    path('', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('delete/', DeleteCrudUser.as_view(), name='delete'),

    path('detail/<int:id>', views.CrudNewdetail, name='detail')
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   urlpatterns += static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

"""Space URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from ReferenceBook.views import index, info, edit, create, delete, edit_article, fix, delete_article, fix_article

urlpatterns = [
    path('', index, name='index'),
    path('info/<int:spacecrafts_id>/', info),
    path('edit/', edit, name='edit'),
    path('admin/', admin.site.urls),
    path('edit/create/', create),
    path('delete/<int:id>/', delete),
    path('info/<int:spacecrafts_id>/edit_article/', edit_article),
    path('info/<int:spacecrafts_id>/fix_article/', fix_article),
    path('info/<int:spacecrafts_id>/delete_article/', delete_article),
    path('fix/<int:id>/', fix),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
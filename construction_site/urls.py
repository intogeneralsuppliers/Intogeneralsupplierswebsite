"""construction_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Into General Suppliers Administration"
admin.site.site_title = "Into General Suppliers Administration"
admin.site.index_title = "Into General Suppliers Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Into_General_Suppliers.urls')),
    # url(r'^admin/', admin.site.urls),
    # path('home/', user_views.Dashboard, name='home'),
    # path('services/', user_views.Dashboard, name='services'),
    # path('projects/', user_views.Dashboard, name='projects'),
    # path('about/', user_views.Dashboard, name='about'),
    # path('blog/', user_views.Dashboard, name='blog'),
    # path('contact/', user_views.Dashboard, name='contact'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
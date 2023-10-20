"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from first_project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage),
    path('admin-path/', admin.site.urls),
    path('about-us/', views.AboutUs, name='AboutUs'),
    path('course/', views.course, name='course'),
    path('course/<str:courseid>', views.coursedetails, name='coursedetails'),
    path('userform/', views.userform, name='userform'),
    path('submitform/', views.submitform, name='submitform'),
    path('calculator/', views.calculator, name='calculator'),
    path('checkevenodd/', views.checkevenodd),
    path('marksheet/', views.marksheet),
    path('Newsdetails/<slug>', views.Newsdetails),
    path('services/', views.services),
    path('formsave/',views.saveEnquiry, name='formsave'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
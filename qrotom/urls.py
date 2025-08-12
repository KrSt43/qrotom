"""
URL configuration for qrotom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from qrotom.views import register_choice
from advertisements import views as adv_views
from customers import views as cust_views
from corporate import views as corp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', adv_views.advertisement_list, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register_choice, name='register_choice'),
    path('register/customer/', cust_views.register_customer, name='register_customer'),
    path('register/corporate/', corp_views.register_corporate, name='register_corporate'),
    path('advertisement/create/', adv_views.create_advertisement, name='create_advertisement'),
    path('advertisement/<int:pk>/', adv_views.advertisement_detail, name='advertisement_detail'),
    path('advertisement/<int:pk>/edit/', adv_views.edit_advertisement, name='edit_advertisement'),
    path('advertisement/<int:pk>/delete/', adv_views.delete_advertisement, name='delete_advertisement'),
    path('my-advertisements/', adv_views.my_advertisements, name='my_advertisements'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

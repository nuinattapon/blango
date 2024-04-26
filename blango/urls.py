"""blango URL Configuration

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
import debug_toolbar

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import blango_auth.views
import blog.views

from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("ip/", blog.views.get_ip),

    path("accounts/", include("django.contrib.auth.urls")),
        path("accounts/", include("allauth.urls")),

    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
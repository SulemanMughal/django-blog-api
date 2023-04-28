"""blogapi URL Configuration

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
from django.urls import path, include, re_path
# from django.conf.urls import url
# from allauth.account.views import confirm_email
# from django.urls import re_path
# from allauth.account.views import confirm_email
# from django.conf.urls import  url

from dj_rest_auth.registration.views import VerifyEmailView
from rest_framework.schemas import get_schema_view
from rest_framework import permissions # new
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new

schema_view = get_schema_view( # new
openapi.Info(
title="Blog API",
default_version="v1",
description="A sample API for learning DRF",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="hello@example.com"),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # re_path('rest-auth/registration/account-confirm-email/(?P<key>.+)/', CustomConfirmEmailView.as_view(), name='account_confirm_email')    
    # path('api/v1/dj-rest-auth/registration/account-confirm-email/(?P<key>.+)/', confirm_email, name='account_confirm_email'),
    # path('accounts-rest/registration/account-confirm-email/<key>.+)/', confirm_email, name='account_confirm_email'),
    re_path(r'registration/account-confirm-email/', VerifyEmailView.as_view(),
            name='account_email_verification_sent'),
    re_path(r'registration/account-confirm-email/(?P<key>[-:\w]+)/', VerifyEmailView.as_view(),
            name='account_confirm_email'),
#             path('openapi', get_schema_view( # new
# title="Blog API",
# description="A sample API for learning DRF",
# version="1.0.0"
# ), name='openapi-schema'),
path('swagger/', schema_view.with_ui( # new
'swagger', cache_timeout=0), name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui( # new
'redoc', cache_timeout=0), name='schema-redoc'),
]

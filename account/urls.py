from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('account/', include('django.contrib.auth.urls')),

    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    # login / logout urls
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('logout-then-login/', auth_views.logout_then_login),

    # Change password urls
    path('password-change/', auth_views.PasswordChangeView.as_view()),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view()),

    # restore password urls
    path('password-reset', auth_views.PasswordResetView.as_view()),
    path('password-reset/done/', auth_views.PasswordChangeDoneView.as_view()),
    path('password-reset/confirm/', auth_views.PasswordResetConfirmView.as_view()),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view()),
]

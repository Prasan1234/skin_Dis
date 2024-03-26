from django.contrib import admin
from django.urls import path
from detection import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('upload/', views.upload_image, name='upload_image'),
    path('user/', views.user_page, name='user_page'),
    path('verify-otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
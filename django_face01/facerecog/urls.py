from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('capture_face/', CaptureFaceView.as_view(), name='capture_face'),
    path('success/', success, name='success'),
    path('face_detection/', FaceDetectionView.as_view(), name='face_detection'),
    path('register_user/', register_user, name='register_user'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('manager/', manager_dashboard, name='manager_dashboard'),
    path('user/<int:user_id>/', user_detail, name='user_detail'),
    path('members/', member_list, name='member_list'),
    path('members/edit/<int:pk>/', member_edit, name='member_edit'),
    path('members/delete/<int:pk>/', member_delete, name='member_delete'),
]

from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('admin/signup/', views.admin_signup, name='admin_signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/update/',
         views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/',
         views.UserDeleteView.as_view(), name='user_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('onboarding', views.onboarding, name='onboarding'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('categories', views.categories, name='categories'),
    path('profile', views.profile, name='profile'),
    path('profileupdate', views.profileupdate, name='profileupdate'),
    path('passwordupdate', views.passwordupdate, name='passwordupdate'),
    path('aboutus', views.about_us, name='about_us'),
    path('all_category', views.all_category, name='all_category'),
    path('category/<str:id>', views.single_category, name='category'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('submit_review/<str:id>', views.detail, name='submit_review'),  # for submitting reviews
]
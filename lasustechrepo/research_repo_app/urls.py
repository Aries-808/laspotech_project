from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name = 'home'),
    path('submit/thesis/', views.submit_thesis, name='submit_thesis'),
    path('submit/research_paper/', views.submit_research_paper, name='submit_research_paper'),
    path('submit/research_data/', views.submit_research_data, name='submit_research_data'),
    path('research_papers/', views.research_list, name='research_list'),
    path('theses/', views.thesis_list, name='thesis_list'),
    path('research_papers/<int:paper_id>/', views.research_details, name='research_details'),
    path('theses/<int:thesis_id>/', views.thesis_details, name='thesis_details'),

]

from django.urls import path, include

from results import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('view-module-result/<slug>/', views.ViewModuleResult.as_view(), name='view_module_result'), 
    path('select-module', views.select_module, name='select_module'), 
    path('get-assessment-group/', views.get_assessment_group, name='get_assessment_group'), 
    path('get-assessments/', views.get_assessments, name='get_assessments'), 
]

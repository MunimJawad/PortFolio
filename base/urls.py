from django.urls import path
from .import views

urlpatterns=[
    path('',views.homePage,name='home'),
    path('project/<str:pk>', views.projectPage,name='project'),
    path('add-project/',views.addProject,name='add-project'),
    path('all-project/',views.projectAll,name='all-project'),
    path('edit-project/<str:pk>/', views.editProject, name="edit-project"),
    path('inbox/',views.inboxPage,name='inbox'),
    path('endorsment/',views.endorsment,name='endorsment'),
    path('delete/<str:pk>/',views.deleteProject,name='delete'),
    path('contact/',views.contactPage,name='contact'),
    path('message/<str:pk>/',views.messagePage,name='message'),
    path('add-skill/',views.addSkill,name='add-skill'),
    path('admin1/',views.func,name='admin')


]


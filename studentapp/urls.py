from django.urls import path, include
from studentapp.views import student_info,CreateTemplate,StudentCreateView


urlpatterns = [

    path('student/', student_info),
    path('studentcreateform/', StudentCreateView.as_view()),
    path('studentcreate/', CreateTemplate.as_view(),name="send")

]


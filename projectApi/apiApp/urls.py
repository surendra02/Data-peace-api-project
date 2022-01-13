from django.urls import path
from .import views
urlpatterns = [
    path('users/',views.saveOrAllData),
    path('users/<int:eid>/',views.singleData),
    path('find-users/',views.EmployeeList.as_view()),
]

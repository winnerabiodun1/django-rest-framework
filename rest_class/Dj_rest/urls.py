from django.urls import path, include
from . import views
urlpatterns = [
        path('create-student/', views.StudentViews.as_view(), name='student')
]
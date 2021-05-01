from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


# Create your views here.

# Making a POST request
class StudentViews(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)


# Making a GET request
class GetStudentViews(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UpdateStudentViews(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeleteStudentViews(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

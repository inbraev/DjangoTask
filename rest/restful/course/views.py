from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView


# courses
class CourseList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# categories
class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Branches
class BranchList(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetail(RetrieveDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


# contacts
class ContactsList(ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsDetail(RetrieveDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

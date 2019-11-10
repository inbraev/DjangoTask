from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.CourseList.as_view(),name="CourseListUrl"),
    path('course/<int:pk>/', views.CourseDetail.as_view(),name="CourseDetailUrl"),
    path('category/', views.CategoryList.as_view(),name="CategoryListUrl"),
    path('category/<int:pk>/', views.CategoryDetail.as_view(),name="CategoryDetailUrl"),
    path('branch/', views.BranchList.as_view(),name="BranchListUrl"),
    path('branch/<int:pk>/', views.BranchDetail.as_view(),name="BranchDetailUrl"),
    path('contacts/', views.ContactsList.as_view(),name="ContactsListUrl"),
    path('contacts/<int:pk>/', views.ContactsDetail.as_view(),name="ContactsDetailUrl"),
]

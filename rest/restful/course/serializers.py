from rest_framework import serializers
from .models import *


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['type','value']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['name','imgpath']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['longitude',"latitude","address"]


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = ['name', 'description', 'category', 'logo', 'branches', 'contacts']

    def create(self, validated_data):
        branches_data = validated_data.pop('branches')
        contacts_data = validated_data.pop('contacts')
        course = Course.objects.create(**validated_data)

        for branch_data in branches_data:
            Branch.objects.create(course=course, **branch_data)

        for contact_data in contacts_data:
            Contacts.objects.create(course=course, **contact_data)

        return course
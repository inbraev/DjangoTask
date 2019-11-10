from model_mommy import mommy
from rest_framework.test import APITestCase
from course.models import *


class CategoryTestMommy(APITestCase):

    def test_category_creation_mommy(self):
        category = mommy.make(Category)
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), category.name)


class BranchTestMommy(APITestCase):

    def test_branch_creation_mommy(self):
        branch = mommy.make(Branch)
        self.assertTrue(isinstance(branch, Branch))
        self.assertEqual(branch.__str__(), branch.address)


class ContactTestMommy(APITestCase):

    def test_contact_creation_mommy(self):
        contact = mommy.make(Contacts)
        self.assertTrue(isinstance(contact, Contacts))
        self.assertEqual(contact.__str__(), contact.type)


class CourseTestMommy(APITestCase):

    def test_course_creation_mommy(self):
        course = mommy.make(Course)
        self.assertTrue(isinstance(course, Course))
        self.assertEqual(course.__str__(), course.name)

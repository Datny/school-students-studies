from django.test import TestCase
from school.models import Teacher



class TeacherModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Teacher.objects.create(name='Big', description='Bob')

    def test_first_name_label(self):
        teacher = Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_first_name_max_length(self):
        teacher = Teacher.objects.get(id=1)
        max_length = teacher._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


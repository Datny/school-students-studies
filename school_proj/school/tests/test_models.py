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

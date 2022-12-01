from django import test
from django.urls import reverse
from programs.models import Program
# Create your tests here.


class HomePageTest(test.SimpleTestCase):
    def test_home_page_response_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(
            response, 'Welcome to the University of Dodoma programs finder')

    def test_home_page_dont_contain_correct_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hello there, I am not contained in home page')

    def test_correct_template_name_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ProgramPageTest(test.TestCase):
    def test_program_page_response_status_code(self):
        response = self.client.get('/programs/')
        self.assertEqual(response.status_code, 200)

    def test_program_page_by_name(self):
        response = self.client.get(reverse('program_list'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_name_used(self):
        response = self.client.get('/programs/')
        self.assertTemplateUsed(response, 'program_list.html')


class ProgramCreationTest(test.SimpleTestCase):
    name = 'Course'
    college = 'COLLEGE OF INFORMATICS AND VIRTUAL EDUCATION'
    year_of_study = 2
    fee = 120000
    field_of_work = 'IT'

    def program_create_status_code(self):
        Program.objects.create(name=self.name, college=self.college,
                               years_of_study=self.year_of_study, fee=self.fee, field_of_work=self.field_of_work)

from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        """
        Test the status code for the home page.
        """
        response = self.client.get(reverse('index'))  # 'index' is the name of the view
        self.assertEqual(response.status_code, 200)  # Expect status code 200

    def test_home_view_template_used(self):
        """
        Test that the correct template is used for the home view.
        """
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')  # Check if 'index.html' template is used

    def test_home_view_content(self):
        """
        Test the content on the home page.
        """
        response = self.client.get(reverse('index'))
        self.assertContains(response, "DevStudio")  # Look for the text "DevStudio" on the page

# from django.test import TestCase
# from .models import YourModel

# class YourModelTest(TestCase):
#     def test_model_string_representation(self):
#         """
#         Test the string representation of the model.
#         """
#         instance = YourModel.objects.create(name="Test Object")
#         self.assertEqual(str(instance), "Test Object")  # Adjust based on your model's `__str__` method

#     def test_model_field(self):
#         """
#         Test that a specific field has the correct default value.
#         """
#         instance = YourModel.objects.create(name="Test Object")
#         self.assertEqual(instance.name, "Test Object")  # Ensure the name field is saved correctly


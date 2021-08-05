from django.test import TestCase

from products.models import Colour

class ColourModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Set up non-modified objects used by all test methods
    Colour.objects.create(
        name='Purple',
        rgb_code='230,230,250',
        description='Purple, one of my favorite colours.'
    )

  def test_name_label(self):
    colour = Colour.objects.get(id=1)
    field_label = colour._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_rgb_code_label(self):
    colour = Colour.objects.get(id=1)
    field_label = colour._meta.get_field('rgb_code').verbose_name
    self.assertEqual(field_label, 'rgb code')

  def test_name_max_length(self):
    colour = Colour.objects.get(id=1)
    max_length = colour._meta.get_field('name').max_length
    self.assertEqual(max_length, 200)

  def test_rgb_code_max_length(self):
    colour = Colour.objects.get(id=1)
    max_length = colour._meta.get_field('rgb_code').max_length
    self.assertEqual(max_length, 200)

  def test_description_max_length(self):
    colour = Colour.objects.get(id=1)
    max_length = colour._meta.get_field('description').max_length
    self.assertEqual(max_length, 200)

  def test_object_name_is_name_then_description(self):
    colour = Colour.objects.get(id=1)
    expected_object_name = f'{colour.name} {colour.description}'
    self.assertEqual(str(colour), expected_object_name)
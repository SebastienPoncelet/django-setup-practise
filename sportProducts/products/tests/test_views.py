from django.test import TestCase
from django.urls import reverse

from products.models import Colour

# TODO: Add test for views restricted to logged in user or based on other permissions


class ColourListViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    # Create 13 colours for pagination tests
    number_of_colours = 13

    for colour_id in range(number_of_colours):
      Colour.objects.create(
        name=f'Purple {colour_id}',
        rgb_code=f'Purple RGB code {colour_id}',
        description=f'Purple Description {colour_id}',
      )

  def test_view_url_exists_at_desired_location(self):
    response = self.client.get('/products/colours/')
    self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
    response = self.client.get(reverse('colours'))
    self.assertEqual(response.status_code, 200)

  # Test example if a pagination has been set with a limit of 10 objects per page.
  # def test_pagination_is_ten(self):
  #   response = self.client.get(reverse('colours'))
  #   self.assertEqual(response.status_code, 200)
  #   self.assertTrue('is_paginated' in response.context)
  #   self.assertTrue(response.context['is_paginated'] == True)
  #   self.assertEqual(len(response.context['colour_list']), 10)

  def test_lists_all_colours(self):
    # Get second page and confirm it has (exactly) remaining 3 items
    response = self.client.get(reverse('colours')+'?page=2')
    self.assertEqual(response.status_code, 200)
    self.assertTrue('is_paginated' in response.context)
    self.assertTrue(response.context['is_paginated'] == True)
    self.assertEqual(len(response.context['colour_list']), 3)

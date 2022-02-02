#from django.test import TestCase
import json
from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate


from .models import Favorite, Quote
from .views import UserRegisteration, UserFavorites, UserQuotes, ObtainCharacters, CharactersQuotes, ObtainFavorites

# Create your tests here.

# Test for registeration endpoint
class RegisterationTestCase(APITestCase):

	def setUp(self):
		self.factory = APIRequestFactory()
		self.url = reverse("signup")
		self.view = UserRegisteration.as_view()

	def test_registeration(self):

		payload = {'username':'kene',
		'email':'kene@company.com', 
		'password':'kene123'}

		request = self.factory.post(self.url, data=payload, format='json')

		response = self.view(request)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)



# Test for user favorite character endpoint
class FavoriteTestCase(APITestCase):


	def setUp(self):
		self.user = User.objects.create_user(username="kens",password="ken123")
		self.factory = APIRequestFactory()
		self.url = reverse("user_favorites", kwargs={'id':"5cd99d4bde30eff6ebccfbc2"} )
		self.view = UserFavorites.as_view()


	def test_favorites_authenticated(self):
		request = self.factory.post(self.url)
		force_authenticate(request, user=self.user)
		response = self.view(request, id="5cd99d4bde30eff6ebccfbc2")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# Test for user favorite character quote endpoint
class QuoteTestCase(APITestCase):

	def setUp(self):
		self.user = User.objects.create_user(username="kens",password="ken123")
		self.factory = APIRequestFactory()
		self.url = reverse("user_quotes", kwargs={'char_id':"5cd99d4bde30eff6ebccfbc2",'quo_id':"5cd99d4bde30eff6ebccfbbe"})
		self.view = UserQuotes.as_view()


	def test_quotes_authenticated(self):
		request = self.factory.post(self.url)
		force_authenticate(request, user=self.user)
		response = self.view(request, char_id="5cd99d4bde30eff6ebccfbc2", quo_id="5cd99d4bde30eff6ebccfbbe")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Test for get characters endpoint
class CharacterTestCase(APITestCase):

	def setUp(self):
		self.factory = APIRequestFactory()
		self.url = reverse("character")
		self.view = ObtainCharacters.as_view()


	def test_character(self):
		request = self.factory.get(self.url)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


#Test for get specific character quotes endpoint
class CharacterQuotesTestCase(APITestCase):

	def setUp(self):
		self.factory = APIRequestFactory()
		self.url = reverse("character_quotes",kwargs={'id':"5cd99d4bde30eff6ebccfbc2"})
		self.view = CharactersQuotes.as_view()


	def test_quote_character(self):
		request = self.factory.get(self.url)
		response = self.view(request,id="5cd99d4bde30eff6ebccfbc2")
		self.assertEqual(response.status_code, status.HTTP_200_OK)



#Test for get all users favorite quotes and character end point
class GetFavoriteTestCase(APITestCase):

	def setUp(self):
		self.user = User.objects.create_user(username="kens",password="ken123")
		self.factory = APIRequestFactory()
		self.url = reverse("favorites")
		self.view = ObtainFavorites.as_view()


	def test_quote_character(self):
		request = self.factory.get(self.url)
		force_authenticate(request, user=self.user)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
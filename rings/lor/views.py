import requests as req
from knox.models import AuthToken
from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions 
from rest_framework.views import APIView
from rest_framework.response import Response
import functools
import itertools

from . models import Favorite, Quote
from . serializers import RegisterUserSerializer, LoginUserSerializer, UserSerializer, FavoriteSerializers, FavoriteQuoteSerializers


# Create your views here.

#get character requests
class CallApi(APIView):

	def get(self, requests, formats=None):

		data = {}
		data['message'] = 'testing testing'
		return Response(data, status=status.HTTP_200_OK)


#get character requests
class ObtainCharacters(APIView):

	def get(self, requests, formats=None):
 
		URL = "https://the-one-api.dev/v2"
		AUTH_CODE = settings.ONE_API_KEY 
		PARAMS = {'Authorization':AUTH_CODE}
		characters = '/character'
		url = URL + characters

		s = req.Session()
		s.headers.update(PARAMS)
		r = s.get(url = url, timeout=None)
		data = r.json()
		return Response(data, status=status.HTTP_200_OK)

	

#specific character quote requests
class CharactersQuotes(APIView):

	def get(self, requests, id, formats=None):


		URL = 'https://the-one-api.dev/v2'
		AUTH_CODE = settings.ONE_API_KEY 
		PARAMS = {'Authorization':AUTH_CODE}
		character_quotes = f'/character/{id}/quote'
		url = URL + character_quotes


		s = req.Session()
		s.headers.update(PARAMS)
		r = s.get(url = url)
		data = r.json()
		return Response(data, status=status.HTTP_200_OK)


#Registeration requests
class UserRegisteration(generics.GenericAPIView):

	def post(self, request, format=None):
		serializer = RegisterUserSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()

			return Response({
				"user": UserSerializer(user,context=serializer).data,
				"token": AuthToken.objects.create(user)[1]},status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		

# Login requests
class UserLogin(generics.GenericAPIView):

	def post(self, request, format=None):
		serializer = LoginUserSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.validated_data

    	    
			return Response({
				"user": UserSerializer(user,context=serializer).data,
				"token": AuthToken.objects.create(user)[1]})

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# favorite request
class UserFavorites(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = FavoriteSerializers
	queryset = Favorite.objects.all()

	def post(self, request, id, format=None):

		user = request.user		
		data = {}
		data['user_id'] = user.id
		data['character_id'] = id

		serializer = FavoriteSerializers(data=data)
		if serializer.is_valid():
			serializer.save()
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FavoriteQuoteSubClassFieldsMixin(object):
	def get_queryset(self):
		return Favorite.objects.select_subclasses()

# favorite, quote request
class UserQuotes(FavoriteQuoteSubClassFieldsMixin, generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = FavoriteQuoteSerializers

	def post(self, request, char_id, quo_id, format=None):

		user = request.user		
		data = {}
		data['user_id'] = user.id
		data['character_id'] = char_id
		data['quote_id'] = quo_id

		serializer = FavoriteQuoteSerializers(data=data)
		if serializer.is_valid():
			serializer.save()
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get favorites
class ObtainFavorites(generics.GenericAPIView):

	permission_classes = [permissions.IsAuthenticated]
	queryset = Favorite.objects.all()

	def get(self, requests,formats=None):

		
		URL = 'https://the-one-api.dev/v2'
		AUTH_CODE = settings.ONE_API_KEY 
		PARAMS = {'Authorization':AUTH_CODE}

		s = req.Session()
		s.headers.update(PARAMS)


		output = {}
		char_lis_output = []
		quo_lis_output = []
		

		# get all the characters
		distinct_characters = Favorite.objects.filter(user_id= requests.user.id).values_list('character_id').distinct() 
		output_characters = list(itertools.chain(*distinct_characters))

		# get all the quotes
		distinct_quotes = Quote.objects.filter(user_id= requests.user.id).values_list('quote_id').distinct() 
		output_quotes = list(itertools.chain(*distinct_quotes))

		output["charaters"] = output_characters
		output["quotes"] = output_quotes


		

		for i in output["charaters"]:

			character_url =  f'/character/{i}/'
			url = URL + character_url
			r = s.get(url = url)
			data = r.json()
			if 'docs' not in data:
				continue
			char_lis_output.append(data['docs'][0])


		for i in output["quotes"]:
			quote_url = f'/quote/{i}'
			url = URL + quote_url
			r = s.get(url = url)
			data = r.json()
			if 'docs' not in data:
				continue

			if len(data['docs']) == 0:
				quo_lis_output.append(None)
			else:
				quo_lis_output.append(data['docs'])
				

		output["charaters"] = char_lis_output
		output["quotes"] = quo_lis_output

		return Response(output, status=status.HTTP_200_OK)




		
		
		
		


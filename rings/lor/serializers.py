from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . models import Favorite, Quote



# user serializer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username']



# registeration serializer
class RegisterUserSerializer(serializers.ModelSerializer):

	password = serializers.CharField(write_only=True)

	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance

	class Meta:
		model = User
		fields = ['id','username','email', 'password']


# login serializer 
class LoginUserSerializer(serializers.Serializer):

	username =  serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		user = authenticate(**data)
		if user and user.is_active:
			return user
		raise serializers.ValidationError("Incorrect Credentials")



	class Meta:
		model = User
		fields = ['username', 'password']



# favorite serializer
class FavoriteSerializers(serializers.ModelSerializer):

	class Meta:
		model = Favorite
		fields = ['user_id','character_id'] 

# favorite serializer
class QuoteSerializers(serializers.ModelSerializer):
	
	class Meta:
		model = Quote
		fields = ['user_id','character_id','quote_id'] 
		depth = 1


class FavoriteQuoteSerializers(serializers.ModelSerializer):

	def to_representation(self, instance):

		if isinstance(instance, Quote):

			output={}

			hold = QuoteSerializers(instance=instance).data
			id_ = hold["user_id"]["id"]
			char_id = hold["character_id"]
			quo_id = hold["quote_id"]


			output["user_id"] = id_
			output["character_id"] = char_id 
			output["quote_id"] = quo_id


			return output
		else:
			return FavoriteSerializers(instance=instance).data

	class Meta:
		model = Quote
		fields = ['user_id','character_id','quote_id']


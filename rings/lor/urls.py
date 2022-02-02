from django.urls import path
from .views import *
from knox import views as knox_views



urlpatterns = [
    path('',CallApi.as_view(), name="api_call"),
    path('characters/', ObtainCharacters.as_view(), name="character"),
    path('characters/<str:id>/quotes/', CharactersQuotes.as_view(),  name="character_quotes"),
    path('characters/<str:id>/favorites/', UserFavorites.as_view(), name="user_favorites"),
    path('characters/<str:char_id>/quotes/<str:quo_id>/favorites/', UserQuotes.as_view(), name="user_quotes"),
    path('favorites/', ObtainFavorites.as_view(), name="favorites"),
    path('register/', UserRegisteration.as_view(),name="signup"),
    path('login/', UserLogin.as_view(),name="login"),
    path('logout/',knox_views.LogoutView.as_view(), name='knox_logout')
]

from django.contrib import admin
from django.urls import path, include
from main import views

app_name = "main"
urlpatterns = [

    path("login/", views.login_view, name='login'),

    path("", views.main, name='main'),
    path("buy/", views.buy_view, name="buy_view"),
    path("buy/create/", views.buy_create, name="buy_create"),





    # 거래처 URL
    path("client/", views.client_view, name="client_view"),
    path("client/create/", views.client_create, name="client_create"),
    path("client/modify/", views.client_modify, name="client_modify"),


    path("search/items/", views.search_items, name="search_items"),


]

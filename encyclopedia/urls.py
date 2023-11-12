from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random_pages", views.random_pages, name='random_pages'),
    path("wiki/new_entry", views.new_entry, name='new_entry'),
    path("wiki/<str:title>", views.display, name='display'),
    path("wiki/edit/<str:title>", views.edit_page, name='edit_page')

]

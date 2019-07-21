from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('ayu/',views.ayu),
    path('add/',views.add_contact, name='add_contact'),
    path('',views.show_contacts, name='show_contact'),
    path('delete/<int:id>/',views.delete_contact, name='delete_contact'),
    path('update/<int:id>/',views.update_contact, name='update_contact'),
]

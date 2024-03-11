from django.urls import path
import presentation.views

urlpatterns = [
    path('', presentation.views.main_page, name='home')
]
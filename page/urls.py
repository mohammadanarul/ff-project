from django.urls import path
from page.views import landing_page


urlpatterns = [
    path('', landing_page, name='home')
]

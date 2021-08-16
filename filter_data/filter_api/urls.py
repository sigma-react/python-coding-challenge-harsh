
from django.urls import path, include

from filter_api.views import FilterApi

urlpatterns = [

    path('filter/', FilterApi.as_view()),
]

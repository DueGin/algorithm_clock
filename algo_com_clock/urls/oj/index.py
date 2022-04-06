from django.urls import path, include
from algo_com_clock.views.get_info import index

urlpatterns = [
    path("get_info/", index, name="text_info")
]

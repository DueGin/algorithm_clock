from django.urls import path, include
from algo_com_clock.views.index import index

urlpatterns = [
    path("", index, name="oj website"),
    path("oj/", include("algo_com_clock.urls.oj.index")),
    
]

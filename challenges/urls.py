from django.urls import path
from . import views

urlpatterns = [
    path('<month>', views.monthlyChallenges)
    # path('january', views.january),
    # path('february', views.february),
]

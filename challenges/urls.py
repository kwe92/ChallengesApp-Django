from django.urls import path
from . import views

urlpatterns = [
    # Dynamic Path Segment:
    #   - Defined by a capture value, a variable name between angle brackets: <variable_name>
    path('<month>', views.monthlyChallenges)
]

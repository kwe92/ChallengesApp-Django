from django.urls import path
from . import views

# Dynamic Path Segment:
#   - Defined by a capture value, a variable name between angle brackets: <variable_name>

# Path Converters (str || int)
#   - Allows you to check if a dynamic segment is an integer or string
#   - Which then allows you to dynamically call urls based on the dynamic segment type
#   - Choose a path based on if the dynamic segment is an integer or string
#   - !int -> str, if the dynamic segment is not an integer then it is implied as a string
# if dynamic segment is a int it also get returned as a type int to the callback from views

urlpatterns = [
    path('<int:month>', views.monthlyChallengesInt),
    path('<str:month>', views.monthlyChallenges)
]

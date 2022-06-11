from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView


class RejestracjaUzytkownika(CreateView):
    model = User
    # template_name =
    form_class = UserCreationForm
    # success_url =

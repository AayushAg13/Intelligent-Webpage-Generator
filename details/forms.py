from . import models

class UserCreateForm(UserCreationForm):
    class Meta:
        model = models.ProfileDetails
        fields = "__all__"

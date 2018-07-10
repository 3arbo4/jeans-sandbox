from django.contrib.auth import get_user_model #returns user_model thats currently active
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

        # password1 and 2 come from the authorization user model
        class Meta:
            fields = ('username','email','password1','password2')
            model = get_user_model()

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = "Email Address"

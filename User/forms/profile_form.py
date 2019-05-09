from django.forms import ModelForm, widgets
from User.models import Profile
from Properties.models import Cities, Addresses



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
        #    'country': widgets.TextInput(attrs={'class': 'form-control'}),
         #   'zip': widgets.TextInput(attrs={'class': 'form-control'}),
          #  'city': widgets.TextInput(attrs={'class': 'form-control'}),
           # 'street': widgets.TextInput(attrs={'class': 'form-control'}),
            #'house_no': widgets.TextInput(attrs={'class': 'form-control'}),
            'snn': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
        }
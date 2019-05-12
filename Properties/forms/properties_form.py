from django.forms import ModelForm, widgets
from Properties.models import Properties


class CitiesForm(ModelForm):
    class Meta:
        model = Properties.address.Cities
        exclude = ['id']
        widgets = {
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class AddressesForm(ModelForm):
    class Meta:
        model = Properties.address
        exclude = ['id', 'Cities_id']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_no': widgets.TextInput(attrs={'class': 'form-control'})
        }


class TagsForm(ModelForm):
    class Meta:
        model = Properties.detail.T_ID
        exclude = ['id']
        widgets = {
            'elevator': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'garage': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'near_bloodbank': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'dungeon': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'seacret_entrence': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }


class TypesForm(ModelForm):
    class Meta:
        model = Properties.detail.Ty_ID
        exclude = ['id']
        widgets = {
            'description': widgets.CheckboxInput(attrs={'class': 'form-control'})
        }


class DetailsForm(ModelForm):
    class Meta:
        model = Properties.detail
        exclude = ['id', 'T_ID', 'Ty_ID']
        widgets = {
            'size': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'property_image': widgets.TextInput(attrs={'class': 'form-control'})
        }


class CreatePropertyForm:
    TagsForm()
    TypesForm()
    CitiesForm()
    AddressesForm()
    DetailsForm()

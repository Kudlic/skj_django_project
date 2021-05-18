from django import forms
from .models import Distributor, User, Game, Collectible, Game_instance, Collectible_instance, Offer

class UserForm(forms.ModelForm):
    description = forms.CharField(required= False, max_length=200)
    class Meta:
        model = User
        fields = ['name', 'description']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = []

class BadgeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(BadgeForm, self).__init__(*args, **kwargs)
        for i, stuffForField in enumerate(extra):
            self.fields['custom_%s' % i] = forms.ChoiceField(label=stuffForField[0], widget=forms.Select, choices=stuffForField[1])
   
    def extra_answers(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('custom_'):
                yield (self.fields[name].label, value)

class CollectibleForm(forms.ModelForm):
    class Meta:
        model = Collectible
        exclude = []

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['price']

class Collectible_instanceForm(forms.ModelForm):
    class Meta:
        model = Collectible_instance
        exclude = []

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True)

class RegisterForm(forms.Form):
    Options = (
        ('0.00','0.00'),
        ('5.00','5.00'),
        ('15.00','15.00'),
        ('50.00','50.00'),
     )
    username = forms.CharField(label ='Username')
    balance = forms.ChoiceField(label='Pick your starting balance', widget=forms.Select, choices=Options)

class StoreSearchForm(forms.Form):
    search = forms.CharField(label='', required=False)
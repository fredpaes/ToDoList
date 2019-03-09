from django.forms import ModelForm, TextInput, Textarea
from .models import List

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['item', 'location', 'cant', 'description']
        exclude = ['completed']
        widgets = {
            'item': TextInput(
                attrs={
                    'id': 'toDoAdd'
                }
            ),
            'description': Textarea(
                attrs={
                    'id': 'toDoDesc',
                    'class': 'materialize-textarea'
                }
            )
        }
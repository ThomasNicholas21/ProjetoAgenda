from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta: 
        # define qual model esse form se refere
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

        # permite definir atributos dentro de tags do forms
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder':'Escreva seu nome'
                }
            )
        }
    # pega os dados do formulário
    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            'first_name',
            ValidationError(
                'Erro',
                code='invalid'
            )
        )

        return super().clean()
    
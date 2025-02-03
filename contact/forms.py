from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Escreva seu primeiro nome'
            }
        ),
        label='Primeiro Nome',
    )

    class Meta: 
        # define qual model esse form se refere
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

        # permite definir atributos dentro de tags do forms
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder':'Escreva seu nome'
        #         }
        #     )
        # }
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


    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == '1':
            self.add_error(
                'first_name',
                ValidationError(
                    'Erro',
                    code='invalid'
                )
            )

        return first_name

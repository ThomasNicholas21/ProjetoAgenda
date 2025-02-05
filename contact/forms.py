from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Insira o primeiro nome'
            }
        ),
        label='Primeiro Nome',
    )
    
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Insira o segundo nome'
            }
        ),
        label='Segundo Nome',
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Insira o número de Telefone'
            }
        ),
        label='Telefone',
    )

    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Insira o e-mail'
            }
        ),
        label='E-mail',
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Insira a descrição.'
            }
        ),
        label='Descrição',
    )

    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    

    class Meta: 
        # define qual model esse form se refere
        model = Contact
        fields = (
            'first_name', 'last_name', 
            'phone', 'email', 
            'description', 'category',
            'picture'
            )

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
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg_first = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid'
                )
            msg_last = ValidationError(
                    'Segundo nome não pode ser igual ao segundo',
                    code='invalid'
                )
            
            self.add_error('first_name', msg_first)
            self.add_error('last_name', msg_last)

        return super().clean()


    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')

    #     if first_name == '1':
    #         self.add_error(
    #             'first_name',
    #             ValidationError(
    #                 'Erro',
    #                 code='invalid'
    #             )
    #         )

    #     return first_name

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu primeiro nome'
            }
        ),
        label='Nome'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu sobrenome'
            }
        ),
        label='Sobrenome'
    )
    
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu e-mail'
            }
        ),
        label='E-mail'
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 
            'email', 'username', 
            'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Já existe este e-mail',
                    code='invalid'
                )
            )

        return email
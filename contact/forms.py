from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="-------", 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Categoria'  
    )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False,
        label='Imagem'
    )
    

    class Meta: 
        # define qual model esse form se refere
        model = Contact
        fields = (
            'first_name', 'last_name', 
            'phone', 'email', 
            'description', 'category',
            'picture',
            )

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

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Insira seu primeiro nome'
            }
        ),
        label='Usuário'
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Insira sua senha'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
        label='Senha'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirme sua senha'
            }
        ),
        help_text='Use a mesma senha de antes',
        label='Confirme sua Senha'
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
    
class RegisterUpdteForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=1,
        max_length=20,
        required=True,
        help_text='Required',
        error_messages={
            'min_length': 'Add 1 latter to complete.'
        },
        label='Nome'
    )
    last_name = forms.CharField(
        min_length=1,
        max_length=20,
        required=True,
        help_text='Required',
        error_messages={
            'min_length': 'Add 1 latter to complete.'
        },
        label='Sobrenome'
    )
    password1 = forms.CharField(
        label='Senha',
        required=False,
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete':'new-password'
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Confirme sua Senha',
        required=False,
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete':'new-password'
        }),
        help_text='Use a mesma senha de antes'
    )
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 
            'email', 'username', 
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user =  super().save(commit=False)

        password = cleaned_data.get('password1')
        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user
    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2', 
                    ValidationError(
                        'As senhas devem ser iguais'
                    )
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'Já existe este e-mail',
                        code='invalid'
                    )
                )

        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as error:
                self.add_error(
                    'password1',
                    ValidationError(
                        error,
                        code='invalid'
                    )
                )

        return password1

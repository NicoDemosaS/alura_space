from django import forms 

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome do login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Ethan Wellick"
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua Senha"
            }
        )
    )

class CadastroForms(forms.Form):

    nome_cadastro = forms.CharField(
        label='Nome a Cadastrar',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Ethan Wellick",
            }
        )
    )

    email_cadastro = forms.EmailField(
        label='Nome a Cadastrar',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: EthanWellick@protonmail.com",
            }
        )
    )

    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua Senha"
            }
        )
    )

    senha_2 = forms.CharField(
        label='Confirme sua Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua Senha novamente"
            }
        )
    )
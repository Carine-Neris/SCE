from django import forms
from django.core.mail.message import EmailMessage
from django.core.mail import send_mail

from .models import Produto

from decouple import config

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    
    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}'
        de = config('EMAIL_HOST_USER')
        para = [config('EMAIL_HOST_USER'),]

        send_mail(
            assunto,
            conteudo,
            de,
            para,
            fail_silently=False,
        )   


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','estoque','imagem']
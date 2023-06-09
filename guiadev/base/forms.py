from django import forms


class TutorialForm(forms.Form):
    id = forms.CharField(max_length=20, required=False)
    like = forms.CharField(required=False)
    copy = forms.CharField(required=False)
    delete = forms.CharField(required=False)
    pesquisa = forms.CharField(max_length=500, required=False)
    email = forms.CharField(required=False)
    comentario = forms.CharField(max_length=500, required=False)
    sair = forms.CharField(max_length=20, required=False)
    email_destinatario = forms.CharField(max_length=500, required=False)


class LoginForm(forms.Form):
    login = forms.CharField(max_length=50, required=False)
    senha = forms.CharField(max_length=50, required=False)


class AdicionarTutorialForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=True)
    descricao = forms.CharField(max_length=1000, required=False)
    conteudos = forms.CharField(widget=forms.Textarea, required=False)
    conteudos_tipo = forms.CharField(widget=forms.Textarea, required=False)


class UsuarioForm(forms.Form):
    nome = forms.CharField(max_length=100, required=False)
    sobrenome = forms.CharField(max_length=1000, required=False)
    email = forms.CharField(widget=forms.Textarea, required=False)

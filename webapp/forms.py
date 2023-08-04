from django import forms
from .models import Materiales, Grupo, Marca, Proveedor, Unidad
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  


class MaterialesForm(forms.ModelForm):

    #https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
    
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Descripcion', 'style': 'width: 300px;', 'class': 'form-control'}))
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Precio', 'style': 'width: 200px;', 'class': 'form-control'}))
    grupo = forms.ModelChoiceField(queryset=Grupo.objects.all(), widget=forms.Select(attrs={ 'style': 'width: 150px;', 'class': 'form-control'}))
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), widget=forms.Select(attrs={ 'style': 'width: 150px;', 'class': 'form-control'}))
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), widget=forms.Select(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    unidad = forms.ModelChoiceField(queryset=Unidad.objects.all(), widget=forms.Select(attrs={ 'style': 'width: 150px;', 'class': 'form-control'}))



    class Meta:   
        model = Materiales
        fields = '__all__'



class GrupoForm(forms.ModelForm):
    categoria = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Categoria', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:   
        model = Grupo
        fields = '__all__'


class MarcaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nombre', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:   
        model = Marca
        fields = '__all__'

class UnidadForm(forms.ModelForm):
    unidad = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Unidad', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:   
        model = Unidad
        fields = '__all__'


class ProveedorForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 300px;', 'class': 'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Direccion', 'style': 'width: 300px;', 'class': 'form-control'}),required=False)
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'style': 'width: 300px;', 'class': 'form-control'}),required=False)
    telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Telefono', 'style': 'width: 300px;', 'class': 'form-control'}),required=False)
    vendedor = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Vendedor', 'style': 'width: 300px;', 'class': 'form-control'}),required=False)

    class Meta:   
        model = Proveedor
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'style': 'width: 400px;', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','style': 'width: 400px;' ,'name': 'password','placeholder':'Clave'}),label='Clave')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','style': 'width: 400px;' ,'name': 'renter_password','placeholder':'Reingrese la Clave'}),label='Reingrese la clave')

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  



""" class AccountSignInForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-Mail..'}), label='E-Mail')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password..'}), label='Password')

    class Meta:
        model = Account
        fields = ['email', 'password'] """





# https://stackoverflow.com/questions/48041375/django-select-a-valid-choice-that-choice-is-not-one-of-the-available-choices


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'style': 'width: 220px;'}),label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','style': 'width: 240px;' ,'name': 'renter_password','placeholder':'Clave'}),label='Clave')


                             
    




""" class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Usuario'
        self.fields['password'].label = 'Contraseña' """
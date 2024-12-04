from django import forms
from .models import Book,Student,Address,Student2,BookCover
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'edition': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'
        exclude = []
    name = forms.CharField(max_length=100,label='Name',required=True,widget=forms.TextInput())
    age = forms.IntegerField(initial=0,label='Age',required=True,widget=forms.NumberInput())
    adress=forms.ModelChoiceField(label='City',queryset=Address.objects.all(),required=True, widget=forms.Select())

class StudentForm2(forms.ModelForm):
    class Meta:
        model= Student2
        fields='__all__'
        exclude = []
    name = forms.CharField(max_length=100,label='Name',required=True,widget=forms.TextInput())
    age = forms.IntegerField(initial=0,label='Age',required=True,widget=forms.NumberInput())
    addresses=forms.ModelMultipleChoiceField(label='City',queryset=Address.objects.all(),required=True, widget=forms.CheckboxSelectMultiple())
    
class BookCoverForm(forms.ModelForm):
    class Meta:
        model= BookCover
        fields='__all__'
        exclude = []
    title = forms.CharField(max_length=100,label='Name',required=True,widget=forms.TextInput())
    coverPage = forms.ImageField(label='Cover Page',required=True,widget=forms.ClearableFileInput() )

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'password1', 'password2')
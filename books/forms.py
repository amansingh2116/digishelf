from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# Make sure this class is named UserRegistrationForm
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'price', 
                 'cover_image', 'genres', 'demo_pages', 'razorpay_link']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
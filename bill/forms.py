from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email Address'}))
    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your First Name'}))
    last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Last Name'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = 'User Name'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




#Create Add Record Form
from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ('S_No',)  # Exclude S_No field from the form as it's a primary key
        widgets = {
            'consignment_No': forms.TextInput(attrs={"placeholder": "consignment_No", "class": "form-control"}),
            # You may exclude the date field if it's set to auto_now_add
            # 'date': forms.TextInput(attrs={"placeholder": "date", "class": "form-control"}),
            'weight': forms.TextInput(attrs={"placeholder": "weight", "class": "form-control"}),
            'destination': forms.TextInput(attrs={"placeholder": "destination", "class": "form-control"}),
            'price': forms.TextInput(attrs={"placeholder": "price", "class": "form-control"}),
        }

    # You can include this method to exclude the date field if it's set to auto_now_add
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Check if the 'date' field is present in the form's fields
        if 'date' in self.fields:
            self.fields['date'].widget = forms.HiddenInput()

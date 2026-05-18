from django import forms
from django.core.validators import RegexValidator
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    phone = forms.CharField(
        required=False,
        validators=[RegexValidator(r"^[0-9+()\-\s]*$", "Enter a valid phone number.")],
        widget=forms.TextInput(
            attrs={
                "class": "form-field",
                "placeholder": "Doe",
            }
        ),
    )

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-field",
                    "placeholder": "John",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-field",
                    "placeholder": "john.doe@example.com",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-field",
                    "placeholder": "Select a discipline",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-field",
                    "placeholder": "Outline the parameters of your project...",
                    "rows": 4,
                }
            ),
        }

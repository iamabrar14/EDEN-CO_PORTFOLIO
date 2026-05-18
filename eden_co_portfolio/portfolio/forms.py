from django import forms
from django.core.validators import RegexValidator
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    phone = forms.CharField(
        required=False,
        validators=[RegexValidator(r"^[0-9+()\-\s]*$", "Enter a valid phone number.")],
        widget=forms.TextInput(
            attrs={
                "class": "w-full rounded-lg border border-emerald-200 px-4 py-3 focus:border-emerald-400 focus:ring-2 focus:ring-emerald-200",
                "placeholder": "Phone (optional)",
            }
        ),
    )

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full rounded-lg border border-emerald-200 px-4 py-3 focus:border-emerald-400 focus:ring-2 focus:ring-emerald-200",
                    "placeholder": "Your name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "w-full rounded-lg border border-emerald-200 px-4 py-3 focus:border-emerald-400 focus:ring-2 focus:ring-emerald-200",
                    "placeholder": "you@example.com",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "w-full rounded-lg border border-emerald-200 px-4 py-3 focus:border-emerald-400 focus:ring-2 focus:ring-emerald-200",
                    "placeholder": "Project inquiry",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "w-full rounded-lg border border-emerald-200 px-4 py-3 focus:border-emerald-400 focus:ring-2 focus:ring-emerald-200",
                    "placeholder": "Tell us about your project",
                    "rows": 6,
                }
            ),
        }

from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    """نموذج لإنشاء وتعديل المهمة."""

    class Meta:
        model = Task
        fields = ["icon", "icon_image", "title", "description", "completed"]
        widgets = {
            "icon": forms.TextInput(attrs={"placeholder": "رمز/إيموجي (مثال: ✅ أو 🔥)"}),
            "title": forms.TextInput(attrs={"placeholder": "عنوان المهمة"}),
            "description": forms.Textarea(attrs={"rows":3, "placeholder": "وصف المهمة (اختياري)"}),
        }


class UserRegisterForm(UserCreationForm):
    """نموذج تسجيل مستخدم جديد مع حقل البريد الإلكتروني اختياري."""

    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

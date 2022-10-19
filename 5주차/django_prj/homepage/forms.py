from django import forms
from .models import Coffee # Model 호출

# ModelFrom을 상속받는 CoffeeForm 생성
class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')
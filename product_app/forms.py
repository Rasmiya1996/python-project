from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from product_app.models import Login, Customer, Category, Item, Quantity_1, Review, Paymoney


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ("username","password1","password2",)
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ("user_1",)
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
class DateInput(forms.DateInput):
    input_type = 'date'

class ItemForm(forms.ModelForm):
    added_date = forms.DateField(widget=DateInput)
    class Meta:
        model= Item
        fields='__all__'
        exclude=("approval_status",)
class QuantityForm(forms.ModelForm):
    add_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Quantity_1
        fields = '__all__'
        exclude = ("item_1","customer_1","product_status")
class PaymoneyForm(forms.ModelForm):
    class Meta:
        model= Paymoney
        fields = "__all__"
        exclude = ("quantity_2",)

class ReviewForm(forms.ModelForm):

    class Meta:
        model= Review
        fields="__all__"
        exclude=("customer_2",)











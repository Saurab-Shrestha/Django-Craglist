from django import forms
from django.forms import fields, widgets, ModelForm
from .models import Editor,Todo
from ckeditor.widgets import CKEditorWidget


class EditorForm(forms.ModelForm):
    body = forms.CharField(widget = CKEditorWidget(), label = "Text Editor")
    
    class Meta:
        model = Editor
        fields = "__all__"



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"  # include all fields in form
        # fields = ("title",)  # include particular fileds of model in form

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input_field",
                "placeholder": "Enter task...",
            }
        ),
    )

    completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "form-check-input"}),
    )


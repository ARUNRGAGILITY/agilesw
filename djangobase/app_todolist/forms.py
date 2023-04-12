from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import *

class NewTodoListForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=NewTodoList.objects.all(), required=False)

    class Meta:
        model = NewTodoList
        fields = ['parent', 'title',  ]

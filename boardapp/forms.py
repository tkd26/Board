from django import forms
from .models import BoardModel
 

class BoardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(BoardForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['images'].required = False
    class Meta:
        model = BoardModel
        fields = ('title', 'content', 'author', 'images')
        # labels = {
        #     'name': '名前',
        #     'age': '年齢'
        # }
        # help_texts = {
        #     'name': '名前を入力',
        #     'age': '年齢を入力'
        # }
from django.forms import ModelForm

from bboard.models import Bb


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('name', 'content', 'price', 'rubric')

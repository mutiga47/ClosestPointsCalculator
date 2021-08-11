from django.forms import ModelForm
from .models import Points

class PointsForm(ModelForm):
    class Meta:
        model = Points
        fields = ['user_points']
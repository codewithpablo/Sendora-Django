from django.forms import ModelForm
from Apps.Motives.models import Motives

class NuevoMotivoForm(ModelForm):
    class Meta:
        model = Motives
        fields = "__all__"
        exclude = ["id"]
        
        
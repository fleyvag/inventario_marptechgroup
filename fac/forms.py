from django import forms

from .models import Cliente,envio

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['nombres','apellidos','tipo',
            'celular','estado']
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
class envioForm(forms.ModelForm):
    fecha_programada=forms.DateInput()
    fecha_revisada=forms.DateInput()
    class Meta:
        model=envio
        fields=['detalle','ncompra','condicionenvio','fecha_programada','fecha_revisada']
        exclude = ['um','fm','uc','fc']
    def __init__(self,*args,**kwargs):
        label={'condicionenvio':"condicion"}
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        
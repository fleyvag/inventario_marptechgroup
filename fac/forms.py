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
    class Meta:
        model=envio
        fields=['detalle','ncompra','condicion','fecha_programada','fecha_revisada']
        
        labels={'detalle':"detalle",
        'ncompra':"numero de compras",
        'condicion':"condicion",
        'fecha_programada':"fecha programada",
        'fecha_revisada':"fecha de recepcion",
        }
       

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            
        self.fields['fecha_programada'].required = True,
        self.fields['fecha_revisada'].widget.attrs['readonly']=True
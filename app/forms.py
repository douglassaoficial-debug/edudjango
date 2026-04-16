from django import forms
from .models import Curso, Avaliacao

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'nome',
            'carga_horaria',
            'nivel',
        ]

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = [
            'nome_aluno',
            'nome_curso',
            'nota',
            'comentario',
        ]

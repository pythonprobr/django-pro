from django.forms import ModelForm

from webdev.tarefas.models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']

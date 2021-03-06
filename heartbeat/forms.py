from core.forms import ModelForm
from .models import Host, Service, Inject, Task

class HostForm(ModelForm):
    redirect_url = 'system:all'
    class Meta:
        model = Host
        fields = [
            'team', 'ip', 'name', 'hostname', 'os'
        ]

class ServiceForm(ModelForm):
    redirect_url = 'system:all'
    hidden_fields = ['team']
    class Meta:
        model = Service
        fields = [
            'host', 'team', 'protocol', 'port', 'point_value'
        ]
        
class InjectForm(ModelForm):
    redirect_url = 'inject:all'
    class Meta:
        model = Inject
        fields = [
            'team', 'subject', 'details', 'available', 'deadline', 'point_value'
        ]
        
class TaskForm(ModelForm):
    redirect_url = 'task:all'
    class Meta:
        model = Task
        fields = [
            'team', 'point_value', 'details'
        ]
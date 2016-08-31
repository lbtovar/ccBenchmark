from django import forms
from .models import Control, Remediation


class ControlForm(forms.ModelForm):

    class Meta:
        model = Control
        fields = ('benchmark', 'section', 'doc_id', 'title', 'scored', 'profile', 'cci_number', 'description',
                  'rationale', 'audit', 'commands', 'remediation', 'impact', 'default', 'references')


class RemediationForm(forms.ModelForm):

    class Meta:
        model = Remediation
        fields = ('project', 'control', 'status', 'action', 'who', 'remediation_date')

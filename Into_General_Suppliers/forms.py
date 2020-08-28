from django.forms import ModelForm
from .models import message

class MessageSubmissionForm(ModelForm):
	class Meta:
		model = message
		fields = '__all__'

			
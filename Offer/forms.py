from django.forms import ModelForm, TextInput, Textarea

from .models import Offers_Mail


class Offers_MailForm(ModelForm):
	class Meta:
		model = Offers_Mail
		fields = ['m_address','m_text']

		widgets = {
		    "m_address": TextInput(attrs={
		    	'type': 'email',
		    	'class': 'form-control',
		    	'id':'exampleInputEmail1',
		    	'aria-describedby':'emailHelp',
		    	'placeholder': 'Ваш email для обратной связи'
		    	}),
		    "m_text": Textarea(attrs={
		    	'id':'crq_msg',
		    	'class':'form-control',
		    	'name':'crq_msg',
		    	'aria-required':'true',
		    	'aria-invalid':'true',
		    	'placeholder':'Ваш текст',
		    	'rows':'4',
		    	})
		}
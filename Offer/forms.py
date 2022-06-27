from django.forms import ModelForm

from .models import Offers_Mail


class Offers_MailForm(ModelForm):
	class Meta:
		model = Offers_Mail
		fields = ['m_address','m_text']
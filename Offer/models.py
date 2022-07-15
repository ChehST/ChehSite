from django.db import models

class Offers_Mail(models.Model):
    m_address = models.EmailField(max_length=32)
    m_text = models.TextField(max_length=320)
    m_datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    class Meta:
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'

    def __str__(self):
        return self.m_address

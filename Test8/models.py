from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
def email_validator(email):
    if not email.endswith('@djangotherightway.com'):
        raise ValidationError('email must end with @djangotherightway.com')

class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[email_validator])
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    age = models.IntegerField()

    def clean(self):
        if self.age < 18:
            if not self.phone_number:
                raise ValidationError('Age must be grater than 18')
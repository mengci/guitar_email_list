from django.db import models

# Create your models here.

class Email(models.Model):
	email_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200, null=True)
	source_type = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	created_date = models.DateTimeField('date published', auto_now=True)

	def __unicode__(self):
		return self.email

	class Meta:
		db_table = "emails"
		ordering = ["email_id"]


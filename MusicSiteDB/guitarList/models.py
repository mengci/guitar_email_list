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
		if self.email is None:
			return "NULL"
		else:
			return unicode(self.email) 
		

	class Meta:
		db_table = "emails"
		ordering = ["email_id"]

class Tag(models.Model):
	tag_id = models.AutoField(primary_key = True)
	tag_name = models.CharField(max_length = 200)
	tag_count = models.IntegerField(default = 0)


	class Meta:
		db_table = "tags"
		ordering = ["tag_id"]

class Image(models.Model):
	image_id = models.AutoField(primary_key = True)
	image_name = models.CharField(max_length = 200)
	tag_index = models.CharField(max_length = 800,null = True)

	class Meta:
		db_table = "images"
		ordering = ["image_id"]

 
	


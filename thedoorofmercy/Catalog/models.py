from django.db import models

# Create your models here.
class Sermon(models.Model):
	sermon_id = models.BigAutoField(primary_key=True,unique=True)
	sermon_title = models.CharField(max_length=100, blank=False, null=False)
	sermon_upload_date = models.DateTimeField(null=False)
	sermon_description = models.CharField(max_length=1000,null=False)
	sermon_content = models.CharField(max_length=20000,null=False)
	sermon_author = models.CharField(max_length=70,null=False)
	sermon_location = models.CharField(max_length=70,null=True)

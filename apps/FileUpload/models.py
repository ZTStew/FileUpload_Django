from django.db import models

# Create your models here.
class Document(models.Model):
    uploader = models.CharField(max_length=255, default='')
    # ROOT: /'Project_Name'
    docfile = models.FileField(upload_to='apps/FileUpload/documents/')
    file_Name = models.CharField(max_length=255, default='')
    file_Extension = models.CharField(max_length=255, default='')
    # Sets destination folder for file being uploaded
    # document = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


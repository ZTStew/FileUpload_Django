from django.db import models

# Create your models here.
class Document(models.Model):
    # Sets destination folder for file being uploaded
    # ROOT: /'Project_Name'
    docfile = models.FileField(upload_to='apps/FileUpload/documents/')
    # print(docfile.__dict__)
    # print(docfile.name)
    # fileName = docfile.name
    # print(fileName)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

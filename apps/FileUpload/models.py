from django.db import models

# class DocValidator(models.Manager):
#     def docValidate(self, form_data):
#         # errors = []

#         userName = "TempUser"
#         fileName = "TempFile"
#         docFile = "TempDocFile"

#         doc = Document.objects.create(
#             userName = userName,
#             fileName = fileName,
#             document = docFile,

#         )
#         return (True, doc)

# Create your models here.
class Document(models.Model):
    # ROOT: /'Project_Name'
    docfile = models.FileField(upload_to='apps/FileUpload/documents/')
    # Sets destination folder for file being uploaded
    # document = models.CharField(max_length=255)
    # uploader = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # print(docfile.__dict__)
    # print(docfile.name)
    # fileName = docfile.name
    # print(fileName)
    # return True

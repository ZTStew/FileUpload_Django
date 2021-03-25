from django.shortcuts import render, redirect
from apps.Login_Register.models import User
from .models import Document
from django.contrib import messages
from .forms import DocumentForm

# Create your views here.
def dashboard(request):

    # form = DocumentForm()
    # Load documents for the list page
    # documents = Document.objects.all()

    # results = User.objects.log(request.POST)
    # test = User.report
    
    # print(User.objects.get(pk=request.session["user_id"]).user_name)


    # prints values in session
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))

    # for key in request.session.keys():
    #     print("key:=>" + request.session[key])

    # Render list page with the documents and the form
    # context = {'documents': Document.objects.all()}
    context = {'documents': Document.objects.all()}

    # print(context)

    return render(request, "FileUpload/dashboard.html", context)
    # return render(request, "FileUpload/dashboard.html")

def fileupload(request):
    if not "user_id" in request.session:
        print("ERROR <fileupload>: user not logged in")
        return(redirect("/dashboard"))

    message = ""
    # Handle File Upload
    # if a POST request has been placed...
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():


            # Validates file information to make sure that the file has a name and an extension
            # Splits given file at '.'
            fileParts = request.FILES['docfile'].name.split('.')
            fileName = ""
            fileExtension = ""

            # Handles when the file does and does not have an extension
            if len(fileParts) > 1:
                # creates fileName
                for i in  range(len(fileParts) - 1):
                    # Readds '.' to 'fileName'
                    if i > 0:
                        fileName += "."
                    # Builds 'fileName'
                    fileName += fileParts[i]

                # Assigns 'fileExtension' the value of the last index of the file to protect against files that have stacked extensions
                fileExtension = "." + fileParts[len(fileParts) - 1]

            else:
                # sets 'fileName' to the value of 'fileParts'
                fileName = fileParts[0]
                # Assigns default value for 'fileExtension'
                fileExtension = "N/A"

            print("fileName: " + fileName)
            print("fileExtension: " + fileExtension)

            newdoc = Document(docfile=request.FILES['docfile'])
            # print(newdoc.__dir__())
            # print(newdoc.name)
                # , uploader=User.objects.get(pk=request.session["user_id"]).user_name)
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('file_upload')
        else:
            message = "ERROR: "
    else:
        form = DocumentForm() # Empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    # print(documents[0].__dict__)

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'FileUpload/list.html', context)
    # return render(request, 'FileUpload/list.html')

    # if "user_id" not in request.session:
        # return(redirect("/ln"))
    # return render(request, "FileUpload/dashboard.html")

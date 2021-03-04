from django.shortcuts import render, redirect
from apps.Login_Register.models import User
from django.contrib import messages
from .models import Document
from .forms import DocumentForm

# Create your views here.
def dashboard(request):

    # form = DocumentForm()
    # Load documents for the list page
    # documents = Document.objects.all()
    # shows properties of documents
    # print(documents[0].__dict__)

    # Render list page with the documents and the form
    context = {'documents': Document.objects.all()}

    return render(request, "FileUpload/dashboard.html", context)

def fileupload(request):
    message = ""
    # Handle File Upload
    # if a POST request has been placed...
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        # docfile=request.FILES['docfile']
        # print("")
        # # print(request.FILES['docfile'].__dict__)
        # print(docfile.__dict__)
        # print(docfile.name)
        # print("")

        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            # newdoc.add_heading({"fileNm": title})
            # print("")
            # print(newdoc.core_properties)
            # print(newdoc.__dict__)
            # print("")
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('file_upload')
        else:
            message = "ERROR: "
    else:
        form = DocumentForm() # Empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message':message}
    return render(request, 'FileUpload/list.html', context)




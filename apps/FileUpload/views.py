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

    # results = User.objects.log(request.POST)
    # test = User.report
    
    print(User.objects.get(pk=request.session["user_id"]).user_name)


    # prints values in session
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))

    # for key in request.session.keys():
    #     print("key:=>" + request.session[key])

    # Render list page with the documents and the form
    context = {'documents': Document.objects.all()}

    return render(request, "FileUpload/dashboard.html", context)

def fileupload(request):
    if not "user_id" in request.session:
        print("ERROR: fileupload, Unlogged in user")
        return(redirect("/dashboard"))

    message = ""
    # Handle File Upload
    # if a POST request has been placed...
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
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
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'FileUpload/list.html', context)

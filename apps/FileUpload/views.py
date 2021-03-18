from django.shortcuts import render, redirect
from apps.Login_Register.models import User
from django.contrib import messages

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

    # return render(request, "FileUpload/dashboard.html", context)
    return render(request, "FileUpload/dashboard.html")

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

            # creates 'Document' object
            newdoc = Document(docfile=request.FILES['docfile'])
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

    # if "user_id" not in request.session:
        # return(redirect("/ln"))
    return render(request, "FileUpload/dashboard.html")

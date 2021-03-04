import os

# clears 'documents' folder of all files each time the server starts
folder = "./apps/FileUpload/documents"

for file in os.listdir(folder):
    # if not file.endswith
    print("File: " + file + " removed")
    os.remove(os.path.join(folder, file))


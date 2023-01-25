def handle_uploaded_file(f):
    filename = f.name
    with open('uploaded_files/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

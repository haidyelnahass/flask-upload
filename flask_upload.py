from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def uploadfile():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save('uploads/' + file.filename)
        return 'File uploaded successfully'

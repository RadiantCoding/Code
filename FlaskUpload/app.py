from flask import Flask

#this is where you will be uploading the file to
UPLOAD_FOLDER = "C:\\Users\\barry\\PycharmProjects\\ProjectVideos\\FlaskWebServers\\uploads"

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
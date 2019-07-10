from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__, upload_folder="/Users/xi/Desktop/images", static_folder="images")
app.config['MONGO_URI'] = 'mongodb://localhost:27017/localTest'
mongo = PyMongo(app)


@app.route('/')
def index():
    return '''
        <form method="POST" action="/upload" enctype="multipart/form-data">
            <input type="text" name="username">
            <input type="file" name="image_file">
            <input type="submit">
        </form>
    '''


@app.route('/upload', methods=["POST"])
def upload():
    f = request.files['image_file']
    f.save("/Users/xi/Desktop/images/" + f.filename)
    return "Done!"


@app.route('/load/<path:filename>')
def load(filename):
    return f'''
        <img src="/Users/xi/Desktop/images/{filename}">
    '''


# if __name__ == '__main__':
#     app.run(debug=True)

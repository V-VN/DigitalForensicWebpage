from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__, static_folder='static')
# app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

@app.route('/main')
def main():
    return render_template('index.html')

def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "File has been uploaded."    
    # return render_template('index.html', form=form)
    # return render_template('index_edit.html', form=form)
    return render_template('index_2.html', form=form)


@app.route('/login')
def login():
    return render_template('index_login.html')

@app.route('/register')
def register():
    return render_template('index_register.html')
 
@app.route('/report')
def report():
    return render_template('index_pdf.html')

if __name__ == '__main__':
    app.run(debug=True)

# this is the main one 
# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import FileField, SubmitField
# from werkzeug.utils import secure_filename
# import os
# from wtforms.validators import InputRequired

# app = Flask(__name__, static_folder='static')
# # app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# app.config['TEMPLATES_AUTO_RELOAD'] = True

# app.config['SECRET_KEY'] = 'supersecretkey'
# app.config['UPLOAD_FOLDER'] = 'static/files'

# class UploadFileForm(FlaskForm):
#     file = FileField("File", validators=[InputRequired()])
#     submit = SubmitField("Upload File")

# @app.route('/', methods=['GET', 'POST'])

# @app.route('/main')
# def main():
#     return render_template('index.html')

# @app.route('/login')
# def login():
#     return render_template('index_login.html')

# @app.route('/home', methods=['GET', 'POST'])
# def home():
#     form = UploadFileForm()
#     if form.validate_on_submit():
#         file = form.file.data
#         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
#         return "File has been uploaded."    
#     # return render_template('index.html', form=form)
#     # return render_template('index_edit.html', form=form)
#     return render_template('index_2.html', form=form)

# @app.route('/register')
# def register():
#     return render_template('index_register.html')
 
# @app.route('/report')
# def report():
#     return render_template('index_pdf.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# # this is the main one 

import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired

app = Flask(__name__, static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Optional: You can include a secret key for form security if needed
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

# Ensure the upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET', 'POST'])
@app.route('/main', methods=['GET', 'POST'])  # Ensure both routes handle GET and POST
def main_redirect():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('index_login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        if filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded', 'success')
        except Exception as e:
            flash(f'File upload failed: {e}', 'error')
            return redirect(request.url)
        return redirect(url_for('home'))
    return render_template('index_2.html', form=form)

@app.route('/register')
def register():
    return render_template('index_register.html')

@app.route('/report')
def report():
    return render_template('index_pdf.html')

if __name__ == '__main__':
    app.run(debug=True)

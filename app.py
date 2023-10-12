import os
import requests

from flask import Flask, jsonify, render_template, redirect, request, send_from_directory, session, url_for
from dotenv import load_dotenv
  
app = Flask(__name__)  
  
UPLOAD_FOLDER = 'static/uploads/'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  
  
@app.route('/')  
def upload_form():
    return render_template('upload.html')  
  
@app.route('/', methods=['POST'])  
def predict():  
    if 'file' not in request.files:  
        return jsonify({'error': 'No file part in the request'}), 400  
    file = request.files['file']  
    if file.filename == '':  
        return jsonify({'error': 'No file selected for uploading'}), 400  
  
    filename = file.filename  
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  
    file.save(file_path)

    # Store the filename in the session  
    session['filename'] = filename

    # Load the environment variables
    load_dotenv()

    # TO DO 
    # Call the Prediction API of the color classification model, this application requires a json
    # response from the model named color_prediction..
    


    # TO DO 
    # Call the Prediction API of the make classification model, this application requires a json
    # response from the model named make_prediction..



  
    return render_template('result.html', filename=filename, color_prediction=color_prediction, make_prediction=make_prediction)  
  
@app.route('/uploads/<filename>')  
def send_file(filename):  
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/reset', methods=['GET'])    
def reset(): 
    if 'filename' in session:    
        try:  
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], session['filename']))    
            session.pop('filename', None)
            print("Previous image deleted.")
        except Exception as e:  
            print("Error: unable to delete file: %s" % str(e))  
    return redirect(url_for('upload_form'))   

if __name__ == '__main__':  
    app.run(debug=True)  

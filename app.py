from flask import Flask, render_template, request
import os
from utils import model_predict

# ✅ Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')

# ✅ Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')

# ✅ Route for Prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        basepath = os.path.dirname(__file__)
        upload_dir = os.path.join(basepath, 'static', 'uploads')
        os.makedirs(upload_dir, exist_ok=True)  # ✅ Ensure uploads folder exists
        upload_path = os.path.join(upload_dir, file.filename)
        file.save(upload_path)

        # Call prediction function from utils.py
        result = model_predict(upload_path)

        return render_template('result.html', result=result, filename=file.filename)

# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True)

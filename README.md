🧬 Hematovision: Blood Cell Classification with Deep Learning
Hematovision is a deep learning–powered web application that classifies blood cell images using transfer learning. This project is designed to assist in the identification of blood cell types from microscopic images using a trained Convolutional Neural Network (CNN), built and served through a user-friendly Flask interface.

🔬 Project Overview
This project uses a pre-trained model (.h5) based on transfer learning to classify uploaded blood cell images into different categories such as:

1.LYMPHOCYTE

2.BASOPHIL

3.EOSINOPHIL

4.NEUTROPHIL

The primary goal is to demonstrate the use of AI in assisting healthcare professionals with diagnostic tasks.

📁 Project Structure
csharp
Copy code
hematovision/
├── app.py                     # Main Flask application
├── utils.py                   # Contains prediction logic
├── hematovision_model.h5      # Pre-trained model file
├── requirements.txt           # Required Python packages
├── static/
│   └── uploads/               # Stores uploaded images
├── templates/
│   ├── home.html              # File upload interface
│   └── result.html            # Displays prediction result
├── README.md                  # Project documentation
└── other supporting files...
🌐 How It Works
User uploads a blood cell image on the web interface.

The image is processed and passed through the pre-trained CNN model.

The model predicts the type of blood cell.

The result is displayed to the user with the uploaded image and predicted label.

⚙️ Technologies Used
Python

Flask (Web Framework)

TensorFlow / Keras (for model and transfer learning)

HTML, CSS (for frontend)

Bootstrap (optional for styling)

🚀 How to Run the Project
Clone the repository:

#bash
Copy code
git clone https://github.com/your-username/hematovision-blood-cells-classification.git
cd hematovision-blood-cells-classification
Install dependencies:

#bash
Copy code
pip install -r requirements.txt
Run the Flask app:

#bash
Copy code
python app.py
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000/
📸 Demo
🔽 Upload a blood cell image and click "Predict" to see the result instantly!


📝 Future Enhancements
*Improve UI/UX design using CSS/Bootstrap

*Add additional cell types

*Integrate model evaluation metrics

*Support drag & drop uploads

🤝 Contributions
Contributions are welcome! If you’d like to improve this project, feel free to fork the repo and submit a pull request.

📧 Contact
If you have any questions or feedback, feel free to contact me at:
📬 arungolamchandhana@gmail.com

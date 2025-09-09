# Mcqs-Generation-App-Using-LLM
📘 MCQ Generator App  A simple Streamlit web application that generates Multiple Choice Questions (MCQs) using Google Gemini (Generative AI). This app allows users to select a subject and instantly generate a set of MCQs with answers, making it useful for students, teachers, and exam preparation.
.

🚀 Features

✅ Generate 3 MCQs per request

✅ Subjects supported: Physics, Chemistry, Biology, Mathematics, Computer Science, Graph Theory, Number Theory

✅ Clear answer marking for each question

✅ Simple & interactive Streamlit UI

🛠️ Tech Stack

Python

Streamlit (Frontend)

Google Generative AI (Gemini 1.5 Flash)

📂 Project Structure
├── app.py              # Main Streamlit app  
├── requirements.txt    # Dependencies  
└── README.md           # Project description  

⚙️ Installation & Setup

Clone the repository:

git clone https://github.com/your-username/mcq-generator-app.git
cd mcq-generator-app


Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Linux/Mac  
venv\Scripts\activate     # On Windows  


Install dependencies:

pip install -r requirements.txt


Add your Google API key in app.py:

os.environ["GOOGLE_API_KEY"] = "your_api_key_here"


Run the app:

streamlit run app.py


Open in browser at:

http://localhost:8501

📸 Screenshot

<img width="876" height="747" alt="image" src="https://github.com/user-attachments/assets/5a3b05cf-54fe-4604-8cf9-0dcbc6a8c748" />

💡 Future Improvements

 Add option to choose the number of questions

 Support exporting MCQs to PDF/CSV

 Add difficulty level selection (Easy/Medium/Hard)

 Allow uploading custom topics




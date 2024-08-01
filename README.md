Overview
This is a web application designed to correct grammatical errors in text. It uses Flask for the backend, Gramformer for grammar correction, and Flet for the frontend. Users can input text into the app, which will then be checked and corrected, adhering to a 300-word limit.

Features
Flask Backend: Handles text correction requests.
Gramformer: Provides grammatical correction functionality.
Flet Frontend: User-friendly interface for text input and output.
Word Limit: Texts exceeding 300 words are flagged.

Installation
Clone the repository:
git clone https://github.com/your-username/grammar-checker-app.git
cd grammar-checker-app

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the dependencies:
pip install -r requirements.txt

Run the Flask server:
python app.py

Run the Flet frontend:
python flet_app.py

Usage
Open your browser and navigate to http://localhost:5000 to access the grammar checking interface.
Enter text into the provided field and click "Submit" to receive corrected text

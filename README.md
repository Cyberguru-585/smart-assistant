
Smart Multi-Domain Assistant

##  Overview
This project is an intelligent multi-domain assistant that can understand user intent and route queries to different modules such as chatbot and recommendation systems.

It is designed with a modular and scalable architecture, making it easy to extend to multiple domains.



##  Features
-  Intent Detection using Machine Learning (TF-IDF + Logistic Regression)
-  Intelligent Routing System
-  Chatbot for general conversations
-  Movie Recommendation System
-  FastAPI Backend (REST API)
-  Streamlit UI (Interactive Chat Interface)
-  Modular and scalable architecture



## Architecture
User Input ↓ Intent Detection (ML Model) ↓ Router (Decision Layer) ↓ Module (Chatbot / Recommender) ↓ Response to User



## Project Structure
project/ │ ├── api/               # FastAPI backend ├── core/              # Routing logic ├── modules/           # Chatbot & recommender ├── models/            # Trained ML models (.pkl) ├── ui/                # Streamlit UI ├── train_model.py     # Model training script ├── README.md └── requirements.txt



### How to Run

### 1 Install dependencies
```bash
pip install -r requirements.txt

2 Train model
Bash
python train_model.py

3️ Run backend (API)
Bash
python -m uvicorn api.app_api:app --reload

4️ Run frontend (UI)
Bash
streamlit run ui/ui.py


### Example Inputs
"hi"
"recommend movie"
"action"
"hello"

### Technologies Used
Python
FastAPI
Streamlit
Scikit-learn
Uvicorn

### Future Improvements
Add multi-domain support (music, news, etc.)
Improve ML model accuracy
Add user context memory
Deploy on cloud (Render / AWS)


TechStax Developer Assessment
Project Overview :-

This project implements a full-stack GitHub webhook system that:
Listens to GitHub events (Push, Pull Request, Merge)
Stores event data in MongoDB
Displays repository activity in a React UI
Polls backend every 15 seconds to show latest updates
The system demonstrates end-to-end integration between GitHub Webhooks, Flask backend, MongoDB database, and a React frontend.

Architecture :-

GitHub (action-repo)
        ↓ Webhook
Flask Backend (/webhook)
        ↓
MongoDB Atlas
        ↓
React Frontend (Polling every 15 sec)

Tech Stack :-

Backend:-
Python 
Flask
MongoDB Atlas
Flask-CORS
GitHub Webhooks

Frontend :-
React (Vite)
Axios

Project Structure :-

TechStax-Assessment/
│
├── frontend/              # React application
│   ├── src/
│   ├── package.json
│
├── webhook-repo/          # Flask backend
│   ├── app.py
│   ├── requirements.txt
│
└── README.md


Backend Setup (Flask) :-

1️. Clone Repository
git clone https://github.com/yourusername/TechStax-Assessment.git
cd TechStax-Assessment/webhook-repo

2️. Create Virtual Environment
python -m venv venv

Activate:

Windows (PowerShell)
.\venv\Scripts\activate
Windows (CMD)
venv\Scripts\activate.bat

3️. Install Dependencies
pip install -r requirements.txt

4️. Create Environment Variables

Create a .env file inside webhook-repo:

MONGO_URI=your_mongodb_connection_string

Note: .env is intentionally not included in the repository for security reasons.

5️. Run Backend
python app.py

Server runs at:

http://localhost:5000


Frontend Setup (React) :-

1. Open a new terminal:

cd TechStax-Assessment/frontend

2. Install dependencies:

npm install

3. Run development server:

npm run dev

4. Frontend runs at:

http://localhost:5173


GitHub Webhook Configuration (For Local Testing) :-

1. Start backend (python app.py)

2. Run ngrok:

ngrok http 5000

3. Copy HTTPS URL

4. Go to GitHub → Repository Settings → Webhooks

5. Add webhook:

https://your-ngrok-url/webhook

Content type:

application/json

Select events:

Push

Pull request
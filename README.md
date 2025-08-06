# 🏫 Basti Ki Pathshala - Django Web Application

A Django-based web application designed for **user registration, login, and profile management**, built with Bootstrap for a clean and responsive UI.  
This project is inspired by **Basti Ki Pathshala Foundation**, which provides education and support for children in underserved communities.

---

## ✨ Features
- 🔑 **User Authentication** (Signup, Login, Logout with sessions)
- 🖼 **Profile Display** (Name, Email, Phone, Profile Picture)
- 🔒 **Password Hashing** (Secure password storage using Django's built-in utilities)
- 🎨 **Bootstrap UI** (Responsive design with soft warm theme)
- 📄 **Focus Area Table** (Dynamic info displayed using Bootstrap tables)
- ✅ **CSRF Protection** (Django default)
- 🌐 **Session Management** (User data stored in session for persistence)

---

## 📂 Project Structure
basti_ki_pathshala/
│
├── homepage/ # Homepage app
│ ├── views.py # Homepage view logic
│ ├── templates/ # HTML templates
│
├── login/ # Login & Signup app
│ ├── models.py # Application model (User data)
│ ├── views.py # Login and signup logic
│
├── static/ # Static assets (CSS, JS, images, logo)
│
├── basti_ki_pathshala/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│
├── db.sqlite3 # SQLite database (default)
├── manage.py
└── README.md

---

## 🛠 Tech Stack
- **Backend**: Django (Python 3.10+)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (default)  
- **Session Auth**: Django session-based authentication  

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/basti-ki-pathshala.git
cd basti-ki-pathshala
2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the Development Server
python manage.py runserver
👤 Default User Workflow
Sign up → Create a new account.

Login → Access homepage (profile displayed).

Profile Info → View details fetched from session.

Logout → End session.

🔒 Security
Passwords are hashed before saving in DB.

Sessions used for secure authentication.

CSRF tokens protect against cross-site attacks.

📸 Screenshots
<img width="1366" height="768" alt="Screenshot (219)" src="https://github.com/user-attachments/assets/9a149ffe-c585-4b48-8d0e-5337899b4472" />
<img width="1366" height="768" alt="Screenshot (218)" src="https://github.com/user-attachments/assets/4fc2e892-865a-4188-9536-642681c08a7a" />
<img width="1366" height="768" alt="Screenshot (217)" src="https://github.com/user-attachments/assets/7e965236-6497-4e93-b3da-76e4c80c087e" />
<img width="1366" height="768" alt="Screenshot (220)" src="https://github.com/user-attachments/assets/4399aab5-b80d-4e90-8f7b-41ff9c79cf11" />

🤝 Contributing
Feel free to fork, modify, and submit PRs to improve this project!

👨‍💻 Author
Vruk (Developer)
📧 Email: developeryuvrajsirganor@gmail.com
🔗 GitHub: xVrukx

## <h1 align="center">Rise of Hablu — Personal Growth & Productivity Platform</h1>

A comprehensive **Rise of Hablu — Personal Growth & Productivity Platform** that helps users track and enhance multiple areas of life including academics, careers, entertainment, personal skills, and self-improvement.

---

## ✨ **Project Overview**

This project integrates multiple modules through a clean **REST API backend** using **Django Rest Framework** and a simple **Frontend interface** using **Django templates (HTML, CSS)**.

It uses **SQLite3** as the default lightweight database.

## 🛠️ **Tech Stack**

* **Backend**

  * Python 3.x
  * Django
  * Django Rest Framework

* **Frontend**

  * Django Templates
  * HTML, CSS (Vanilla)
  * JavaScript 

* **Database**

  * SQLite3 (default Django database)

## **Features (Modules / APIs Built)**

1. **Subject Grade Tracker** 
   Track academic subject grades.
   
   URL: `/api/subjectgrades/`

2. **Job Tracker** 
   Manage job applications and opportunities.
   
   URL: `/api/jobs/`

3. **Movie Recommender** 
   Track movies to watch.
   
   URL: `/api/movies/`

4. **Fun Fact Logger** 
   Store interesting fun facts.
   
   URL: `/api/funfacts/`

5. **Study Group Planner** 
   Organize and plan group study sessions.
   
   URL: `/api/studygroups/`

6. **Hero Dashboard** 
   Track personal development metrics (like level, XP, etc.).

   URL: `/api/herodashboard/`

7. **Learn New Skills** 
   Track new skills to learn and related resources.
   
   URL: `/api/learnskills/`

8. **Dress Better** 
   Organize outfit ideas and style tips.
   
   URL: `/api/dressbetter/`

9. **Chatbot** 
   Interactive chatbot to assist with dashboard tasks.

   URL: `/api/chatbot/`

---

## 📂 **API Root URL**

```json
{
    "subjectgrades": "http://127.0.0.1:8000/api/subjectgrades/",
    "learnskills": "http://127.0.0.1:8000/api/learnskills/",
    "dressbetter": "http://127.0.0.1:8000/api/dressbetter/",
    "jobs": "http://127.0.0.1:8000/api/jobs/",
    "movies": "http://127.0.0.1:8000/api/movies/",
    "funfacts": "http://127.0.0.1:8000/api/funfacts/",
    "studygroups": "http://127.0.0.1:8000/api/studygroups/",
    "herodashboard": "http://127.0.0.1:8000/api/herodashboard/"
}
```

---

##  **Setup Instructions**

1️⃣ **Clone Repository**

```
git clone <repo-url>
cd <project-directory>
```

2️⃣ **Create Virtual Environment and Install Dependencies**

```
python -m venv env
source env/bin/activate  # (Linux/macOS)
# OR
env\Scripts\activate    # (Windows)

pip install -r requirements.txt
```

3️⃣ **Run Migrations**

```
python manage.py makemigrations
python manage.py migrate
```

4️⃣ **Run Server**

```
python manage.py runserver
```

5️⃣ **Access the app**

* Backend APIs: `http://127.0.0.1:8000/api/`
* Frontend Templates: Visit root `http://127.0.0.1:8000/`

---

## 🤝 **Contributors**

* Md Rakibul Hassan
* Dipa Barua
* MD Tahsin Azad Shaikat
* Sabikun Nahar Nova

---

## 📌 **Future Work**

* Integrate fully functional **Chatbot** module
* Improve frontend UI/UX design
* Add user authentication and authorization (Login/Signup)

---

> **Thank you!** ✨
> This project aims to help individuals organize, grow, and improve themselves across various life domains easily and interactively.

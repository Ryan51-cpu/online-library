# 📚 Online Library

A Django web app that allows users to browse, review, and rate books. Users can register, log in, and leave reviews — making it a simple, interactive library system.

🧠 Features

✅ User registration & login/logout ✅ Browse all available books ✅ Filter books by category ✅ Search books by title or author ✅ View book details, description, and cover ✅ Add reviews & star ratings (1–5) ✅ Dynamic average rating calculation ✅ Clean responsive UI with TailwindCSS

# ⚙️ Technologies Used

Python 3

Django 5

SQLite3 (default database)

TailwindCSS (CDN version)

HTML / CSS (Jinja templates)

# 🚀 How to Run the Project

## Clone or download this project:

git clone https://github.com/Ryan51-cpu/online-library.git cd online-library

## Create and activate a virtual environment:

python -m venv env source env/bin/activate # on macOS/Linux env\Scripts\activate # on Windows

## Install dependencies:

pip install django

## Run migrations:

python manage.py migrate

## Create a superuser (if you want to add/remove books):

python manage.py createsuperuser

## Run the development server:

python manage.py runserver

Open the app in your browser:

👉 http://127.0.0.1:8000/

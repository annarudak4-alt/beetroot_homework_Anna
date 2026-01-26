from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)

# Конфігурація бази даних SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# --- МОДЕЛІ ---

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # Зв'язок: одна категорія має багато нотаток
    notes = db.relationship('Note', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.title}>'

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    reminder = db.Column(db.DateTime, nullable=True)
    # Зовнішній ключ на таблицю категорій
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    def __repr__(self):
        return f'<Note {self.title}>'

# --- VIEW ---

@app.route("/")
def index():
    # Отримуємо всі нотатки з бази даних
    notes = Note.query.all()
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)

with app.app_context():
    db.create_all()
    print("База даних успішно створена або вже існує!")
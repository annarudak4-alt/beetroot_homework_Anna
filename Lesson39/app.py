from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Тестові дані (нотатки)
    notes = [
        {"title": "Плани", "text": "Відвідати тренування, зробити покупки, читання"},
        {"title": "Домашні справи", "text": "Прання, посуд, винести сміття"},
        {"title": "Нагадування", "text": "Оплатити комунальні платежі"}
    ]

    # Передаємо нотатки у шаблон
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)
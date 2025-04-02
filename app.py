from flask import Flask, render_template, send_from_directory
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.datetime.now()
    return render_template(
        "index.html",
        current_time=now.strftime("%H:%M:%S"),
        current_year=now.year
    )

# Новый маршрут для отображения кода
@app.route("/show_code")
def show_code():
    # Получаем путь к текущему файлу
    file_path = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(file_path, "app.py", mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
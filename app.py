from dotenv import load_dotenv
load_dotenv()

import os
import psycopg2
from flask import Flask, render_template, request, redirect

REQUIRED_VARS = ["DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD"]

app = Flask(__name__)


def get_conn():
    missing = [v for v in REQUIRED_VARS if not os.environ.get(v)]
    if missing:
        raise RuntimeError("Missing environment variables: " + ", ".join(missing))
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        connect_timeout=3,
    )


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS notes "
        "(id SERIAL PRIMARY KEY, text TEXT NOT NULL)"
    )
    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT text FROM notes ORDER BY id DESC")
    notes = [row[0] for row in cur.fetchall()]
    conn.close()
    return render_template("index.html", notes=notes)


@app.route("/notes", methods=["POST"])
def add_note():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (text) VALUES (%s)", (request.form["text"],))
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/health")
def health():
    try:
        get_conn().close()
        return {"status": "ok", "database": "up"}, 200
    except Exception:
        return {"status": "unhealthy", "database": "down"}, 503


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
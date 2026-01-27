from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import re
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

SENDER_EMAIL = "limaone09@gmail.com"
SENDER_PASSWORD = "groerwepfyhyykty"

def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def run_topsis(input_file, weights, impacts, output_file):
    data = pd.read_csv(input_file)
    criteria = data.iloc[:, 1:].astype(float)

    weights = np.array(weights, dtype=float)
    impacts = np.array(impacts)

    norm = np.sqrt((criteria ** 2).sum())
    normalized = criteria / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    d_pos = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_neg = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = d_neg / (d_pos + d_neg)
    data["Topsis Score"] = score
    data["Rank"] = data["Topsis Score"].rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)


def send_email(receiver_email, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result File"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg.set_content("Please find the TOPSIS result file attached.")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="csv",
            filename="result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        weights = request.form.get("weights", "").split(",")
        impacts = request.form.get("impacts", "").split(",")
        email = request.form.get("email", "")

        if not file:
            return "Error: No file uploaded"

        if len(weights) != len(impacts):
            return "Error: Number of weights must be equal to number of impacts"

        for i in impacts:
            if i not in ['+', '-']:
                return "Error: Impacts must be + or -"

        if not valid_email(email):
            return "Error: Invalid email format"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "result.csv")
        file.save(input_path)

        run_topsis(input_path, weights, impacts, output_path)
        send_email(email, output_path)

        return "Result sent to your email successfully!"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/platforms")
def platforms():
    return render_template("platforms_intro.html")

@app.route("/platforms-grid")
def platforms_grid():
    return render_template("platforms_grid.html")

@app.route("/campaign", methods=["GET", "POST"])
def campaign():
    result = None
    if request.method == "POST":
        product = request.form["product"]
        audience = request.form["audience"]
        platform = request.form["platform"]

        prompt = f"""
Create a professional marketing campaign for:
Product: {product}
Target Audience: {audience}
Platform: {platform}

Include:
- Campaign objective
- Key message
- Call to action
"""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        result = response.choices[0].message["content"]

    return render_template("campaign.html", result=result)

@app.route("/pitch", methods=["GET", "POST"])
def pitch():
    result = None
    if request.method == "POST":
        product = request.form["product"]
        persona = request.form["persona"]

        prompt = f"""
Write a short sales pitch for:
Product: {product}
Customer Persona: {persona}

Include:
- Pain point
- Solution
- Value proposition
- Call to action
"""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250
        )

        result = response.choices[0].message["content"]

    return render_template("pitch.html", result=result)

@app.route("/lead", methods=["GET", "POST"])
def lead():
    result = None
    if request.method == "POST":
        name = request.form["name"]
        budget = request.form["budget"]
        need = request.form["need"]
        urgency = request.form["urgency"]

        prompt = f"""
Evaluate this sales lead:

Name: {name}
Budget: {budget}
Business Need: {need}
Urgency: {urgency}

Give:
- Lead score out of 100
- Probability of conversion
- Priority level (Hot/Warm/Cold)
- Short reasoning
"""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250
        )

        result = response.choices[0].message["content"]

    return render_template("lead.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

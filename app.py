
import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
openai.api_key = 'openAI key'  # Replace with your actual OpenAI API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_visa', methods=['POST'])
def check_visa():
    nationality = request.form['nationality']
    visa_countries = request.form['visa_countries']
    departure_airport = request.form['departure_airport']
    connecting_airports = request.form['connecting_airports']
    arrival_airport = request.form['arrival_airport']

    prompt = (
        f"A person with nationality {nationality} who has visas from {visa_countries} "
        f"is traveling from {departure_airport} to {arrival_airport} with connecting airports {connecting_airports}. "
        "Do they require a visa or transit visa to complete their journey?"
    )

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0
    )
    result = response.choices[0].message['content'].strip()
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

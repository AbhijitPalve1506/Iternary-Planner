from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

# Function to generate itinerary using the Ollama model
def generate_itinerary(days):
    activities_prompt = ""
    for day in range(1, days + 1):
        activities_prompt += f"Day {day}:\n- Activity 1\n- Activity 2\n\n"
    
    prompt = f"Create a {days}-day itinerary for Mumbai. Include unique activities for each day, ensuring no places repeat. Format it like this:\n\n{activities_prompt}"
    
    # Call the Ollama model to generate the itinerary
    response = ollama.chat("llama3.2", [{"role": "user", "content": prompt}])
    
    return response['message']['content']

# Route for the home page
@app.route('/')
def index():
    return render_template('home.html')

# Route for generating itinerary
@app.route('/generate-itinerary', methods=['POST'])
def itinerary():
    days = int(request.form.get('days'))
    if 1 <= days <= 7:
        itinerary = generate_itinerary(days)
        return render_template('result.html', itinerary=itinerary, days=days)
    else:
        return "Please enter a valid number of days (1-7)."

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from g4f.client import Client

app = Flask(__name__)

# Initialize the G4F client
client = Client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['POST'])
def generate_text():
    user_input = request.form['user_input']
    
    # Call the GPT-4 model for text response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}],
    )
    
    text_response = response.choices[0].message.content
    return jsonify({'text_response': text_response})

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.form['image_prompt']
    
    # Call the flux model for image generation
    response = client.images.generate(
        model="flux",
        prompt=prompt,
        response_format="url"
    )
    
    image_url = response.data[0].url
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)

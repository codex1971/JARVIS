import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# আপনার API Key এখানে বসান (প্রোডাকশনে Environment Variable ব্যবহার করা ভালো)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get('command')
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input)
    return jsonify({"answer": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

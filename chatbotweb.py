from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "my-API-key"

def get_completion(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )
    return response['choices'][0]['message']['content']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        response = get_completion(user_input)
        return render_template('index.html', response=response)
    else:
        return render_template('index.html', response="")

if __name__ == "__main__":
    app.run(debug=True)

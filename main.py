from flask import Flask, render_template, request, jsonify
from datetime import datetime
from app.qa_chain import qa_chain

app = Flask(__name__)

# Create a global chain instance once
chain = qa_chain()

@app.route('/')
def index():
    # Pass the current time to the template
    return render_template('index.html', now=datetime.now())

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        user_question = data.get('question')

        if not user_question:
            return jsonify({'response': "Please enter a valid question."}), 400

        # Invoke the QA chain
        response = chain.invoke(user_question)

        return jsonify({'response': response})
    except Exception as e:
        print(f"Error during processing: {e}")
        return jsonify({'response': "Something went wrong. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)

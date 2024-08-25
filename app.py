from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_lowercase_alphabet = [max([char for char in alphabets if char.islower()], default='')]

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({
        "operation_code": 1
    })

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/rf', methods=['POST'])
def handle_request():
    # Получаем данные из запроса
    data = request.get_json()
    
    # Обрабатываем запрос
    response_text = "Привет! Это мой первый навык."
    
    # Формируем ответ
    response = {
        "response": {
            "text": response_text,
            "end_session": False
        },
        "version": "1.0"
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

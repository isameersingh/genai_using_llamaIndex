from flask import Flask, jsonify
from chatSql import ChatWithSql
app = Flask(__name__)
obj = ChatWithSql("root","12345","localhost","ahi_database")
@app.route('/send-message', methods=['GET'])
def send_message():
    # message = "Hello, this is a message from the Flask API!"
    message = obj.message("How many rows do we have in cattle table ?")
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)

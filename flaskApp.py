from flask import Flask, jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': "Raju",
        'Contact': "995510186", 
        'done': False
    },
    {
        'id': 2,
        'Name': "Rahul",
        'Contact': "9219505321", 
        'done': False
    },
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"ERROR!",
            "message": "Please provide the missing data!"
        }),400

    contact = {
        'id': List[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    List.append(contact)
    return jsonify({
        "status":"SUCCESS",
        "message": "Contact saved succesfully!"
    })

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    pt = data.get('text', '')

    if "판정" in pt :
        pt='/emas " " '+pt
    else :
        pt='/desc '+pt

    return jsonify({"text": pt})

if __name__ == "__main__":
    app.run()

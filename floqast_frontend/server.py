from flask import Flask, render_template, request, jsonify
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return 'floqast Frontend - use /register or /transaction'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form or request.json
        if not data.get('email'):
            return jsonify({'error':'email required'}), 400
        return jsonify({'id':'u123','email':data.get('email')}), 201
    return render_template('register.html')

@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    if request.method == 'POST':
        data = request.form or request.json
        if not data.get('amount'):
            return jsonify({'error':'amount required'}), 400
        return jsonify({'id':'t123','amount':data.get('amount')}), 201
    return render_template('transaction.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

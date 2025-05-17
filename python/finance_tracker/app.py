from flask import Flask, render_template
from controller.transaction_controller import transaction_api

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(transaction_api)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

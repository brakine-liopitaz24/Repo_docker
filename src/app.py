from flask import Flask, render_template
 
# app = Flask(__name__, template_folder='../templates', static_folder='../static')
app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"

@app.route('/')
def inicio():
    return render_template('./index.html')

if __name__ == '__main__':
    app.run(port=7000, host="0.0.0.0",debug=True)
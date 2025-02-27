from flask import Flask, render_template
import os 

app= Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    register_service_url = os.getenv('REGISTER_SERVICE_URL')
    deletion_service_url = os.getenv('DELETION_SERVICE_URL')
    print(register_service_url)
    return render_template('index.html', register_service_url=register_service_url, deletion_service_url=deletion_service_url)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

#run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=8000,ssl_context=('certificate.crt', 'private.key'))
    # app.run(debug=True, port=5002)
    app.run(host='0.0.0.0', port=5002, debug=True, ssl_context=('localhost.pem', 'localhost-key.pem'))





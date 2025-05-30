from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, HTTPS!"

if __name__ == "__main__":
    context = (
        "C:/Users/matos/OneDrive/Desktop/mamoney/certificates/CF_origin_certificate_bananagold.com.au.PEM",
        "C:/Users/matos/OneDrive/Desktop/mamoney/certificates/PK_CF_origin_certificate_bananagold.com.au.key"
    )
    app.run(host='0.0.0.0', port=443, ssl_context=context)

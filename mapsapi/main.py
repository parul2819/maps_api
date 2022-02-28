from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def follow_map():
    return render_template('google_map_api.html')


if __name__ == '__main__':
    app.run(debug=True)
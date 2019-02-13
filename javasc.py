from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def  hello():
	return render_template('javasc.html')

@app.route('/admin')
def  hello_admin():
	return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'Hello %s as Guest' % guest


if __name__ == '__main__':
	app.run(debug = True)

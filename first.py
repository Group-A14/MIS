from flask import Flask, render_template, url_for, request
import os

app=Flask(__name__)
route=os.path.dirname(os.path.abspath(__file__))# our current path

@app.route('/')
@app.route('/user/register', methods=['POST','GET'])
def register():
	if request.method=='POST':
		image=request.files['image']#get image from html
		file='/'+image.filename#new path to join 
		destiny=''.join([route,file])#to join with the previous path
		name = request.form['name']
		email = request.form['email']
		desc = request.form['desc']
		button=request.form['send']
		image.save(destiny)
		return "<h1>"+name+"<br>"+email+"<br>"+desc+"<br></h1>"+image
		# return "<h1>I am from POST request</h1>"
	return render_template('welc.html')


if __name__=='__main__':
	app.run(debug=True)

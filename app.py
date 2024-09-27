from flask import flask,render_template,request
app=flask(__name__)


@app.route('/')
def registration_form():
    return render_template('register.html')
@app.route('/submit',methods=['POST'])
def submit():
   name=request.form['name']
   email=request.form['email]
   

   return f"registration successful for {name} with {email}"

if __name__=='__main__':
     app.run(host='0.0.0',por=50000)

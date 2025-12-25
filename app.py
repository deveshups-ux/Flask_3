from flask import Flask, render_template , request , session , url_for , redirect , flash
app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        username = request.form.get("username")
        if not username :
            flash("Plese enter your name " , "error")
            return redirect(url_for('form'))
        
        flash(f"Login Succesful {username}" , "success")
        return redirect(url_for('thanku'))

        
    return render_template('form.html')

@app.route('/thanku')
def thanku():
    return render_template('thanku.html')

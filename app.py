from flask import Flask, render_template, redirect, url_for, request


total_q = 0
correct_q = 0
app = Flask(__name__) #creating the Flask class object

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/donate' , methods=['GET', 'POST'])
def log_don():
    if request.method == 'POST':
        user = request.form['emaildon']
        password = request.form['passdon']

        if user == 'recep@engenius.com' and password == 'ryilkici1':
            return render_template("donator.html")

        else:
            return render_template("mainpage.html")

@app.route('/packages' , methods=['GET', 'POST'])
def log_stu():
    if request.method == 'POST':
        user = request.form['emailstu']
        password = request.form['passstu']

        if user == 'engenius@insider.com' and password == 'engenius1':
            return render_template("packages.html")

        else:
            return render_template("mainpage.html")

@app.route('/aims' , methods=['GET', 'POST'])
def aim():
    if request.method == 'POST':
        return render_template("surd.html")

@app.route('/video' , methods=['GET', 'POST'])
def video():
    return render_template("video.html", correct_q=correct_q, total_q=total_q)

@app.route('/temp' , methods=['GET', 'POST'])
def temp():
    return redirect(url_for("video"))

@app.route('/video/<float:timeq1>/<int:correct_q>/<int:total_q>')
def videoq1(timeq1, correct_q, total_q):
    return render_template("video.html", timeq1 = timeq1, correct_q = correct_q, total_q = total_q)

@app.route('/videoq1', methods = ["POST", "GET"])
def login():
    global total_q, correct_q
    total_q += 1
    print(request.form)
    if request.form["q1"] == "second":
        correct_q += 1
    return redirect(url_for("videoq1", timeq1 = 3.251, correct_q = correct_q, total_q = total_q))


@app.route('/videoq2', methods = ["POST", "GET"])
def login2():
    global total_q, correct_q
    total_q += 1
    print(request.form)
    if request.form["q2"] == "first":
        correct_q += 1
    return redirect(url_for("videoq1", timeq1 = 8.251, correct_q = correct_q, total_q = total_q))

@app.route('/videoq3', methods = ["POST", "GET"])
def login3():
    global total_q, correct_q
    total_q += 1
    print(request.form)
    if request.form["q3"] == "second":
        correct_q += 1
    return redirect(url_for("videoq1", timeq1 = 12.251, correct_q = correct_q, total_q = total_q))

@app.route('/videoq4', methods = ["POST", "GET"])
def login4():
    global total_q, correct_q
    total_q += 1
    correct_q += 1
    return redirect(url_for("videoq1", timeq1 = 16.251, correct_q = correct_q, total_q = total_q))

if __name__ =='__main__':
    app.run(debug = True)

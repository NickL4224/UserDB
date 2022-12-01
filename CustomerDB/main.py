from flask import Flask, request, render_template, redirect, abort
from models import db, CustomerModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()


@app.route("/home")
def home():
    return render_template('home.html', user_count = count_users())


@app.route('/add_cust', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create_cust.html')
    if request.method == 'POST':
        fname = request.form['first_name']
        lname = request.form['last_name']
        cEmail = request.form['email']
        cPhone = request.form['phone']
        cCity = request.form['city']
        cState = request.form['state']
         
        customer = CustomerModel(first_name=fname, last_name=lname, email=cEmail, phone=cPhone, city=cCity, state=cState)
        db.session.add(customer)
        print(customer.first_name + " Added Successfully")
        db.session.commit()
        return redirect('/data')


@app.route('/data')
def getAllCusts():
    customers = CustomerModel.query.all()
    return render_template('datalist.html', customers = customers)


@app.route('/data/<id>')
def retrieveSingleCustomer(id):
    customer = CustomerModel.query.filter_by(id=id).first()
    if customer:
        return render_template('data.html', customer = customer)
    return f"Customer with id = {id} Doenst exist"

@app.route('/data/delete', methods=['GET','POST'])
def delete_page():
    return render_template('delete.html')

@app.route('/data/delete/<int:id>', methods=['GET','POST'])
def delete_cust(id):
    customer = CustomerModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return redirect('/data')
        abort(404)
    return render_template('datalist.html')

@app.route('/data/delete_all', methods=['GET', 'POST'])
def delete_all():
    customers = CustomerModel.query.all()
    if request.method == 'POST':
        for customer in customers:
            db.session.delete(customer)
        db.session.commit()
        return redirect('/home')
    return render_template('delete.html')

def count_users():
    i = 0
    customers = CustomerModel.query.all()

    for customer in customers:
        i +=  1
    
    return i
       


app.run(host='localhost', port=5000, debug=True)
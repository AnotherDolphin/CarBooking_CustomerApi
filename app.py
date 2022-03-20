from flask import Flask, redirect, request, render_template
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
db = yaml.safe_load(open('db.yaml'))

# connection
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

# MAIN PAGE
@app.route("/", methods=['GET'])
def form():
    return render_template('index.html')

# ADD CUSTOMER
@app.route("/add", methods=['GET', 'POST'])
def addCustomer():
    if request.method == 'POST':
        details = request.form
        first_name = details['first_name']
        last_name = details['last_name']
        phone = details['phone']
        email = details['email']
        city = details['city']
        street = details['street']
        cursor = mysql.connection.cursor()
        cursor.execute(f"""
        insert into customers (first_name, last_name, phone, email, city, street)
        values('{first_name}','{last_name}','{phone}', '{email}', '{city}', '{street}')
        """)
        mysql.connection.commit()
        cursor.close()
        return render_template('success.html')
    return render_template('add.html')

# CUSTOMER RETRIEVAL(GET) INTERFACE
@app.route("/get", methods=['GET'])
def getOptions():
    if('id' in request.args):
        id = request.args['id']
        return redirect(f'/get/{id}')
    return render_template('get.html')

# VIEW ALL CUSTOMERS
@app.route("/get/all", methods=['GET'])
def getAllCustomers():
    cursor = mysql.connection.cursor()
    result = cursor.execute("select * from customers")
    if result > 0:
        data = cursor.fetchall()
        return render_template('get.html', data = data)
    else:
        return render_template('get.html', data = 'No customers in database yet')

# GET CUSTOMER WITH ID
@app.route("/get/<int:id>", methods=['GET'])
def getCustomer(id):
    cursor = mysql.connection.cursor()
    result = cursor.execute(f"select * from customers where id = '{id}'")
    if result > 0:
        data = cursor.fetchall()
        return render_template('get.html', data = data)
    else:
        return render_template('get.html', data = 'No customer with that ID')

# UPDATE CUSTOMER DATA
@app.route("/update", methods=['GET', 'PUT'])
def updateCustomer():
    if request.method == 'PUT':
        details = request.json
        id = details['id']
        cursor = mysql.connection.cursor()
        result = cursor.execute(f"select * from customers where id='{id}'")
        if not result > 0:
            return 'No Customer with that ID'
        attr = details['attr']
        val = details['val']
        try:
            cursor.execute(f"""update customers
                set {attr} = '{val}'
                where id = '{id}' """)
            mysql.connection.commit()
            cursor.close()
            return 'Update Operation Successful'
        except Exception as e:
            cursor.close()
            return 'Operation Failed: check input.'
    return render_template('update.html')

# DELETE INTERFACE
@app.route("/delete", methods=['GET'])
def deleteTemplate():
    return render_template('delete.html')

# DELETE REQUEST
@app.route("/delete/<int:id>", methods=['GET', 'DELETE'])
def deleteCustomer(id):
    if request.method == 'DELETE':
        cursor = mysql.connection.cursor()
        result = cursor.execute(f"select * from customers where id='{id}'")
        if not result > 0:
            return 'No Customer with that ID'
        try:
            cursor.execute(f"delete from customers where id='{id}'")
            mysql.connection.commit()
            cursor.close()
            return 'Delete Operation Successful'
        except Exception as e:
            cursor.close()
            return 'Operation Failed: check input.'
    else:
        return render_template('delete.html', rej = 'DELETE requests can only be made using the app interface')

if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request,  redirect  ,url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

# MYSQL Connection
app.config['MYSQL_HOST'] = 'Localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'flaskemployees'
mysql = MySQL(app)


# settings  
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM employees')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', empls = data)

@app.route('/add_employees', methods=['POST'])
def add_employees():
    if request.method == 'POST':
      fullname =  request.form['fullname']
      phone =  request.form['phone']
      email =  request.form['email']
      cur = mysql.connection.cursor()
      cur.execute('INSERT INTO employees (fullname, phone, email) VALUES (%s, %s, %s)',
      (fullname, phone, email))
      mysql.connection.commit()
      flash('Empleado Agregado exitosamente')

      return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_employees(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM employees WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit-employees.html', empl = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_empl(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE employees
        SET fullname = %s,
            email = %s,
            phone = %s
        WHERE id = %s
    """, (fullname, phone, email, id))
    mysql.connection.commit()
    flash('actualizacion de los empleados ha sido exitoza')
    return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_employees(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM employees WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Empleado Removido Exitosamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)


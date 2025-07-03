from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

conexion = psycopg2.connect(
            database="practica",
            host="192.168.3.116",
            user="hectorguz",
            password="Us3r123"
        )
cur = conexion.cursor()
cur.execute(
    """CREATE TABLE IF NOT EXISTS productos(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio FLOAT);"""
)
cur.execute(
    """INSERT INTO productos(nombre, precio)VALUES(
    'Manzana',15),('Naranja',50);"""
)
conexion.commit()
cur.close()
conexion.close()

@app.route("/")
def index():
    conexion = psycopg2.connect(
            database="practica",
            host="192.168.3.116",
            user="hectorguz",
            password="Us3r123"
        )
    cur = conexion.cursor()
    cur.execute('''SELECT * FROM productos''')
    data = cur.fetchall()
    cur.close()
    conexion.close()
    return render_template('index.html', data=data)

@app.route('/create', methods=['POST'])
def create():
    conexion = psycopg2.connect(
            database="practica",
            host="192.168.3.116",
            user="hectorguz",
            password="Us3r123"
        )
    conexion.commit()
    nombre = request.form['nombre']
    precio = request.form['precio']
    cur.execute('''INSERT INTO productos (nombre, precio)VALUES(%s, %s)''', (nombre, precio))
    conexion.commit()
    cur.close()
    conexion.close()
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    conexion = psycopg2.connect(
            database="practica",
            host="192.168.3.116",
            user="hectorguz",
            password="Us3r123"
        )
    cur = conexion.cursor()
    nombre = request.form['nombre']
    precio = request.form['precio']
    id = request.form['id']

    cur.execute('''UPDATE producto set NOMBRE=%s, \ precio=%s WHERE id=%s''', (nombre, precio,id))
    conexion.commit()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    conexion = psycopg2.connect(
            database="practica",
            host="192.168.3.116",
            user="hectorguz",
            password="Us3r123"
        )
    cur = conexion.cursor()
    id = request.form['id']
    cur.execute('''DELETE FROM productos WHERE id=%s''', (id,))
    conexion.commit()
    cur.close()
    conexion.close()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
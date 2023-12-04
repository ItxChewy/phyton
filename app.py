from flask import Flask, render_template, flash, request, Response, jsonify, redirect, url_for
from database import app, db, UsuarioSchema
from usuario import Usuario

usuario_schema = UsuarioSchema()
usuario_schema = UsuarioSchema(many=True)

@app.route('/')
def home():
    usuario = Usuario.query.all()
    usuarioLeidos = usuario_schema.dump(usuario)
    return render_template('index.html', usuario = usuarioLeidos)

    # return jsonify(estudiantesLeidos)

#Method Post
@app.route('/usuario', methods=['POST'])
def addUsuario():
    nombreusuario = request.form['nombreusuario']
    nombre = request.form['nombre']
    contraseña = request.form['contraseña']
   
    if nombreusuario and nombre and contraseña:
        nuevo_usuario = Usuario(nombreusuario, nombre, contraseña)
        db.session.add(nuevo_usuario)
        db.session.commit()
        response = jsonify({
            'nombreusuario' : nombreusuario,
            'nombre' : nombre,
            'contraseña' : contraseña
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<id>')
def deleteUsuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    
    flash('Usuario ' + id + ' eliminado correctamente')
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<id>', methods=['POST'])
def editUsuario(id):    
    nombreusuario = request.form['nombreusuario']
    nombre = request.form['nombre']
    contraseña = request.form['contraseña']
    
    if nombreusuario and nombre and contraseña:
        usuario = Usuario.query.get(id)
  # return student_schema.jsonify(student)
        usuario.nombreusuario = nombreusuario
        usuario.nombre = nombre
        usuario.contraseña = contraseña
        
        db.session.commit()
        
        response = jsonify({'message' : 'Usuario ' + id + ' actualizado correctamente'})
        flash('Usuario ' + id + ' modificado correctamente')
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
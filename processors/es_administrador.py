
def usuario_es_administrador(request):
    
    #Verifica si el usuario está en el grupo 'Administrador' y lo pasa al contexto global.
    usuario_es_administrador = request.user.groups.filter(name='Administrador').exists() #el metodo exists() verifica si el usuario pertenece a ese grupo
 
    # Devolvemos el resultado como un diccionario
    return {'usuario_es_administrador': usuario_es_administrador}
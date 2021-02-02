# dubee-employees

Repositorio destinado para llevar a cabo el proceso de evaluacion y posible onboarding de Ariel Tavarez

#### Problema

La empresa Dubeetech necesita crear una aplicación web que permita registrar programadores de nuevo ingreso, de modo que cuando sea necesario realizar alguna consulta acerca de ellos, se disponga de una herramienta para tal fin. De igual forma, dicha herramienta deberá permitir que los datos de los programadores puedan ser actualizados y si en algún punto alguno dejara de laborar para la empresa pueda ser desactivado (no eliminado)

#### Solución

Crear un formulario web para registrar/actualizar programadores, una vista (puede ser una tabla) para listar los programadores existentes y colocar un buscador que permita filtrar por cualquier campo. 

Los campos listados a continuación son los que deben aparecer en el formulario y en la vista.

- Nombres
- Apellidos
- Fecha de Nacimiento 
- Email
- Célula 
- Número de Móvil 
- Número Residencial (Opcional)
- Sexo (Usar radios)
- Lenguaje De Programación Principal (Usar dropdown)
- Status (usar radios con los valores: Activo e Inactivo) 

  Todos los campos son requeridos, excepto Numero Residencial.

  También crear una tabla donde se puedan mostrar todos los programadores existentes.

Para fines de esta prueba, no es indispensable  crear una interfaz con estilos CSS, es suficiente con que los Campos se puedan visualizar bien y en orden). Sin embargo, es un plus si el manejas Bootstrap o algún otro framework de CSS y lo puedes usar para esta tarea.

Crear un API simple con los siguientes endpoints:

- Para crear un nuevo programador:  POST /api/v1/programmers
- Para actualizar un programador: PUT /api/v1/programmers
- Para obtener todos los programadores: GET /api/v1/programmers?term=

Crear el API también implica crear la base de datos con los campos listados más arriba. Es responsabilidad del desarrollador crearla adecuadamente y con el tipo de datos correcto.

Es necesario que los datos sean validados según el tipo del que sean.

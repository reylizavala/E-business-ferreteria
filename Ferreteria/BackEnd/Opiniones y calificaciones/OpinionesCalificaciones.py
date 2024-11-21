#Opiniones y calificaciones

#Requerimientos
"""
El sistema ofrecerá al usuario poder escribir un comentario de opinión en los productos que haya realizado pedidos a través del botón 
“Escribir un comentario” en la sección de “Historial de compras”. El usuario tendrá que ingresar una calificación en medida de 1 a 5 
estrellas en conjunto con su comentario. Los comentarios no podrán exceder el límite de 240 caracteres.

Los usuarios podrán eliminar sus propios comentarios a través del botón “Eliminar comentario” que será visible solo en sus propios 
comentarios. 

Todos los productos tendrán su calificación promedio visible en el catálogo de compras. La calificación promedio se calculará 
automáticamente y se deberá de actualizar cada vez que un usuario realice un comentario.

El sistema permitirá que los usuarios vean las opiniones de otros usuarios sobre un producto antes de proceder con la compra.  Esta 
funcionalidad se habilitará a través de un botón de “Ver comentarios” en la página del producto, donde los usuarios podrán ver la 
calificación y leer comentarios sobre la experiencia de otros clientes.

El sistema deberá permitir a los usuarios ordenar y filtrar los comentarios mediante calificaciones y fechas. El filtro de calificación 
deberá permitir a los usuarios seleccionar la cantidad de estrellas (1 a 5) de las cuales desea ver comentarios. Si no existen 
comentarios con esa cantidad de estrellas se mostrará una leyenda indicando que no hay comentarios con la calificación seleccionada. 
El filtro de fecha podrá ser en modo ascendente (más recientes primero) y descendiente (más antiguos primero). 

El sistema permitirá al administrador gestionar los comentarios de los usuarios en los productos proporcionando una opción para poder 
eliminar aquellos comentarios inapropiados o que no cumplan las políticas de uso. Esto se podrá hacer a través del botón “Eliminar 
comentario” dentro de la sección de comentarios en el inventario.
"""

#Clases relacionadas
"""
---Clase Opinion---
    Atributos: 
        idOpinion - Número único identificador de opinión. Tipo entero. Acceso público.
        contenido - Contenido del comentario de opinión. Tipo cadena. Acceso público.
        calificacion - Calificacion del pedido asociado a la opinión. Tipo entero. Acceso público.
    Métodos:
        publicarOpinion() - Permite publicar una opinión. Método privado.
        borrarOpinion() - Permite borrar una opinión existente. Método privado.
    Conexiones: 
        Conexión 1 a 1 con Pedido.
"""
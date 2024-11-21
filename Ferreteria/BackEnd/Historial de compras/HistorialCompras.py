#Historial de compras

#Requerimientos
"""
El sistema permitirá al usuario visualizar su historial de compras desde el apartado de “Historial de compras” en donde se podrán 
observar detalles como la fecha de la compra, productos adquiridos, monto total pagado, estado del pedido y método de pago utilizado.

El sistema permitirá al usuario seleccionar productos de pedidos anteriores y agregarlos a su carrito de compras para realizar la 
compra nuevamente, mediante un botón de “Volver a comprar”. Los productos del pedido anterior serán puestos en el carrito de compras 
si hay stock disponible para los productos. Si algún producto no tiene stock necesario o no está en existencia el sistema mostrará un 
mensaje informando al usuario que ese producto no pudo ser guardado en el carrito de compra.

El sistema mostrará un botón de “devolución” en los pedidos que tengan mínimo 24 horas con el estado “entregado”. Los usuarios podrán 
solicitar una devolución de dinero en caso de no estar satisfechos con la compra. 

El sistema mostrará un botón de “Escribir un comentario” en los pedidos con el estado “entregado”. 

El sistema dará acceso al administrador a los detalles de cada pedido realizado por los usuarios como cantidad de productos comprados, 
la descripción de cada producto, el precio unitario y monto total.
"""

#Clases relacionadas
"""
---Clase Usuario---
    Atributos: 
        idUsuario - Número único identificador de usuario. Tipo entero. Acceso público.
        nombreUsuario - Nombre asociado a la cuenta del usuario. Tipo cadena. Acceso público.
        correo - Dirección de correo electrónico asociada a la cuenta. Tipo cadena. Acceso privado.
        contrasena - Contraseña asociada a la cuenta. Tipo cadena. Acceso privado.
        telefono - Número de teléfono asociado a la cuenta. Tipo cadena. Acceso privado.
    Métodos:
        registrarse() - Permite registrar un nuevo usuario. Método público.
        iniciarSesion() - Permite iniciar sesión a una cuenta existente. Método público.
        verHistorialCompras() - Permite ver el historial de compras asociadas a la cuenta. Método público.
    Conexiones: 
        Conexión 1 a N con clase MetodoDePago.
        Conexión 1 a N con Pedido.

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
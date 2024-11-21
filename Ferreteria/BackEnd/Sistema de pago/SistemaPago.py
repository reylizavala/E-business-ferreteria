#Sistema de pago

#Requerimientos
"""
El sistema contará con una página de pago, a la cual se podrá acceder una vez se procese un pedido en el carrito de compra. 
La página mostrará un desglose del total a pagar, mostrando información de los productos en el carrito y el precio por envío.

El sistema solicitará al usuario ingresar una dirección para el envío del producto. Los datos que solicita son: código postal,
calle y número de dirección, estado, ciudad, país. Estos campos son obligatorios. El sistema mostrará los siguientes campos
opcionales: número de apartamento, nota de entrega. Los usuarios tendrán la opción de guardar la dirección ingresada para compras
posteriores.

El sistema solicitará una forma de pago para procesar la compra. Los métodos de pago autorizados son: tarjeta de crédito, tarjeta
de débito. Los datos bancarios solicitados son: nombre de propietario de tarjeta, número de tarjeta, fecha de vencimiento, código
de seguridad. Los usuarios tendrán la opción de guardar los datos bancarios para compras posteriores.

El sistema guardará en la base de datos la información bancaria del usuario con un cifrado de extremo a extremo para proteger los datos.

El sistema deberá guardar los datos bancarios con un identificador para diferenciarlos en caso de que existan más de una forma de 
pago guardada por el usuario, los datos bancarios del usuario solo se guardaran en el sistema si el usuario da la autorización.

El sistema verificará la dirección de envío y los datos bancarios. Una vez verificados se mostrará el botón de “realizar compra”. 
Al realizar la compra el pedido será procesado por el sistema, se realizará la transacción y se le enviará un correo de confirmación 
mostrando el resumen de la compra y los datos del pedido al correo electrónico que está vinculado con la cuenta. El sistema mostrará 
la confirmación de que la compra ha sido realizada, mostrará el número de identificación del pedido y un botón de “volver a catálogo”
posterior  a la compra para volver a la página de catálogo.

El sistema debe de procesar la compra y realizar la transacción de manera inmediata posterior a la compra. El sistema no debe de 
demorar más de 20 segundos en procesar la compra. El mensaje de confirmación por correo no debe demorar más de 10 segundos en enviarse.

Los usuarios podrán cancelar su pedido una vez haya sido procesado, tendrán 48 horas posterior a la compra del pedido para realizar 
la cancelación. Los usuarios no podrán cancelar su compra después de las 48 horas o una vez el pedido sea enviado. Los usuarios podrán 
solicitar una devolución si no están satisfechos con la compra. El sistema solo permitirá devoluciones 24 horas después de la 
confirmación de entrega de pedido. Las devoluciones se podrán realizar en el apartado de “historial de compras”.

El sistema permitirá al administrador autorizar y realizar devoluciones y cancelaciones de productos o de envíos.

El sistema deberá de notificar al administrador en no más de 5 minutos posterior a una compra si existe algún tipo de problema con el 
pago de algún producto y deberá de dar una pequeña reseña del error en el mensaje enviado por correo al administrador.
"""

#Clases relacionadas
"""
---Clase Pago---
    Atributos: 
        idPago - Número único identificador de pago. Tipo entero. Acceso privado.
        monto - Cantidad a pagar. Tipo flotante. Acceso privado.
    Métodos:
        procesarPago() - Permite procesar un pago. Método público.
        confirmarPago() - Permite verificar los datos bancarios. Método privado.
    Conexiones: 
        Conexión 1 a 1 con MetodoDePago
        Conexión 1 a 1 con Pedido

---Clase MetodoDePago---
    Atributos: 
        idMetodoPago - Número único identificador de método de pago. Tipo entero. Acceso privado.
        numTarjeta - Número de tarjeta bancaria. Tipo entero largo. Acceso privado.
        fechaVencimiento - Fecha de vencimiento de tarjeta bancaria. Tipo fecha. Acceso privado.
        cvv - Número de seguridad de tarjeta bancaria. Tipo entero. Acceso privado.
    Métodos:
        nuevoMetodoPago() - Permite crear un nuevo método de pago. Método público.
        editarMetodoPago() - Permite editar los detalles de un método de pago existente. Método privado.
        eliminarMetodoPago() - Permite eliminar un método de pago existente. Método privado.
    Conexiones: 
        Conexión N a 1 con Usuario
        Conexión 1 a 1 con Pago

---Clase Producto---
    Atributos: 
        idProducto - Número único identificador de producto. Tipo entero. Acceso público.
        nombreProducto - Nombre del producto. Tipo cadena. Acceso público.
        descripcion - Descripción del producto. Tipo cadena. Acceso público.
        precio - Precio unitario del producto. Tipo flotante. Acceso público.
        disponibilidad - Muestra si el producto está disponible. Tipo booleano. Acceso público.
    Métodos:
        crearProducto() - Permite crear un nuevo producto. Método privado.
        borrarProducto() - Permite borrar un producto del sistema. Método privado.
        editarProducto() - Permite editar los detalles de un producto. Método privado.
        consultarDisponibilidad() - Permite consultar el valor del atributo disponibilidad. Método público.
    Conexiones: 
        Conexión N a N con Pedido.
        Conexión 1 a 1 con Inventario.
"""
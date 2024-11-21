#Carrito de compra

#Requerimientos
"""
El sistema ofrecerá la opción en cada producto de agregar al carrito de compras. El carrito de compras será una sección en la que
se irán guardando todos los productos seleccionados para poderlos comprar en un solo pedido. 

El usuario puede agregar un mismo producto múltiples veces, con un límite máximo del número de stock disponible de ese producto.

El usuario tendrá la opción de eliminar productos existentes del carrito de compras. Si existen múltiples unidades de un mismo 
producto podrá eliminar cierto número de unidades o todas las existencias en el carrito.

El sistema al editar el carrito de compra se actualizará instantáneamente y mostrará los cambios al carrito, sea adición o eliminación
de productos, aumento o disminución de unidades por producto, y el desglose del monto total a pagar.

El sistema mostrará un desglose del subtotal de pago del carrito de compra, mostrando cada producto y existencias en el carrito junto
con el precio respectivo, más costos añadidos por envío. El sistema realizará una suma de todos los costos y mostrará la cantidad
tentativa a pagar. Al final del subtotal se mostrará el botón de “pagar”, que redirigirá al usuario a la página de pago.

El sistema permitirá añadir descuentos a las compras ingresando un código de descuento. Los descuentos aplicarán al total de los 
productos agregados al carrito de compras, esto aplica solo si en el carrito de compras hay de dos o más productos agregados.

El sistema reúne las características principales de los productos que el usuario tiene agregados en el carrito de compra y después 
de la compra le mostrará sugerencias en la página principal sobre productos que tengan características similares a esos productos.
"""

#Clases relacionadas
"""
--- Clase Pedido ---
    Atributos: 
        idPedido - Número único identificador de pedido. Tipo entero. Acceso público.
        estadoPedido - Estado de entrega en tiempo real del pedido. Tipo cadena. Acceso privado.
        direccion - Dirección a donde se enviará el pedido. Tipo cadena. Acceso privado.
        total - Precio total a pagar por el pedido. Tipo flotante. Acceso privado.
    Métodos:
        crearPedido() - Permite comenzar la existencia de un pedido. Método público.
        agregarProductoAPedido() - Permite agregar productos a un pedido. Método público.
        eliminarProductoAPedido() - Permite eliminar un producto de un pedido. Método público.
        confirmarPedido() - Permite procesar un pedido completado. Método público.
        calcularTotal() - Permite calcular la suma de los precios de los productos. Método público.
        actualizarEstadoPedido() - Permite actualizar el estado de un pedido. Método público.
    Conexiones: 
        Conexión N a 1 con Usuario.
        Conexión 1 a 1 con Pago
        Conexión N a N con Producto
        Conexión 1 a N con Notificaciones
        Conexión 1 a 1 con Opinion

--- Clase Producto ---
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

--- Clase Pago ---
    Atributos: 
        idPago - Número único identificador de pago. Tipo entero. Acceso privado.
        monto - Cantidad a pagar. Tipo flotante. Acceso privado.
    Métodos:
        procesarPago() - Permite procesar un pago. Método público.
        confirmarPago() - Permite verificar los datos bancarios. Método privado.
    Conexiones: 
        Conexión 1 a 1 con MetodoDePago
        Conexión 1 a 1 con Pedido
"""
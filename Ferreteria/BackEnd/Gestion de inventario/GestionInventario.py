#Gestion de inventario

#Requerimientos
"""
El sistema permitirá al administrador ver y gestionar el inventario a través de una sección llamada “Inventario”.

El sistema permitirá al administrador agregar y eliminar productos. El sistema solicitará los siguientes datos al agregar un nuevo 
producto al inventario: nombre del producto, descripción del producto, imagen del producto, precio unitario, stock en almacén y
cantidad mínima en stock. Todos los campos son obligatorios.

El administrador podrá gestionar la lista de productos disponibles en la tienda con opciones para agregar nuevos productos, modificar
detalles de productos existentes o eliminar productos. El sistema permitirá al administrador modificar únicamente la cantidad de stock
disponible de cada producto a través de un botón específico. 

El sistema mostrará cuando un producto esté por terminarse cuando el stock llegue a la cantidad especificada de stock mínimo a través
de un signo de notificación naranja sobre el apartado del producto. Los productos cuyo stock sea 0 serán identificados con un signo 
de notificación rojo sobre el apartado del producto.

Las actualizaciones y modificaciones del inventario deben reflejarse en tiempo real en todas las partes del sistema.
"""

#Clases relacionadas
"""
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

---Clase Inventario---
    Atributos: 
        productos - Lista de productos. Tipo lista de objeto Productos. Acceso privado.
        stock - Número de stock de producto. Tipo entero. Acceso privado.
    Métodos:
        actualizarStock() - Permite actualizar el número de stock de un producto. Método privado.
    Conexiones: 
        Conexión 1 a 1 con Producto.
"""
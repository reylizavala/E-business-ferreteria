#Catalogo de productos

#Requerimientos
"""
El sistema tendrá un apartado “Catálogo” en el cual se mostrará el catálogo de todos los productos disponibles que hay
en existencia para el usuario con los datos respectivos de cada producto: nombre de producto, imagen del producto,
precio unitario, disponibilidad.

Los productos que no estén disponibles se distinguirán por una leyenda roja de “agotado”. Se podrán visualizar pero no
será posible agregarlos al carrito de compras.

El sistema tendrá una barra de búsqueda en la cual se podrán buscar productos por nombre. El sistema también contará con
un filtro de productos en el cual se podrá seleccionar una o más características de forma que solo mostrará los productos
que cumplan con esas características. Los filtros son:  rango de precio, categoría, marca, material, popularidad  y ofertas.

Los usuarios podrán seleccionar un producto en el catálogo, lo que los redirigirá a la página del producto. En esta página
se mostrará toda la información del producto: nombre, imagen(es), descripción, precio unitario, cantidad de productos disponibles,
calificación promedio, opiniones. El sistema permitirá a los usuarios agregar el producto a su carrito de compras. El número
máximo de veces que se puede agregar un mismo producto al carrito de compras es equivalente al número de stock del producto.

"""

#Clases relacionadas
"""
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

--- Clase Inventario ---
    Atributos: 
        productos - Lista de productos. Tipo lista de objeto Productos. Acceso privado.
        stock - Número de stock de producto. Tipo entero. Acceso privado.
    Métodos:
        actualizarStock() - Permite actualizar el número de stock de un producto. Método privado.
    Conexiones: 
        Conexión 1 a 1 con Producto.
"""
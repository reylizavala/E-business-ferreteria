#Notificaciones

#Requerimientos
"""
El sistema le notificará al usuario si su compra fue aceptada mediante el canal de comunicación elegido. La notificación se enviará 
al usuario a través del canal de comunicación elegido (correo electrónico, SMS y notificación en el sistema en el apartado “Mis pedidos”) 
y deberá incluir un mensaje que informe que su pedido ha sido confirmado, con el número de identificación del pedido y un resumen de
la compra y el total.

El sistema notificará al usuario cuando el estado del pedido cambie. Los estados posibles son: en proceso, enviado, entregado, 
cancelado. El tiempo en el que el sistema detecta un cambio de estado del pedido no debe exceder los 5 segundos.

El sistema enviará notificaciones al usuario en tiempo real cuando el pedido se encuentre por llegar a su ubicación en la sección de 
notificaciones y por el medio de comunicación elegido (correo electrónico, SMS).

El sistema enviará una notificación al usuario informando si el pedido ha sido entregado. Esta notificación se activará cuando el 
estado del pedido cambie a “entregado”, y detallará el nombre y los datos de la persona que realizó la recolección del paquete.

El sistema debe proporcionar opciones para que el usuario personalice sus preferencias de notificación: medio de comunicación preferido 
(correo electrónico o sms), notificaciones dentro y fuera del sistema. 

El sistema enviará notificaciones al administrador al momento en el que un producto se haya vendido en la sección de notificaciones en 
el apartado de "Ventas”. Se mostrarán los detalles del producto vendido, el número de unidades vendidas, y el número identificador del 
pedido del que forman parte.

El sistema mostrará al administrador todos los pedidos realizados en el apartado de “Pedidos”. Se mostrará la información de cada 
pedido junto con su estado. El administrador recibirá notificaciones que indicarán el cambio de estado de los pedidos. 

El sistema enviará notificaciones al administrador en el caso de que haya problemas o modificaciones en la entrega del pedido bajo el 
apartado de “Problemas” dentro de la sección de “Pedidos”. El sistema enviará al administrador una notificación en caso de cancelación 
o devolución.

Las notificaciones deberán ser enviadas instantáneamente y no tardar más de 10 segundos en ser procesadas por el sistema.  
"""

#Clases relacionadas
"""
---Clase Notificaciones---
    Atributos: 
        idNotificacion - Número único identificador de notificación. Tipo entero. Acceso público.
        mensaje - Mensaje de la notificación. Tipo cadena. Acceso privado.
    Métodos:
        enviarNotificacion() - Permite al sistema enviar una notificación. Método privado.
    Conexiones: 
        Conexión N a 1 con Pedido.
"""
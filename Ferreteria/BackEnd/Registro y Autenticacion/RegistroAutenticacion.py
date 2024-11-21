# Registro y autenticación

#Requerimientos 
"""
El usuario podrá elegir la opción de crear o iniciar sesión en el sistema al navegar en el sistema sin tener una cuenta guardada.
Los usuarios no podrán entrar al resto del sistema sin antes iniciar sesión.

El sistema solicitará a los usuarios registrarse en caso de que no tengan una cuenta previamente. El apartado de registro solicitará
los siguientes campos: nombre del usuario, correo electrónico, número de teléfono, y contraseña.

El correo utilizado debe ser un correo válido y único por cuenta, de lo contrario el sistema no permitirá que se registre.

La contraseña necesita tener un mínimo de 8 caracteres y utilizar mínimo una letra mayúscula, una letra minúscula, un número y un
carácter especial. Se debe confirmar la contraseña dos veces para poder continuar. Las contraseñas deben coincidir. 

El inicio de sesión solicitará el correo electrónico asociado a una cuenta junto con la contraseña respectiva. El usuario tendrá
5 oportunidades para ingresar los datos correctos. Al fallar el quinto intento el sistema no permitirá más intentos y enviará una 
notificación al correo electrónico asociado a la cuenta informando sobre el intento fallido de acceso a la cuenta.

El sistema tendrá un método de verificación en dos pasos al iniciar sesión y enviará un correo con un número de confirmación de 5
dígitos al correo vinculado. El usuario deberá ingresar el código al sistema y al coincidir, se le permitirá acceso al sistema.
Este número es de tiempo limitado de 5 minutos y pasado el tiempo podrá solicitar otro código. 

El sistema contará con una base de datos la cual llevará el registro de todos los clientes que han iniciado sesión en la que existirá
la información que ingresó el usuario al registrarse y un número identificador de cliente con el que se identificará cada uno. 
"""

#Clases relacionadas
"""
--- Clase Usuario ---
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
"""
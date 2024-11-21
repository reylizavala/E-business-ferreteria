CREATE DATABASE Ferreteria_E_BUSINESS
GO
USE Ferreteria_E_BUSINESS
GO

CREATE TABLE Usuario(
ID_Usuario INT IDENTITY,
Nombre_Usuario VARCHAR(30) NOT NULL,
Correo VARCHAR(30) NOT NULL UNIQUE,
Telefono INT,
Contraseña VARCHAR (100)

CONSTRAINT PK_Usuario PRIMARY KEY (ID_Usuario)
)
GO

CREATE TABLE Metodo_Pago(
ID_Metodo_Pago INT IDENTITY,
Num_Tarjeta INT NOT NULL,
Fecha_Vencimiento DATE NOT NULL,
CVV INT NOT NULL,
ID_Usuario INT NOT NULL

CONSTRAINT PK_Metodo_Pago PRIMARY KEY (ID_Metodo_Pago)
CONSTRAINT FK_Usuario_MetodoPago FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario)
)
GO

CREATE TABLE Producto(
ID_Producto INT IDENTITY,
NombreProducto VARCHAR(100) NOT NULL,
Descripcion TEXT,
Precio DECIMAL(10, 2) NOT NULL,
Disponibilidad VARCHAR NOT NULL DEFAULT 'TRUE'

CONSTRAINT PK_Producto PRIMARY KEY (ID_Producto)
)
GO

CREATE TABLE Pedido(
ID_Pedido INT NOT NULL IDENTITY,
Estado_Pedido VARCHAR (50),
Direccion VARCHAR (50),
Total DECIMAL (10, 2) NOT NULL,
ID_Usuario INT NOT NULL,
ID_Producto INT NOT NULL

CONSTRAINT PK_Pedido PRIMARY KEY (ID_Pedido)
CONSTRAINT FK_Usuario_Pedido FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
CONSTRAINT FK_Producto_Pago FOREIGN KEY (ID_Producto) REFERENCES Producto(ID_Producto)
)
GO

CREATE TABLE Inventario(
Stock INT NOT NULL,
ID_Producto INT NOT NULL

CONSTRAINT FK_Producto_Inventario FOREIGN KEY (ID_Producto) REFERENCES Producto(ID_PRODUCTO)
)
GO

CREATE TABLE Pago(
ID_Pago INT NOT NULL IDENTITY,
Monto DECIMAL (10, 2) NOT NULL,
ID_Pedido INT NOT NULL,
ID_Metodo_Pago INT NOT NULL

CONSTRAINT PK_Pago PRIMARY KEY (ID_Pago),
CONSTRAINT FK_Pedido_Pago FOREIGN KEY (ID_Pedido) REFERENCES Pedido(ID_Pedido),
CONSTRAINT FK_MetodoPago_Pago FOREIGN KEY (ID_Metodo_Pago) REFERENCES Metodo_Pago(ID_Metodo_Pago)
)
GO

CREATE TABLE Notificaciones(
ID_Notificacion INT IDENTITY,
Mensaje TEXT NOT NULL,
ID_Pedido INT NOT NULL

CONSTRAINT PK_Notificaciones PRIMARY KEY (ID_Notificacion)
CONSTRAINT FK_Pedido_Notificaciones FOREIGN KEY (ID_Pedido) REFERENCES Pedido(ID_Pedido)
)
GO

CREATE TABLE Opinion(
ID_Opinion INT IDENTITY,
Contenido TEXT,
Calificacion INT NOT NULL CHECK (Calificacion between 1 and 5),
ID_Pedido INT NOT NULL

CONSTRAINT PK_Opinion PRIMARY KEY (ID_Opinion)
CONSTRAINT FK_Pedido_Opinion FOREIGN KEY (ID_Pedido) REFERENCES Pedido(ID_Pedido)
)
GO
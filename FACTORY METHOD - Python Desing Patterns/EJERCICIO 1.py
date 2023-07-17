# from abc import ABC, abstractmethod

# # Clase base abstracta para los productos
# class Product(ABC):
#     @abstractmethod
#     def operation(self):
#         pass

# # Clase de producto concreta
# class ConcreteProductA(Product):
#     def operation(self):
#         return "Operación del Producto A"

# # Clase de producto concreta
# class ConcreteProductB(Product):
#     def operation(self):
#         return "Operación del Producto B"

# # Clase creadora abstracta
# class Creator(ABC):
#     @abstractmethod
#     def factory_method(self):
#         pass

#     def some_operation(self):
#         product = self.factory_method()
#         result = f"El creador está utilizando {product.operation()}"
#         return result

# # Clase creadora concreta que implementa el Factory Method
# class ConcreteCreatorA(Creator):
#     def factory_method(self):
#         return ConcreteProductA()

# # Clase creadora concreta que implementa el Factory Method
# class ConcreteCreatorB(Creator):
#     def factory_method(self):
#         return ConcreteProductB()

# # Uso del Factory Method
# def main():
#     creator_a = ConcreteCreatorA()
#     print(creator_a.some_operation())

#     creator_b = ConcreteCreatorB()
#     print(creator_b.some_operation())

# if __name__ == "__main__":
#     main()


from abc import ABC, abstractmethod

# Clase base abstracta para las conexiones a bases de datos
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

# Clase de conexión a base de datos concreta: MySQL
class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Conectado a la base de datos MySQL")

# Clase de conexión a base de datos concreta: PostgreSQL
class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("Conectado a la base de datos PostgreSQL")

# Fábrica de conexiones a bases de datos
class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(database_type):
        if database_type == "MySQL":
            return MySQLConnection()
        elif database_type == "PostgreSQL":
            return PostgreSQLConnection()
        else:
            raise ValueError("Invalid database type")

# Uso de la fábrica de conexiones a bases de datos
def main():
    mysql_connection = DatabaseConnectionFactory.create_connection("MySQL")
    mysql_connection.connect()

    postgresql_connection = DatabaseConnectionFactory.create_connection("PostgreSQL")
    postgresql_connection.connect()

if __name__ == "__main__":
    main()

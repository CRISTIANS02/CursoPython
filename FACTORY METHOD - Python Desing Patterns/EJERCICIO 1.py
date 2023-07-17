class Product:
    def operation(self):
        pass
 # Clase concreta que implementa el producto
class ConcreteProduct(Product):
    def operation(self):
        print("Operación realizada por ConcreteProduct")
Clase creadora que contiene el Factory Method
class Creator:
    def factory_method(self):
        return ConcreteProduct()
     def some_operation(self):
        product = self.factory_method()
        product.operation()
 # Uso del patrón Factory Method
if __name__ == "__main__":
    creator = Creator()
    creator.some_operation()
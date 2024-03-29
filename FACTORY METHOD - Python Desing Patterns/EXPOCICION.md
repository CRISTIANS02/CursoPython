# Pseudocódigo
Este ejemplo ilustra cómo puede utilizarse el patrón Factory Method para crear elementos de interfaz de usuario (UI) multiplataforma sin acoplar el código cliente a clases UI concretas.


![Alt text](image.png)


 ## Ejemplo del diálogo multiplataforma.

La clase base de diálogo utiliza distintos elementos UI para representar su ventana. En varios sistemas operativos, estos elementos pueden tener aspectos diferentes, pero su comportamiento debe ser consistente. Un botón en Windows sigue siendo un botón en Linux.

Cuando entra en juego el patrón Factory Method no hace falta reescribir la lógica del diálogo para cada sistema operativo. Si declaramos un patrón Factory Method que produce botones dentro de la clase base de diálogo, más tarde podremos crear una subclase de diálogo que devuelva botones al estilo de Windows desde el Factory Method. Entonces la subclase hereda la mayor parte del código del diálogo de la clase base, pero, gracias al Factory Method, puede representar botones al estilo de Windows en pantalla.

Para que este patrón funcione, la clase base de diálogo debe funcionar con botones abstractos, es decir, una clase base o una interfaz que sigan todos los botones concretos. De este modo, el código sigue siendo funcional, independientemente del tipo de botones con el que trabaje.

Por supuesto, también se puede aplicar este sistema a otros elementos UI. Sin embargo, con cada nuevo método de fábrica que añadas al diálogo, más te acercarás al patrón Abstract Factory. No temas, más adelante hablaremos sobre este patrón.

La clase creadora declara el método fábrica que debe devolver
un objeto de una clase de producto. Normalmente, las
subclases de la creadora proporcionan la implementación de
este método.

    Class Dialog is

la creadora tambien puede proporcionar cierta implementacion por defecto del metodo de fabrica.

    abstrac method createButton(): Button

Observa que, a pesar de su nombre, la principal
responsabilidad de la creadora no es crear productos.
Normalmente contiene cierta lógica de negocio que depende
de los objetos de producto devueltos por el método
fábrica. Las subclases pueden cambiar indirectamente esa
lógica de negocio sobrescribiendo el método fábrica y devolviendo desde él un tipo diferente de producto.

    method render() is

 Invoca el método fábrica para crear un objeto de
producto.
Patrones creacionales 

    Button okButton = createButton()

 Ahora utiliza el producto.

    okButton.onClick(closeDialog)
    okButton.render()


Los creadores concretos sobrescriben el método fábrica para
cambiar el tipo de producto resultante.

    class WindowsDialog extends Dialog is
            method createButton():Button is
                return new WindowsButton()

    class WebDialog extends Dialog is
        method createButton():Button is
            return new HTMLButton()


La interfaz de producto declara las operaciones que todos los productos concretos deben implementar.

        interface Button is
            method render()
            method onClick(f)

Los productos concretos proporcionan varias implementaciones
 de la interfaz de producto.

    class WindowsButton implements Button is
    method render(a, b) is

Representa un botón en estilo Windows.

    method onClick(f) is
Vincula un evento clic de OS nativo.

    class HTMLButton implements Button is
    method render(a, b) is
        Devuelve una representación HTML de un botón.
    method onClick(f) is
        Vincula un evento clic de navegador web.

class Application is
    field dialog: Dialog
 La aplicación elige un tipo de creador dependiendo de la configuración actual o los ajustes del entorno. 

     method initialize() is
        config = readApplicationConfigFile()

        if (config.OS == "Windows") then
            dialog = new WindowsDialog()
        else if (config.OS == "Web") then
            dialog = new WebDialog()
        else
            throw new Exception("Error! Unknown operating system.")
            
El código cliente funciona con una instancia de un
creador concreto, aunque a través de su interfaz base.
Siempre y cuando el cliente siga funcionando con el creador a través de la interfaz base, puedes pasarle cualquier subclase del creador.

     method main() is
        this.initialize()
        dialog.render()











# ejemplo  en Python del patrón Factory Method:

Clase base para el producto

    class Product:
        def operation(self):
            pass

Clase concreta que implementa el producto

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


Uso del patrón Factory Method

    if __name__ == "__main__":
        creator = Creator()
        creator.some_operation()



En este ejemplo, la clase  Product  es la clase base para todos los productos.  ConcreteProduct  es una implementación concreta de  Product  que realiza una operación específica. 
 
La clase  Creator  es la clase creadora que contiene el Factory Method. En este caso, el Factory Method  factory_method  simplemente devuelve una instancia de  ConcreteProduct . El método  some_operation  utiliza el Factory Method para crear un objeto y realizar una operación en él. 
 
Al ejecutar el código, se crea una instancia de  Creator  y se llama al método  some_operation . Esto resulta en la creación de un objeto  ConcreteProduct  y la realización de la operación definida en esa clase. 
 
Espero que este ejemplo más simple te ayude a comprender mejor el patrón Factory Method en Python. Si tienes alguna otra pregunta, no dudes en preguntar.
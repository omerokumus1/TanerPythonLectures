# Define a class
# weakly typed language - strongly typed language
def f3():
    print("f3 static method is called")


class Car:
    # Property: objenin özellikleridir. Örneğin aşağıdaki brand, model, price, age Car objelerinin özelliklerini temsil eder
    def __init__(self, brand, model: str, price: int):  # type enforcement
        self.brand = brand
        self.model = model
        self.price = price
        self.age = 0  # default value
        print(price/3)

    # Operation: objenin yaptığı işlerdir/işlevlerdir. Her bir instance method objenin bir işlevidir
    def f1(self):  # instance methodlarda self parametresi olmak zorunda
        print("f1 instance method is called on " + self.model)

    def f2(self):  # self keyword'ü kullanılmadı. Bundan dolayı static hale çevrilebilir fakat şu an instance method olarak tanımlandı
        print("f2 static method is called ")


car1 = Car("Toyota", "F-150", 40000)
car2 = Car("Tesla", "Roadstar", 35000)

print(car1)
print(car1.price)

# Instance method:
#   Çalışabilmesi için o class'tan üretilmiş bir objeye ihtiyacı var. Bu objenin ÜZERİNE çağırılır

car1.f1()  # car1.f1 olduğu için ÜZERİNE çağırılır denir. class içerisindeki self kelimesi car1'in kendisi olur
car2.f1()  # class içerisindeki self kelimesi car2'nin kendisi olur


# Static method: Çalışabilmesi için herhangibir objeye ihtiyacı yoktur, herhangi bir objenin üzerine çağırılmaz
# Aşağıdaki çıktılar car1 veya car2 objelerinden bağımsızdır. Çünkü f2 fonksiyonu kendi body'sinde self keyword'ünü kullanmaz.
# Bu sebeple f2 static hale çevrilebilir.
car1.f2()
car2.f2()
# f2()  # bu şekilde çağırım yapılmaz. Çünkü f2 fonksiyonu instance olarak tanımlandı


# Static function vs Instance method
#   Bir fonksiyon class içinde tanımlanmış ise instance method olur
#   Bir fonksiyon class dışında tanımlı ise static function olur
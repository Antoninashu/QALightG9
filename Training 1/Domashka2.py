# Домашнє завдання №2: Робота з класами

# Preconditions:
# 1. Створити клас Human, в якому визначити метод drink.
# При ініціалізації, приймати вік людини; створити поле класу favorite_drink зі значенням 'beer'.
# 2. Створити клас Worker, віднаслідувавши його від Human, та додавши при ініціалізації зарплату.

# Завдання:
# 1. Реалізувати метод drink, так щоб він виводив в консоль назву поточного класу
# та додавав до неї відповідну дію та напій;
# Якщо людині менше 18 років, заміняти улюблений напій на 'juice'

# 1.1. Використовуючи даний клас, зробити виклик який:
# а) Виведе в консоль улюблений напій людини
# б) Виведе в консоль всю фразу, наприклад "Human likes drink beer"
# якщо людині більше 18 років, та "Human likes drink juice" якщо ні.

# 2. Перевизначити в класі Worker улюблений напій таким чином,
# щоб коли зарплата людини більша за 1000, то він змінювався на 'whiskey'
# Вивести в консоль все так само як в першому завданні, але з урахуванням зарплати.

class Human:
    favorite_drink = 'beer'

    def __init__(self, age):
        self.age = age
        if self.age < 18:
            self.favorite_drink = 'juice'

    def drink(self):
        print(f'{self.__class__.__name__} likes drink {self.favorite_drink}')


class Worker(Human):

    def __init__(self, age, salary):
        super().__init__(age)
        self.salary = salary
        if salary > 1000:
            self.favorite_drink = 'wiskey'


Dima = Worker(14, 5000)
Dima.drink()

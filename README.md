# Тестируем классы интернет-магазина
Вам нужно реализовать и протестировать классы интернет-магазина.
Все места, которые нужно дописать как в тестах, так и классах, отмечены `# TODO`.

При реализации обращайте внимание на типизацию аргументов методов и возвращаемых значений.
Так же обратите внимание на организацию тестов в файле с тестами:
- Тесты сгруппированы по классу, который они тестируют.
- Каждый тест называется именем соответствующего ему метода.

Вы можете начать как с реализации классов, так и с тестов.


# Дополнительные вопросы:
1. С чего проще начать выполнение домашнего задания: с тестов или с реализации классов?
2. Почему для хранения товаров в корзине используется словарь, а не список?
3. Зачем нужен __hash__ в классе Product? Изучите этот метод и объясните, почему он нужен.

# Изученные темы
1. Инкапсуляция
Самодокументируемость кода, а так же соблюдение принципов вроде DRY и KISS
позволяет избежать дублирования кода и упростить его поддержку.

2. Объектный подход - абстракция
Класс - это абстракция, которая описывает поведение и состояние объекта.
Экземпляр - это конкретный объект, который создан на основе класса.

3. Наследование
Наследование позволяет создавать новые классы на основе уже существующих.
Новый класс может расширять функциональность существующего, а так же переопределять его поведение.

4. Полиморфизм
Полиморфизм позволяет использовать один и тот же интерфейс для разных типов объектов.


5. Модули и классы
Файлы и папки в Python - это модули. 
Модули могут содержать в себе функции, классы, переменные и другие объекты.

# Вопросы для самоконтроля:
- Для чего нужен self?
- Как используется __init__() в классе?
- Что такое @classmethod?
- Что такое @staticmethod?
- Что такое @property?
- Зачем нужны дата-классы?
- Какие типы данных удобно использовать с Enum?
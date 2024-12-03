from threading import Thread
from time import sleep

# Класс Knight, наследованный от Thread
class Knight(Thread):
    total_enemies = 100  # Общее количество врагов для всех рыцарей

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while Knight.total_enemies > 0:
            self.days += 1
            sleep(1)  # Симуляция одного дня сражения
            # Уменьшаем количество врагов
            Knight.total_enemies -= self.power
            # Если врагов стало меньше 0, обнуляем
            if Knight.total_enemies < 0:
                Knight.total_enemies = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {Knight.total_enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

# Основной блок программы
if __name__ == "__main__":
    # Создание объектов рыцарей
    first_knight = Knight("Sir Lancelot", 10)
    second_knight = Knight("Sir Galahad", 20)

    # Запуск потоков
    first_knight.start()
    second_knight.start()

    # Ожидание завершения потоков
    first_knight.join()
    second_knight.join()

    # Финальное сообщение
    print("Все битвы закончились!")
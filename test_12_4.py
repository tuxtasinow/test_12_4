import unittest
import logging
from rt_with_exceptions import Runner  # импортируем ваш класс Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',  # Режим записи с заменой файла
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Usain', speed=-5)  # Устанавливаем некорректное значение для скорости
            runner.walk()
            self.assertEqual(runner.distance, 5 * 10)  # Здесь тест упадет из-за некорректной скорости
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            runner = Runner(123, speed=10)  # Некорректное значение для имени (должна быть строка)
            runner.run()
            self.assertEqual(runner.distance, 20 * 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")


if __name__ == '__main__':
    unittest.main()

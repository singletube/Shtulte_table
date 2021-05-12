import sys
import random
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import QTimer, Qt
from interface import Ui_MainWindow
from config import hard, mid, Finaly_hard, Finaly_ez, ez

"""
    Импорт:

    Необходимых для работы программы библиотек
    Интерфейса программы
    Констант
"""


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pixmap = QPixmap('Mid.png')
        self.Picture.setPixmap(self.pixmap)
        self.pixmap_2 = QPixmap('back.jpg')
        self.BackPic.setPixmap(self.pixmap_2)
        self.StartButton.clicked.connect(self.start)
        self.Button.clicked.connect(self.cont)
        self.Button_2.clicked.connect(self.cont)
        self.Button_3.clicked.connect(self.cont)
        self.Button_4.clicked.connect(self.cont)
        self.Button_5.clicked.connect(self.cont)
        self.Button_6.clicked.connect(self.cont)
        self.Button_7.clicked.connect(self.cont)
        self.Button_8.clicked.connect(self.cont)
        self.Button_9.clicked.connect(self.cont)
        self.Button_10.clicked.connect(self.cont)
        self.Button_11.clicked.connect(self.cont)
        self.Button_12.clicked.connect(self.cont)
        self.Button_13.clicked.connect(self.cont)
        self.Button_14.clicked.connect(self.cont)
        self.Button_15.clicked.connect(self.cont)
        self.Button_16.clicked.connect(self.cont)
        self.Button_17.clicked.connect(self.cont)
        self.Button_18.clicked.connect(self.cont)
        self.Button_19.clicked.connect(self.cont)
        self.Button_20.clicked.connect(self.cont)
        self.Button_21.clicked.connect(self.cont)
        self.Button_22.clicked.connect(self.cont)
        self.Button_23.clicked.connect(self.cont)
        self.Button_24.clicked.connect(self.cont)
        self.Button_12.clicked.connect(self.cont)
        self.help.clicked.connect(self.podskazka)
        self.lider_dif.currentIndexChanged.connect(self.ld_cn)
        self.Podskazka.setReadOnly(True)
        self.Podskazka.hide()
        self.osh_count = 0
        self.podskact = False
        self.first_num = 0
        con = sqlite3.connect('Winer_list.db')
        cur = con.cursor()
        b = self.lider_dif.currentText()
        result = cur.execute(
            f"""SELECT * from Records
                        WHERE Dificulty =(
                        SELECT id FROM Dificulty_list
                    WHERE Hard_level = '{self.lider_dif.currentText()}')""").fetchall()

        def sort(i):
            return i[2]

        self.Cheats = False

        result = sorted(result, key=sort)
        for elem in result:
            elem = f'{str(elem[0])}\t{b}\t{str(elem[2])}'
            self.Records.addItem(str(elem))
        con.close()
        self.DisableButtons()

        """
        Задание Изначальных параметров
        """

    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.ShiftModifier:
            if event.key() == Qt.Key_P or \
                    event.key() == 1047:
                if self.Cheats:
                    try:
                        if self.Dificulty.currentText() == ez:
                            d = 1
                        elif self.Dificulty.currentText() == mid:
                            d = 2
                        elif self.Dificulty.currentText() == hard:
                            d = 3
                        self.Player.setText('Вы Выиграли!!!')
                        self.timer_game.stop()
                        self.win_time = self.Time()
                        name = self.Ask_name()
                        self.Add_to_records(name, d)
                        self.ld_cn()
                    except AttributeError:
                        pass

            elif event.key() == Qt.Key_Q or \
                    event.key() == 1049:
                self.Mesbox()

            elif event.key() == Qt.Key_H or \
                    event.key() == 1056:
                self.podskazka()

            elif event.key() == Qt.Key_C or \
                    event.key() == 1057:
                if self.Cheats:
                    self.Cheats = False
                else:
                    self.Cheats = True

            elif event.key() == Qt.Key_W or \
                    event.key() == 1062:
                self.start()

            elif event.key() == Qt.Key_T or \
                    event.key() == 1045:
                if self.Cheats:
                    self.secs = 0

            elif event.key() == Qt.Key_D or \
                    event.key() == 1042:
                self.ChangeBack()

                self.pixmap_2 = QPixmap(fname)
                self.BackPic.setPixmap(self.pixmap_2)
            elif event.key() == Qt.Key_M or \
                    event.key() == 1068:
                self.Hard_help()

            elif event.key() == Qt.Key_O or \
                    event.key() == 1065:
                self.Mid_help()

            elif event.key() == Qt.Key_U or \
                    event.key() == 1043:
                self.Ez_help()

        """
        Задача горячих клавиш
        """

    def Ez_help(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("\tЛегкий режим")
        msgBox.setText("Счет идет с одного до 24.\n"
                       "Отмечать кнопки нужно\n"
                       "Т.Е. 1-2-3 и тд.\n"
                       "Последняя цифра отображается.\n"
                       "Все кнопки белого цвета.\n"
                       "После того как вы ответили цифра\n"
                       "блокируется\n"
                       "\t\tУдачи")
        msgBox.exec()

    def Mid_help(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("\tСредний режим")
        msgBox.setText("Счет идет с одного до 24.\n"
                       "Отмечать кнопки нужно\n"
                       "Т.Е. 1-2-3 и тд.\n"
                       "Последняя цифра отображается.\n"
                       "Все кнопки разного цвета.\n"
                       "После того как вы ответили цифра\n"
                       "блокируется и меняет цвет\n"
                       "\t\tУдачи")
        msgBox.exec()

    def Hard_help(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("\tСложный режим")
        msgBox.setText("Сложный режим - настоящее испытание для вас\n"
                       "Счет идет с одного до 47.\n"
                       "Отмечать кнопки нужно через 1\n"
                       "Т.Е. 1-3-5 и тд.\n"
                       "Последняя цифра не отображается.\n"
                       "Все кнопки разного цвета.\n"
                       "После того как вы ответили цифра\n"
                       "не блокируется и не меняет цвет\n"
                       "\t\tУдачи")
        msgBox.exec()

    def ChangeBack(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать фон', '',
            'Картинка (*.jpg)')[0]

        self.pixmap_2 = QPixmap(fname)
        self.BackPic.setPixmap(self.pixmap_2)

        """
        Функция Смены Заднего фона
        """

    def Mesbox(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Горячие клавиши")
        msgBox.setText("Shift + q - Просмотр Горячих клавиш\n"
                       "Shift + H - Показать подсказку\n"
                       "Shift + W - Начать игру\n"
                       "Shift + u - Показать подсказку для\n"
                       "легкого режима\n"
                       "Shift + o - Показать подсказку для\n"
                       "среднего режима\n"
                       "Shift + m - Показать подсказку для\n"
                       "сложного режима\n"
                       "Shift + d - Сменить фон\n"
                       "Shift + c - Включить читы\n"
                       "    -ПРИ ВКЛЮЧЕННЫХ ЧИТАХ-\n"
                       f"       Читы -{'Включены' if self.Cheats else 'Выключенны'}\n"
                       "Shift + p - Завершить игру\n"
                       "Shift + t - Обнулить время")
        msgBox.exec()

        """
        Функция для показа подсказки
        """

    def ld_cn(self):
        self.Records.clear()
        con = sqlite3.connect('Winer_list.db')
        cur = con.cursor()
        b = self.lider_dif.currentText()
        result = cur.execute(
            f"""SELECT * from Records
                WHERE Dificulty =(
                SELECT id FROM Dificulty_list
            WHERE Hard_level = '{self.lider_dif.currentText()}')""").fetchall()
        for elem in sorted(result):
            elem = f'{str(elem[0])}\t{b}\t{str(elem[2])}'
            self.Records.addItem(str(elem))
        con.close()

        """
        Обновление Таблицы рекордов
        """

    def podskazka(self):
        if self.podskact:
            self.Podskazka.hide()
            self.podskact = False
        else:
            self.Podskazka.show()
            self.podskact = True

        """
        Показать/спрятать подсказку
        """

    def cont(self):
        self.Dificulty.hide()
        if self.Dificulty.currentText() == hard:
            self.cont_hd()
        elif self.Dificulty.currentText() == mid:
            self.cont_md()
        elif self.Dificulty.currentText() == ez:
            self.cont_ez()
        if self.first_num == Finaly_ez or \
                self.first_num == Finaly_hard:
            if self.Dificulty.currentText() == ez:
                d = 1
            elif self.Dificulty.currentText() == mid:
                d = 2
            elif self.Dificulty.currentText() == hard:
                d = 3

            self.Player.setText('Вы Выиграли!!!')
            self.timer_game.stop()
            self.win_time = self.Time()
            name = self.Ask_name()

            self.Add_to_records(name, d)
            self.DisableButtons()
            self.Dificulty.show()
            self.ld_cn()
        """
        Определение нажатой цифры и проверка на победу
        """

    def Add_to_records(self, name, d):

        con = sqlite3.connect('Winer_list.db')

        cur = con.cursor()

        names = cur.execute('''SELECT Nickname from Records''')
        names = [str(*x) for x in names]
        if not name in names:
            cur.execute(
                f"""INSERT INTO Records VALUES ('{name}', {d}, '{self.win_time}')""").fetchall()
        else:
            cur.execute(f"""UPDATE Records
                            SET Time = '{self.win_time}'
                            WHERE Nickname = '{name}'""").fetchall()
        con.commit()

    """
    Добавление в таблицу рекордов:
    Имени
    Сложности
    Времени
    
    Перезапсь в случае существования анологичной записи в базе данных
    """

    def start(self):
        self.secs = 0
        self.timer_game = QTimer()
        for i in [self.Button, self.Button_2, self.Button_3, self.Button_4, self.Button_5, self.Button_6,
                  self.Button_7, self.Button_8, self.Button_9, self.Button_10, self.Button_11, self.Button_12,
                  self.Button_13, self.Button_14, self.Button_15, self.Button_16, self.Button_17, self.Button_18,
                  self.Button_19, self.Button_20, self.Button_21, self.Button_22, self.Button_23,
                  self.Button_24]:
            i.setDisabled(False)
        self.Player.setText('Завершите, чтобы начать сначала')
        self.timer_game.timeout.connect(self.tick)
        self.timer_game.start(1000)
        if self.Dificulty.currentText() == hard:
            self.first_num = -1
            self.start_hd()
            self.Counter.display('lol')
        elif self.Dificulty.currentText() == mid:
            self.first_num = 0
            self.start_md()
            self.Counter.display(0)
        elif self.Dificulty.currentText() == ez:
            self.osh_count = 0
            self.first_num = 0
            self.start_ez()
            self.Counter.display(0)

        """
        Включение активности клавиш
        
        Начало:
        Игры
        Таймера
        """

    def start_ez(self):

        a = [str(x) for x in range(1, 25)]
        b = [self.Button, self.Button_2, self.Button_3, self.Button_4, self.Button_5, self.Button_6,
             self.Button_7, self.Button_8, self.Button_9, self.Button_10, self.Button_11, self.Button_12,
             self.Button_13, self.Button_14, self.Button_15, self.Button_16, self.Button_17, self.Button_18,
             self.Button_19, self.Button_20, self.Button_21, self.Button_22, self.Button_23,
             self.Button_24]
        for i in range(0, 24):
            b[i].setText(a.pop(random.randint(0, len(a) - 1)))
            b[i].setStyleSheet(f"background-color: {0, 0, 0}")

        """
        Подготовка к игре на легом уровне сложности
        """

    def start_md(self):
        a = [str(x) for x in range(1, 25)]
        c = []
        for i in range(24):
            d = QColor(random.randint(10, 200), random.randint(10, 200), random.randint(10, 200))
            if d not in c:
                c.append(d)
        b = [self.Button, self.Button_2, self.Button_3, self.Button_4, self.Button_5, self.Button_6,
             self.Button_7, self.Button_8, self.Button_9, self.Button_10, self.Button_11, self.Button_12,
             self.Button_13, self.Button_14, self.Button_15, self.Button_16, self.Button_17, self.Button_18,
             self.Button_19, self.Button_20, self.Button_21, self.Button_22, self.Button_23,
             self.Button_24]
        for i in range(0, 24):
            b[i].setText(a.pop(random.randint(0, len(a) - 1)))
            b[i].setStyleSheet(f"background-color: {c[i].name()}")

    """
    Подготовка к игре на Среднем уровне сложности
    """

    def start_hd(self):
        a = [str(x) for x in range(1, 49, 2)]
        c = []
        for i in range(24):
            d = QColor(random.randint(10, 200), random.randint(10, 200), random.randint(10, 200))
            if d not in c:
                c.append(d)
        b = [self.Button, self.Button_2, self.Button_3, self.Button_4, self.Button_5, self.Button_6,
             self.Button_7, self.Button_8, self.Button_9, self.Button_10, self.Button_11, self.Button_12,
             self.Button_13, self.Button_14, self.Button_15, self.Button_16, self.Button_17, self.Button_18,
             self.Button_19, self.Button_20, self.Button_21, self.Button_22, self.Button_23,
             self.Button_24]
        for i in range(0, 24):
            b[i].setText(a.pop(random.randint(0, len(a) - 1)))
            b[i].setStyleSheet(f"background-color: {c[i].name()}")

    """
    Подготовка к игре на Сложном уровне сложности
    """

    def cont_ez(self):
        try:
            self.second_num = int(self.sender().text())
            if self.second_num - self.first_num == 1 or \
                    self.second_num == self.first_num:
                self.first_num = self.second_num
                self.Counter.display(self.first_num)
                self.sender().setDisabled(True)
                self.sender().setText('')
            else:
                if self.osh_count == 2:
                    self.Counter.display('Error')
                    self.Dificulty.show()
                    self.Player.setText('Вы проиграли :(')
                    self.DisableButtons()
                else:
                    self.osh_count += 1
                    self.Player.setText(f'Вы ошиблись {self.osh_count} из 3х раз')
        except ValueError:
            pass

        """
        Обработка правильности нажатия для легкой сложности
        """

    def cont_md(self):
        try:
            self.second_num = int(self.sender().text())
            self.sender().setText('')
            self.sender().setDisabled(True)
            self.sender().setStyleSheet(f"background-color: {0, 0, 0}")
            if self.second_num - self.first_num == 1 or \
                    self.second_num == self.first_num:
                self.first_num = self.second_num
                self.Counter.display(self.first_num)
            else:
                self.Counter.display('Error')
                self.Dificulty.show()
                self.Player.setText('Вы Проиграли :(')
                self.DisableButtons()
        except ValueError:
            pass

        """
        Обработка правильности нажатия для средней сложности
        """

    def cont_hd(self):
        try:
            self.second_num = int(self.sender().text())
            if self.second_num - self.first_num == 2 or \
                    self.second_num == self.first_num:
                self.first_num = self.second_num
                self.Counter.display('lol')
            else:
                self.Counter.display('Error')
                self.Dificulty.show()
                self.Player.setText('Вы Проиграли :(')
                self.DisableButtons()
        except ValueError:
            pass

        """
        Обработка правильности нажатия для сложной сложности
        """

    def tick(self):
        self.secs += 1
        self.timer.display(str(self.Time()))

        """
        Добавление секунды,Обновление дисплея
        """

    def Time(self):
        m = self.secs // 60
        s = self.secs % 60
        if len(str(m)) != 2:
            m = '0' + str(m)
        if len(str(s)) != 2:
            s = '0' + str(s)
        return f'{m}:{s}'

    """
    Подсчет времени
    """

    def DisableButtons(self):
        for i in [self.Button, self.Button_2, self.Button_3, self.Button_4, self.Button_5, self.Button_6,
                  self.Button_7, self.Button_8, self.Button_9, self.Button_10, self.Button_11, self.Button_12,
                  self.Button_13, self.Button_14, self.Button_15, self.Button_16, self.Button_17, self.Button_18,
                  self.Button_19, self.Button_20, self.Button_21, self.Button_22, self.Button_23,
                  self.Button_24]:
            i.setDisabled(True)

    """
    Перевод клавиш в неактивное состояние
    """

    def Ask_name(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                f"Ваше время {self.win_time}, как тебя зовут, победитель?")
        if ok_pressed:
            if name.strip() == '':
                name = 'Аноним'
        else:
            name = 'Аноним'
        return name

    """
    Ввод имени победителя
    """


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

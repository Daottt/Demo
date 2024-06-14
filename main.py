from PySide6.QtWidgets import QApplication, QMainWindow
from src.database.DataBaseManager import DataBaseManager
from src.ui.main_ui import Ui_MainWindow

TabelData = {"Task": ["ID", "ФИО мастера", "ФИО клиента"]}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db = DataBaseManager("service.db")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.enter.clicked.connect(self.login)
        self.ui.reg.clicked.connect(self.register)
        self.ui.reg_a.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.cancel.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        self.ui.logout.clicked.connect(self.logout)

    def login(self):
        data = self.db.login(self.ui.login.text(), self.ui.password.text())
        if not data:
            self.ui.auth_tip.setText("Неверный логин или пароль")
            return
        self.ui.stackedWidget.setCurrentIndex(2)

    def register(self):
        if self.ui.r_login.text() == "" or self.ui.r_password.text() == "":
            print("логин или пароль пусты")
            return

        if self.db.check_login(self.ui.r_login.text()):
            print("логин уже занят")
            return

        data = {
            "fio": self.ui.fio.text(),
            "phone_number": self.ui.phone.text(),
            "login": self.ui.r_login.text(),
            "password": self.ui.r_password.text(),
            "user_type_id": self.ui.user_type.currentIndex() + 1
        }
        self.db.create("Users", data)
        self.ui.stackedWidget.setCurrentIndex(0)

    def logout(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.auth_tip.setText("")

    def show_tasks(self):
        data = self.db.get_tasks()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

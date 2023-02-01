# Задача 3: Создайте программу для игры в "Крестики-нолики".

# from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QApplication, QCheckBox
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
#
#
# class Button(QPushButton):
#     def __init__(self, text):
#         super().__init__()
#
#         self.setText(f'{text}')
#         self.setFixedSize(150, 150)
#
#         self.setStyleSheet("""  QPushButton:!hover {border : 1px solid gray;}
#                                 QPushButton: hover {border : 1px solid lightgreen;}
#                                 QPushButton:pressed{border : 2px solid lightgreen;}
#                            """)
#         self.setFont(QFont("Times", 100, QFont.Bold))
#
#
# class Game(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.label_change = QLabel("Выберите, кто\nначнёт\n(по умолчанию\nначинает O):")
#         self.label_x = QLabel("X")
#         self.label_o = QLabel("O")
#         self.check_box_x = QCheckBox()
#         self.check_box_o = QCheckBox()
#         self.reset = QPushButton("Сброс")
#
#
#         layout = QGridLayout(self)
#
#         for step in range(9):
#             btn = Button(' ')
#             btn.clicked.connect(lambda but, b=btn: self.onClicked(b))
#             layout.addWidget(btn, step // 3, step % 3)
#             self.reset.clicked.connect(lambda text, b = btn: self.clear_btn(b))
#         layout.addWidget(self.label_change, 0, 4, 1, 2, Qt.AlignTop)
#         layout.addWidget(self.label_x, 1, 4, Qt.AlignRight)
#         layout.addWidget(self.label_o, 2, 4, Qt.AlignRight)
#         layout.addWidget(self.check_box_x, 1, 4, 1, 2, Qt.AlignLeft)
#         layout.addWidget(self.check_box_o, 2, 4, 1, 2, Qt.AlignLeft)
#         layout.addWidget(self.reset, 2, 4, 1, 2, Qt.AlignBottom)
#
#     def onClicked(self, btn):
#         if self.check_box_x.isChecked():
#             btn.setText("X")
#             self.check_box_x.setChecked(False)
#             self.check_box_o.setChecked(True)
#         else:
#             btn.setText("O")
#             self.check_box_x.setChecked(True)
#             self.check_box_o.setChecked(False)
#
#     def clear_btn(self, btn):
#         btn.setText(' ')
#
#     def clear_text(self, btn):
#         btn.setText(' ')
#
#
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     w = Game()
#     w.show()
#     sys.exit(app.exec_())
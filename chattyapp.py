import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Chatty")
window.resize(1000, 700)

browser = QWebEngineView()
browser.setUrl(QUrl("https://chatty.ct.ws/"))  # <-- tutaj opakowujemy string w QUrl
window.setCentralWidget(browser)

window.show()
sys.exit(app.exec_())

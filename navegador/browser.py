from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cypher")
        self.resize(1920, 1080)

        self.criar_interface()
    
    def criar_interface(self):

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout_principal = QVBoxLayout()
        central_widget.setLayout(layout_principal)

        # Barra de navegação
        barra_navegacao = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Digite uma URL...")

        self.botao_ir = QPushButton("Ir")

        barra_navegacao.addWidget(self.url_bar)
        barra_navegacao.addWidget(self.botao_ir)

        layout_principal.addLayout(barra_navegacao)
        

        self.browser_view = QWebEngineView()
        print(type(self.browser_view))

        self.browser_view.setUrl(QUrl("https://wikipedia.org"))
        layout_principal.addWidget(self.browser_view)

        self.botao_ir.clicked.connect(self.carregar_url)
        self.url_bar.returnPressed.connect(self.carregar_url)

    def carregar_url(self):
        url = self.url_bar.text()
        print("URL digitada:", url)

        if not url.startswith("http"):
            url = "https://" + url

        print("URL final:", url)

        self.browser_view.setUrl(QUrl(url))
        
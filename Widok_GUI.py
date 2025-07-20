# Widok GUI
class GUIWidok(Obserwator):
    def __init__(self):
        # Konstruktor, który tworzy aplikację, okno i układ widoku
        # - Zainicjalizuj aplikację PyQt5, okno i widok
        # - Utwórz QGraphicsScene i QGraphicsView do rysowania komórek na planszy
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.layout = QVBoxLayout(self.window)
        self.label = QLabel("Gra w Życie", self.window)
        self.layout.addWidget(self.label)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self.window)
        self.layout.addWidget(self.view)
        self.window.setLayout(self.layout)
        self.window.setWindowTitle("Życie")
        self.window.show()
        pass

    def aktualizuj(self, plansza):
        # Metoda dodająca komórkę do widoku, rysując ją na planszy
        # - Jeśli komórka jest żywa, narysuj ją jako np. kolorowy prostokąt w odpowiednich współrzędnych
        # wykorzystaj metody scene.clear(), QGraphicsRectItem.setBrush(Qt.blue), scene.addItem(QGraphicsRectItem(params))

        pass
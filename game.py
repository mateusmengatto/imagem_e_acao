import random
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PySide6.QtGui import QFont

class RandomWordsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Definir as listas de palavras
        self.lista1 = self.load_words_from_file(r"listas_palavras\facil.txt")
        self.lista2 = self.load_words_from_file(r"listas_palavras\dificil.txt")
        self.lista3 = self.load_words_from_file(r"listas_palavras\filmes.txt")
        self.lista4 = self.load_words_from_file(r"listas_palavras\frase.txt")
        self.listarepetida = []
        # Configurar a interface gráfica
        self.setWindowTitle("Gerador de Palavras Aleatórias")
        self.layout = QVBoxLayout()

        self.word_labels = []
        for _ in range(4):
            label = QLabel()
            label.setFont(QFont("Arial", 24))
            self.word_labels.append(label)
            self.layout.addWidget(label)

        self.generate_button = QPushButton("Jogar")
        self.generate_button.setFont(QFont("Arial", 24))
        self.generate_button.clicked.connect(self.generate_words)
        self.layout.addWidget(self.generate_button)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # Gerar as primeiras palavras
        self.generate_words()
    
    def load_words_from_file(self, filename):
        with open(filename, "r", encoding="utf8") as file:
            words = [line.strip() for line in file]
        return words

    def generate_words(self):
        # Gerar quatro palavras aleatóri         

        word1 = random.choice(self.lista1) 

        word2 = random.choice(self.lista2)

        word3 = random.choice(self.lista3)   

        word4 = random.choice(self.lista4)

        if word1 in self.listarepetida:
            word1 = random.choice(self.lista1) 
        if word2 in self.listarepetida:
            word2 = random.choice(self.lista2)
        if word3 in self.listarepetida:
            word3 = random.choice(self.lista3)   
        if word4 in self.listarepetida:
            word4 = random.choice(self.lista4)
        word1_a = f'Fácil             (2): {word1}'           
        word2_a = f'Difícil            (8): {word2}'           
        word3_a = f'Cinema        (4): {word3}'           
        word4_a= f'Frase           (5): {word4}'
        self.listarepetida.append(word1)           
        self.listarepetida.append(word2)           
        self.listarepetida.append(word3)           
        self.listarepetida.append(word4)           

        # Atualizar os rótulos com as palavras geradas
        self.word_labels[0].setText(word1_a)
        self.word_labels[1].setText(word2_a)
        self.word_labels[2].setText(word3_a)
        self.word_labels[3].setText(word4_a)

if __name__ == "__main__":
    app = QApplication([])
    window = RandomWordsApp()
    window.show()
    app.exec()

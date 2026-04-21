import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QLineEdit, QTextEdit
)
import statistics
from collections import Counter

class CalculadoraEstatistica(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Estatística")

        layout = QVBoxLayout()

        self.label = QLabel("Digite os números separados por vírgula:")
        layout.addWidget(self.label)

        self.input_dados = QLineEdit()
        layout.addWidget(self.input_dados)

        self.botao = QPushButton("Calcular")
        self.botao.clicked.connect(self.calcular)
        layout.addWidget(self.botao)

        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def calcular(self):
        texto = self.input_dados.text()

        try:
            dados = [float(x.strip()) for x in texto.split(",")]

            if len(dados) == 0:
                self.resultado.setText("Digite valores válidos.")
                return

            media = statistics.mean(dados)
            mediana = statistics.median(dados)

            # Moda
            contagem = Counter(dados)
            max_freq = max(contagem.values())
            modas = [k for k, v in contagem.items() if v == max_freq]

            if max_freq == 1:
                tipo_moda = "Amodal"
                moda_str = "Não há moda"
            else:
                if len(modas) == 1:
                    tipo_moda = "Unimodal"
                elif len(modas) == 2:
                    tipo_moda = "Bimodal"
                elif len(modas) == 3:
                    tipo_moda = "Trimodal"
                else:
                    tipo_moda = "Multimodal"

                moda_str = f"{modas} ({tipo_moda})"

            variancia = statistics.variance(dados) if len(dados) > 1 else 0
            desvio = statistics.stdev(dados) if len(dados) > 1 else 0
            coef_var = (desvio / media) * 100 if media != 0 else 0

            # Tabela de frequência
            tabela_freq = "Valor | Fi\n"
            tabela_freq += "-" * 15 + "\n"
            for valor, freq in sorted(contagem.items()):
                tabela_freq += f"{valor} | {freq}\n"

            resultado_texto = f"""
Média: {media:.2f}
Mediana: {mediana:.2f}
Moda: {moda_str}

Variância: {variancia:.2f}
Desvio Padrão: {desvio:.2f}
Coeficiente de Variação: {coef_var:.2f}%

Tabela de Frequência:
{tabela_freq}
"""

            self.resultado.setText(resultado_texto)

        except:
            self.resultado.setText("Erro: verifique os dados inseridos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = CalculadoraEstatistica()
    janela.show()
    sys.exit(app.exec_())


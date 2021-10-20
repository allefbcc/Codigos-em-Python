from pylab import plot, show, legend, title, xlabel, ylabel, axis
from matplotlib import pyplot as plt
import math


import PySimpleGUI as sg


sg.theme('Random')

layout = [
    [sg.Text('Informe os Valores:')],
    [sg.Text('Comprimento Inicial (m):', size=(22, 1,)), sg.InputText(size=(10,5))],
    [sg.Text('Diâmetro Inicial (m): ', size=(22, 1)), sg.InputText(size=(10,5))],
    [sg.Text('Força (N):', size=(22, 1)), sg.InputText(size=(10,5))],
    [sg.Text('Comprimento Instantâneo (m):', size=(22, 1)), sg.InputText(size=(10,5))],
    [sg.Text('Diâmetro Instantâneo', size=(22, 1)), sg.InputText(size=(10,5))],
    [sg.Submit('Registar'), sg.Cancel('Sair')]
]

window = sg.Window('IHM', layout)
event, values = window.read()
window.close()

sg.popup('Voce registrou os seguintes valores',
         'Comprimeno Inicial',values[0],
         'Diâmetro Inicial', values[1],
         'Força (N)', values[2],
         'Comprimento Instantâneo', values[3],
         'Diâmetro Instantâneo', values[4],

         title="Valores Registrados")

comprimento_Inicial = float(values[0])
diametro_Inicial = float(values[1])


forca = int(values[2])
comprimento_Instantaneo = float(values[3])
diametro_Instantaneo = float(values[4])


tensao_De_Engenharia = forca / ((diametro_Inicial / 2) ** 2) * 3.14
deformacao_De_Engenharia = (comprimento_Instantaneo - comprimento_Inicial) / comprimento_Inicial
tensao_Verdadeira = forca / ((diametro_Instantaneo / 2) ** 2) * 3.14
deformacao_Verdadeira = math.log(comprimento_Instantaneo / comprimento_Inicial)

sg.popup('Valores Calculados',
         'Tensão de Engenharia',tensao_De_Engenharia,
         'Deformação de Engenharia', deformacao_De_Engenharia,
         'Tensão Verdadeira', tensao_Verdadeira,
         'Deformação Verdadeira', deformacao_Verdadeira,

         'CLIQUE EM OK PARA GERAR O GRÁFICO',
         title="Valores Claculados")


engenharia = [deformacao_De_Engenharia, tensao_Verdadeira]
real = [deformacao_Verdadeira, tensao_De_Engenharia]

plot(engenharia, marker="o")
plot(real, marker="o")

title('Tensão vs Deformação')

xlabel('Deformação')
ylabel('Tensão (MPa)')
legend(['Engenharia','Real'])

axis(ymin=0,ymax=570000)
axis(xmin=0, xmax=2)

plt.grid()
show()



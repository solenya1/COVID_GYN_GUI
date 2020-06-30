import PySimpleGUI as sg
from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Configurando Plotagem
def draw_casos_acomulados():
    df1 = pd.read_csv('COVID19-GYN.csv')
    plt.plot(df1['data'], df1['casos'],
             label='Casos positivos confirmados')
    plt.xlabel('Data de notificação')
    plt.ylabel('Número de casos ')
    plt.title('Casos acomulados por data da notificação')
    plt.xticks(np.arange(1, df1['data'].max(), step=2))
    plt.annotate('abertura do comércio', xy=(23, 5561),
                 xytext=(21, 5000),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )
    plt.legend()
    plt.grid(True)
    plt.show(block=False)
def draw_casos_diarios():
    df2 = pd.read_csv('COVID19-GYN.csv')
    plt.bar(df2['data'], df2['casos diarios'], color='green')
    plt.xlabel('Data de Notificação')
    plt.yticks(np.arange(0, 550, step=50))
    plt.xticks(df2['data'])
    plt.ylabel('Registros diarios')
    plt.title('Número de casos por dia')
    plt.show(block=False)
def draw_obitos_diarios():
    df3 = pd.read_csv('COVID19-GYN.csv')
    MAX_DEATHS = df3['obitos diarios'].max()
    LAST_UPDATE_DATA = df3['data'].max()
    plt.bar(df3['data'], df3['obitos diarios'], color='red')
    plt.xlabel('Data de óbito', size=20)
    plt.xticks(df3['data'])
    plt.ylabel('Número de óbitos', size=20)
    plt.yticks(np.arange(0, 17))
    plt.title('Número de óbitos por data de evento', size=20)
    plt.plot([1, LAST_UPDATE_DATA], [MAX_DEATHS, MAX_DEATHS], 'b--')
    plt.annotate('MAIOR REGISTRO', xy=(1, 13.1), xytext=(1, 13.1), size=(15))
    plt.show(block=False)
def open_info():
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    browser = webdriver.Chrome(
        executable_path=r'./chromedriver', chrome_options=options
    )
    browser.get('https://saude.goiania.go.gov.br/goiania-contra-o-coronavirus/informe-epidemiologico-covid-19/')
sg.theme('Material2')

layout = [[sg.Text('COVID-19 GYN UI', size=(30,1), justification='center',
                   font=("Helvetica", 15))],
          [sg.Text('Clique para acessar as informações')],
          [sg.Button('Visualizar Informativos')],
          [sg.Text('Clique para visualizar os gráficos:')],
          [sg.Button('Casos acomulados')],
          [sg.Button('Casos diarios')],
          [sg.Button('Óbitos por data')]]

window = sg.Window('COVID INFO GUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Visualizar Informativos':
        open_info()
    if event == 'Casos acomulados':
        draw_casos_acomulados()
    if event == 'Casos diarios':
       draw_casos_diarios()
    if event == 'Óbitos por data':
        draw_obitos_diarios()


window.close()
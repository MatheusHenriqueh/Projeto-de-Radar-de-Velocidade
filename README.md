Este projeto simula o funcionamento básico de um radar de trânsito utilizando Python.
Ele verifica a velocidade de um veículo em relação ao limite permitido e determina se o motorista deve ser multado com base na posição do carro em relação ao radar.

🎯 Objetivo

Identificar se um veículo ultrapassou o limite de velocidade ao passar pela área monitorada pelo radar.

🧠 Lógica do Programa

O programa:

Recebe a velocidade atual do carro.

Recebe a posição atual do carro na estrada.

Compara a velocidade com o limite permitido.

Verifica se o carro está dentro da área de detecção do radar.

Informa se o motorista será multado ou não.

📌 Configurações do Radar

Velocidade máxima permitida: 50 km/h

Localização do radar: 80 metros

Área de detecção: 5 metros antes e depois do radar

🧾 Código
velocidade_do_seu_car = int(input("Qual a velocidade do seu carro no momento?"))
local_do_seu_car = int(input("O local do seu carro (exemplo: 100, 20, 123):"))

RADAR_VELOCIDADE_MAXIMA = 50
LOCAL_DO_RADAR = 80
RADAR_METROS = 5

multa = velocidade_do_seu_car > RADAR_VELOCIDADE_MAXIMA
n_multa = velocidade_do_seu_car < RADAR_VELOCIDADE_MAXIMA
local = LOCAL_DO_RADAR + RADAR_METROS  #85
local2 = LOCAL_DO_RADAR - RADAR_METROS #75
local3 = local2 <= local_do_seu_car <= local
local4 = local2 >= local_do_seu_car <= local

if local3 and multa:
    print(f"Você recebeu uma multa, pois está acima da velocidade de {RADAR_VELOCIDADE_MAXIMA}")
elif local3 or n_multa:
    print("Você não tomou multa, pois passou na velocidade baixa.")
elif local4 and n_multa:
    print("Não passou no radar ainda!")

▶️ Como Executar

Certifique-se de ter o Python instalado.

Salve o código em um arquivo radar.py

Execute no terminal:

python radar.py

📅 Data do Projeto

31/10/2025

👨‍💻 Autor

Matheus Ruivo

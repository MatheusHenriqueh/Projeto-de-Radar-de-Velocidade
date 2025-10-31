#Projeto de RADAR
#Autor: Matheus Ruivo
#Data: 31/10/25

velocidade_do_seu_car = int(input("Qual a velocidade do seu carro no momento?"))#exp: 50
local_do_seu_car = int(input("O local do seu carro (exemplo: 100, 20, 123):"))# 80

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
    print(F"Você recebeu uma multa, pois está acima da velocidade de {RADAR_VELOCIDADE_MAXIMA}")
elif local3 or n_multa:
    print("Você não tomou multa, pois passou na velocidade baixa.")
elif local4 and n_multa:
    print("Não passou no radar ainda!")
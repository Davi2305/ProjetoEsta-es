dia = int(input('Informe o dia em questão: \n'))
mes = int(input('Agora digite o mês: \n'))
if mes == 12 and 31 >= dia >=22 or mes==1 or mes==2 or mes==3 and dia<20:
    print(f'Na data {dia}/{mes}/2023 estaremos na estação "Verão"')
if mes == 4 and 31>= dia >=20 or mes == 5 or mes == 6 and dia < 21:
    print(f'Na data {dia}/{mes}/2023 estaremos na estação "Outono"')
if mes == 6 and 31>= dia >=21 or mes == 7 or mes == 8 or mes == 9 and dia < 23:
    print(f'Na data {dia}/{mes}/2023 estaremos na estação "Inverno"')
if mes == 9 and 31>= dia >=23 or mes == 10 or mes == 11 or mes == 12 and dia <22:
    print(f'Na data {dia}/{mes}/2023 estaremos na estação "Primavera"')
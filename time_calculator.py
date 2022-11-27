from datetime import datetime, timedelta

def add_time(arg_hora, tempo_acrescentado):
    hora = arg_hora
    hora_entrada = datetime.strptime(hora, "%I:%M %p")
    hora_saida = datetime.strftime(hora_entrada, "%H:%M")

    hora_saida_list = hora_saida.split(":")
    #concertar as coversões para int
    h = int(hora_saida_list[0])
    m = int(hora_saida_list[1])


    hora_add = tempo_acrescentado
    hora_add_list = hora_add.split(":")

    h_add = int(hora_add_list[0])
    m_add = int(hora_add_list[1])

    data = datetime(2019, 3, 1, h, m)
    data_dia = data.day

    add = timedelta(hours=h_add, minutes=m_add)

    data_final = data + add
    data_final_dia = data_final.day

    if data_final_dia - data_dia == 0:
        st = ''
    elif data_final_dia - data_dia == 1:
        st = '(next day)'
    elif data_final_dia - data_dia > 1:
        st = f'({data_final_dia - data_dia} days later)'

    hora_final = data_final.strftime("%I:%M %p")

    print(f'Returns: {hora_final} {st}')
     

add_time('06:30 PM', '205:12' )
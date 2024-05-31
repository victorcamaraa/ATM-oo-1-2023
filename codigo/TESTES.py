import datetime

def somar_meses(data, num_meses):
    data_resultante = data + datetime.timedelta(days=num_meses * 30)
    return data_resultante

data_inicial = datetime.datetime.now()  # Data inicial


print("Data resultante:", data_final.strftime("%d/%m/%Y"))

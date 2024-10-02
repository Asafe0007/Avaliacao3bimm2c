def escolher_sala(num_participantes):
    if num_participantes <= 3:
        return "Sala Pequena"
    elif num_participantes <= 10:
        return "Sala Média"
    else:
        return "Sala Grande"

def agendar_reuniao(num_participantes):
    sala = escolher_sala(num_participantes)
    return f"Reunião agendada na {sala} para {num_participantes} participantes."

num_participantes = int(input("Informe o número de participantes: "))
while num_participantes < 0:
    num_participantes = int(input("informe um número que não seja negativo: "))

print(agendar_reuniao(num_participantes))
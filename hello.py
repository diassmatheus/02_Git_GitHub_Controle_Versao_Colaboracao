import datetime
from mensagem import printa_mensagem, versao

print(f'Versão {versao}: {printa_mensagem()}')
print(f'Hora do print: {datetime.datetime.now()}')
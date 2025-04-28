from datetime import datetime

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))


print(f"Horário em Oslo: {data}")
print(f"Horário em São Paulo: {data2}")

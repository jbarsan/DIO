from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(f"Horário em Oslo utilizando somente o timezone python: {data_oslo}")
print(f"Horário em São Paulo utilizando somente o timezone ptyhon: {data_sao_paulo}")

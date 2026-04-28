import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Gerar datas (30 dias)
datas = [datetime(2026, 1, 1) + timedelta(days=i) for i in range(30)]

# Gerar valores aleatórios
valores = [random.randint(1, 100) for _ in range(30)]

# Criar DataFrame
df = pd.DataFrame({
    "data": datas,
    "quantidade": valores
})

# Plotar
plt.plot(df["data"], df["quantidade"])

plt.title("Dados Aleatórios")
plt.xlabel("Data")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Lista de acciones
tickers = ['AAPL', 'MSFT', 'GOOGL']

# Descargar datos históricos
data = yf.download(tickers, start='2020-01-01', end='2025-01-01')['Close']

# Calcular retornos diarios
returns = data.pct_change().dropna()

# Gráfico de retornos acumulados
(1 + returns).cumprod().plot(figsize=(10, 6))
plt.title('Retorno Acumulado del Portafolio')
plt.show()

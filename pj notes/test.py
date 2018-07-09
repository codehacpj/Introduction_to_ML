import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ram_prices = pd.read_csv('ram_price.csv')
plt.semilogy(ram_prices.date,ram_prices.price)
plt.xlabel("year")
plt.ylabel("Price in $/Mbyte")
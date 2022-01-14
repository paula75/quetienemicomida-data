
import pandas as pd
from data.lacteos import yogurts
from data.lacteos import leches

COLUMNAS = ['Marca', 'Tipo', 'Energía', 'Proteinas', 'Grasas', 'Hidratos de carbono', 'Grasas saturadas', 'Colesterol', 'Azúcar total', 'Sodio', 'Ingredientes', 'imagen']

def read_lacteos():
    yogurt_df = pd.DataFrame(data=yogurts, columns=COLUMNAS)
    leches_df = pd.DataFrame(data=leches, columns=COLUMNAS)

    print(yogurt_df)


if __name__ == '__main__':
    read_lacteos()

import numpy as np
from sklearn.tree import DecisionTreeRegressor

# Inicializamos la secuencia de datos y el modelo de Árbol de Decisión
sequence_length = 3  # Cuántos números anteriores usar para predecir
data = []
model = DecisionTreeRegressor()

def create_dataset(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i + sequence_length])
        y.append(data[i + sequence_length])
    return np.array(X), np.array(y)

def add_number_and_train(number):
    global data, model
    data.append(number)
    
    if len(data) > sequence_length:
        # Convertimos los datos en el conjunto adecuado para entrenar el modelo
        X, y = create_dataset(data, sequence_length)
        
        # Entrenamos el Árbol de Decisión
        model.fit(X, y)
        
        # Predecimos el próximo número en base a los últimos `sequence_length` números
        next_input = np.array([data[-sequence_length:]])
        prediction = model.predict(next_input)
        
        print(f"Basado en los últimos {sequence_length} números, el siguiente número probablemente será: {prediction[0]}")
    else:
        print(f"Se necesitan al menos {sequence_length} números para hacer una predicción.")

# Aquí puedes ir añadiendo números manualmente
while True:
    try:
        number = float(input("Introduce un número: "))
        add_number_and_train(number)
    except ValueError:
        print("Por favor, introduce un número válido.")

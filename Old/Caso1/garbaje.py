
def prueba_2():

    # Crear el problema de optimización
    prob = pulp.LpProblem("Maximize_Message_Success_Probability", pulp.LpMaximize)

    # Crear las variables X_ij
    X = np.array([[pulp.LpVariable(f"X_{i}_{j}", lowBound=0, cat=pulp.LpBinary) for j in range(42)] for i in range(42)])

    # Función objetivo linealizada
    FO_linealizada = np.sum(np.log(probabilities) * X) + np.sum(np.log(X_values) * X)

    # Agregar la función objetivo al problema
    prob += FO_linealizada

    # Restricciones: cada servidor solo puede recibir un mensaje y enviar un mensaje
    for i in range(42):
        prob += np.sum(X[i, :]) == 1  # Restricción de salida
        prob += np.sum(X[:, i]) == 1  # Restricción de entrada

    # Resolver el problema
    prob.solve()

    # Obtener la solución
    if pulp.LpStatus[prob.status] == "Optimal":
        print("Solución encontrada:")
        for i in range(42):
            for j in range(42):
                if pulp.value(X[i, j]) > 0:
                    print(f"Enviar mensaje de servidor {i+1} a servidor {j+1}")
    else:
        print("No se encontró una solución óptima.")
        
        






    if pulp.LpStatus[prob.status] == "Optimal":
        print("Solución encontrada:")
        for i in range(42):
            for j in range(42):
                if pulp.value(X[i, j]) > 0:
                    print(f"Enviar mensaje de servidor {i+1} a servidor {j+1}")
    else:
        print("No se encontró una solución óptima.")
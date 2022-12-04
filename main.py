from scipy.optimize import linprog

# ЛП 0
def doLinearProgNull():
    f = [1, 1, 1, 1, 1]
    A0 = [[-3, -15, -26, -38, -50],
          [-4, -3, -2, -1, -0]]
    b0 = [-40, -33]
    lb0 = [(0, float("inf")), (0, float("inf")), (0, float("inf")), (0, float("inf")), (0, float("inf"))]
    X0 = linprog(c=f, A_ub=A0, b_ub=b0, bounds=lb0, method="highs")
    print(X0)
    print("\n---------------------------------------------------------------------------------------------------------------\n")
    # fun: 8.549019607843137
    # x: array([7.35294118, 1.19607843, 0., 0., 0.])

# ЛП 1 – НИЖНЯЯ ГРАНИЦА
def doLinearProgOne():
    f = [1, 1, 1, 1, 1]
    A0 = [[-3, -15, -26, -38, -50],
          [-4, -3, -2, -1, -0]]
    b0 = [-40, -33]
    lb1 = [(0, 7), (0, 1), (0, float("inf")), (0, float("inf")), (0, float("inf"))]
    X1 = linprog(c=f, A_ub=A0, b_ub=b0, bounds=lb1, method="highs")
    print(X1)
    print(
        "\n---------------------------------------------------------------------------------------------------------------\n")


# Вызов ЛП решений
doLinearProgNull()
doLinearProgOne()

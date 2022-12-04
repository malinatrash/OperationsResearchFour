from pulp import LpMinimize, LpProblem, LpStatus, LpVariable


def doLinearProgNull():
    model0 = LpProblem(name="LP0", sense=LpMinimize)

    x01 = LpVariable(name="x01", lowBound=0)
    x02 = LpVariable(name="x02", lowBound=0)
    x03 = LpVariable(name="x03", lowBound=0)
    x04 = LpVariable(name="x04", lowBound=0)
    x05 = LpVariable(name="x05", lowBound=0)

    model0 += 1 * x01 + 1 * x02 + 1 * x03 + 1 * x04 + 1 * x05  # Целевая функция ЛП0
    model0 += 3 * x01 + 15 * x02 + 26 * x03 + 38 * x04 + 50 * x05 >= 40  # Ограничение 1
    model0 += 4 * x01 + 3 * x02 + 2 * x03 + 1 * x04 + 0 * x05 >= 33  # Ограничение 2

    model0.solve()

    print(f"status: {model0.status}, {LpStatus[model0.status]}")
    print(f"objective: {model0.objective.value()}")

    for var in model0.variables():
        print(f"{var.name}: {var.value()}")
    for name, constraint in model0.constraints.items():
        print(f"{name}: {constraint.value()}")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    # objective: 8.5490196
    # x1: 7.3529412
    # x2: 1.1960784
    # x3: 0.0
    # x4: 0.0
    # x5: 0.0


def doLinearProgOne():
    model1 = LpProblem(name="LP1", sense=LpMinimize)

    x11 = LpVariable(name="x11", lowBound=0)
    x12 = LpVariable(name="x12", lowBound=0)
    x13 = LpVariable(name="x13", lowBound=0)
    x14 = LpVariable(name="x14", lowBound=0)
    x15 = LpVariable(name="x15", lowBound=0)

    model1 += 1 * x11 + 1 * x12 + 1 * x13 + 1 * x14 + 1 * x15  # Целевая функция ЛП1
    model1 += 3 * x11 + 15 * x12 + 26 * x13 + 38 * x14 + 50 * x15 >= 40  # Ограничение 1
    model1 += 4 * x11 + 3 * x12 + 2 * x13 + 1 * x14 + 0 * x15 >= 33  # Ограничение 2
    model1 += x11 <= 7
    model1 += x12 <= 1

    model1.solve()

    print(f"status: {model1.status}, {LpStatus[model1.status]}")
    print(f"objective: {model1.objective.value()}")

    for var in model1.variables():
        print(f"{var.name}: {var.value()}")
    for name, constraint in model1.constraints.items():
        print(f"{name}: {constraint.value()}")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    # objective: 9.0
    # x1: 7.0
    # x2: 1.0
    # x3: 1.0
    # x4: 0.0
    # x5: 0.0


def doLinearProgTwo():
    model2 = LpProblem(name="LP2", sense=LpMinimize)

    x21 = LpVariable(name="x21", lowBound=0)
    x22 = LpVariable(name="x22", lowBound=0)
    x23 = LpVariable(name="x23", lowBound=0)
    x24 = LpVariable(name="x24", lowBound=0)
    x25 = LpVariable(name="x25", lowBound=0)

    model2 += 1 * x21 + 1 * x22 + 1 * x23 + 1 * x24 + 1 * x25  # Целевая функция ЛП2
    model2 += 3 * x21 + 15 * x22 + 26 * x23 + 38 * x24 + 50 * x25 >= 40  # Ограничение 1
    model2 += 4 * x21 + 3 * x22 + 2 * x23 + 1 * x24 + 0 * x25 >= 33  # Ограничение 2
    model2 += x21 >= 7
    model2 += x22 <= 1

    model2.solve()

    print(f"status: {model2.status}, {LpStatus[model2.status]}")
    print(f"objective: {model2.objective.value()}")

    for var in model2.variables():
        print(f"{var.name}: {var.value()}")
    for name, constraint in model2.constraints.items():
        print(f"{name}: {constraint.value()}")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    # objective: 9.0
    # x1: 7.0
    # x2: 1.0
    # x3: 1.0
    # x4: 0.0
    # x5: 0.0


# Вызов решений ЛП
doLinearProgNull()
doLinearProgTwo()
doLinearProgOne()

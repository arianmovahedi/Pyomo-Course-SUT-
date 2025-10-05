# coding: utf-8
import pyomo.environ as pyo

model = pyo.ConcreteModel() 

model.x_1 = pyo.Var(within=pyo.NonNegativeReals)
model.x_2 = pyo.Var(within=pyo.NonNegativeReals)

model.obj = pyo.Objective(expr=model.x_1 + 2 * model.x_2)

model.con1 = pyo.Constraint(expr=3 * model.x_1 + 4 * model.x_2 >= 1)
model.con2 = pyo.Constraint(expr=2 * model.x_1 + 5 * model.x_2 >= 2)
# 1. Selecting a solver
opt = pyo.SolverFactory('glpk')

# 2. Solving the model
results = opt.solve(model)

"""
3. Checking the state of the answer
Using pyo.assert_optimal_termination() function will halt the script and outputs the message that the solver couldn't find the optimal solution
If we don't want to halt the progression and just assign it to a variable or use it in a conditional block we can use check_optimal_termination().
"""
pyo.assert_optimal_termination(results)

# Display the results
model.display()

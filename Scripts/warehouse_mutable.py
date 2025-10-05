# coding: utf-8
# warehouse_mutable.py: warehouse location problem with mutable parameters

# Importing dependencies
import pyomo.environ as pyo

# Model creation function
def create_warehouse_model(N, M, d, P):
    model = pyo.ConcreteModel(name= "(WL)")

    # Model variable creation
    model.x = pyo.Var(N, M, bounds=(0,1))
    model.y = pyo.Var(N, within=pyo.Binary)
    model.P = pyo.Param(initialize=P, mutable=True)

    # Objective function rule
    def obj_rule(model):
        return sum(d[n,m] * model.x[n,m] for n in N for m in M)
    model.obj = pyo.Objective(rule=obj_rule)

    # Defining Constraints
    def demand_rule(model, m):
        return sum(model.x[n,m] for n in N) == 1
    model.demand = pyo.Constraint(M, rule=demand_rule)

    def warehouse_active_rule(model, n, m):
        return model.x[n, m] <= model.y[n]
    model.warehouse_active = pyo.Constraint(N, M, rule=warehouse_active_rule)

    def num_warehouses_rule(model):
        return sum(model.y[n] for n in N) <= model.P
    model.num_warehouses = pyo.Constraint(rule=num_warehouses_rule)

    return model

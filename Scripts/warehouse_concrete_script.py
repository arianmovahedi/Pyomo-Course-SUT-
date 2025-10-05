# coding: utf-8
def create_warehouse_model(N, M, d, P):

    # Importing Dependencies
    import pyomo.environ as pyo
    
    # Model Creation
    model = pyo.ConcreteModel(name="(WL)")

    # Variable Definition
    model.x = pyo.Var(N, M, bounds=(0,1))
    model.y = pyo.Var(N, within=pyo.Binary)

    # Objective Function Definition
    def obj_rule(model):
        return sum(d[n, m] * model.x[n,m] for n in N for m in M)
    model.obj = pyo.Objective(rule=obj_rule)

    # Constraint 1
    def demand_rule(model, m):
        return sum(model.x[n,m] for n in N) == 1
    model.demand = pyo.Constraint(M, rule=demand_rule)

    # Constraint 2
    def warehouse_active_rule(model,n, m):
        return model.x[n,m] <= model.y[n]
    model.warehouse_active = pyo.Constraint(N, M, rule=warehouse_active_rule)

    # Constraint 3
    def num_warehouse_rule(model):
        return sum(model.y[n] for n in N) <= P
    model.num_warehouse = pyo.Constraint(rule=num_warehouse_rule)

    # Function Output
    return model 

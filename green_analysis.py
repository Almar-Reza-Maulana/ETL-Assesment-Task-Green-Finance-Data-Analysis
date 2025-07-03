# Create a module green_analysis.py with a function compute_co2_efficiency that takes CO2_Reduction and Investment_Cost as parameters.
# Use try-except to handle ZeroDivisionError (if Investment_Cost is 0), returning "Cannot compute" if an error occurs.
# Otherwise, compute and return the ratio: CO2_Reduction / (Investment_Cost* 1_000_000).

def compute_co2_efficiency(CO2_Reduction, Investment_Cost):
    try:
        efficiency = CO2_Reduction / (Investment_Cost * 1000000)
        return round(efficiency, 2)
    except ZeroDivisionError:
        return "Cannot compute"

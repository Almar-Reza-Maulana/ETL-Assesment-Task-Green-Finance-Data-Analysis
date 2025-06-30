# green_analysis.py

def compute_co2_efficiency(CO2_Reduction, Investment_Cost):
    try:
        efficiency = CO2_Reduction / (Investment_Cost * 1000000)
        return round(efficiency, 2)
    except ZeroDivisionError:
        return "Cannot compute"

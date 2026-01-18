# Wall dimensions
wall_width_cm = 200
wall_height_cm = 200
wall_area_cm2 = wall_width_cm * wall_height_cm

# Panel dimensions
panel_width_cm = 60
panel_height_cm = 40
panel_area_cm2 = panel_width_cm * panel_height_cm
unit_cost = 15000

# Calculation 1: Pure area math
exact_units_needed = wall_area_cm2 / panel_area_cm2

# Calculation 2: Practical layout (buying whole pieces to cover gaps)
# Columns and rows
import math
cols = math.ceil(wall_width_cm / panel_width_cm)
rows = math.ceil(wall_height_cm / panel_height_cm)
practical_units_needed = cols * rows

total_cost_min = math.ceil(exact_units_needed) * unit_cost
total_cost_practical = practical_units_needed * unit_cost

print(f"{wall_area_cm2=}")
print(f"{panel_area_cm2=}")
print(f"{exact_units_needed=}")
print(f"{practical_units_needed=}")
print(f"{total_cost_min=}")
print(f"{total_cost_practical=}")
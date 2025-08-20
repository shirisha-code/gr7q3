# 24f1002401@ds.study.iitm.ac.in
# Marimo interactive notebook for demonstrating variable relationships

import marimo as mo

# --- Cell 1: Data setup ---
# Define a base dataset (x values)
x_values = list(range(1, 21))
# Documenting flow: x_values will be used downstream in analysis.

# --- Cell 2: Interactive widget ---
# Create a slider for scaling y values
scale = mo.ui.slider(1, 10, value=2, label="Scale Factor")

# --- Cell 3: Dependent variable ---
# y depends on x_values and scale.value
y_values = [x * scale.value for x in x_values]
# Documenting flow: y_values updates automatically when slider moves.

# --- Cell 4: Dynamic Markdown Output ---
mo.md(f"""
### Interactive Relationship Demo

- Scale factor: **{scale.value}**
- First 5 y values: **{y_values[:5]}**

{"🔵" * scale.value}
""")

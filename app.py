import streamlit as st


# -----------------------------
# Thermodynamics Calculations
# -----------------------------

def work_done():
    st.subheader("Work Done During Expansion")

    pressure = st.number_input(
        "Pressure (Pa)",
        min_value=0.0
    )

    initial_volume = st.number_input(
        "Initial Volume (m³)",
        min_value=0.0
    )

    final_volume = st.number_input(
        "Final Volume (m³)",
        min_value=0.0
    )

    if st.button("Calculate Work"):
        work = pressure * (final_volume - initial_volume)

        st.success(f"Work Done = {work:.2f} J")


def heat_supplied():
    st.subheader("Heat Supplied")

    mass = st.number_input(
        "Mass (kg)",
        min_value=0.0
    )

    specific_heat = st.number_input(
        "Specific Heat Capacity (J/kg·K)",
        min_value=0.0
    )

    initial_temperature = st.number_input(
        "Initial Temperature (K)"
    )

    final_temperature = st.number_input(
        "Final Temperature (K)"
    )

    if st.button("Calculate Heat"):
        heat = mass * specific_heat * (
                final_temperature - initial_temperature
        )

        st.success(f"Heat Supplied = {heat:.2f} J")


def change_internal_energy():
    st.subheader("Change in Internal Energy")

    heat = st.number_input(
        "Heat Supplied Q (J)"
    )

    work = st.number_input(
        "Work Done W (J)"
    )

    if st.button("Calculate Internal Energy"):
        delta_u = heat - work

        st.success(
            f"Change in Internal Energy = {delta_u:.2f} J"
        )


def efficiency():
    st.subheader("Efficiency of Heat Engine")

    work = st.number_input(
        "Work Output (J)",
        min_value=0.0
    )

    heat_input = st.number_input(
        "Heat Supplied (J)",
        min_value=0.0
    )

    if st.button("Calculate Efficiency"):

        if heat_input == 0:
            st.error("Heat supplied cannot be zero.")

        else:
            efficiency_value = (work / heat_input) * 100

            st.success(
                f"Efficiency = {efficiency_value:.2f}%"
            )


# -----------------------------
# Main Application
# -----------------------------

st.title("🌡️ Thermodynamics Calculator")

st.write(
    "Select the required thermodynamics calculation."
)

option = st.selectbox(
    "Choose a calculation:",
    [
        "Work Done During Expansion",
        "Heat Supplied",
        "Change in Internal Energy",
        "Efficiency of Heat Engine"
    ]
)


# -----------------------------
# Menu Selection
# -----------------------------

if option == "Work Done During Expansion":
    work_done()

elif option == "Heat Supplied":
    heat_supplied()

elif option == "Change in Internal Energy":
    change_internal_energy()

elif option == "Efficiency of Heat Engine":
    efficiency()
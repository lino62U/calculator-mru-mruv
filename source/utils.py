def calculate_mru(option, value1, value2):
    try:
        value1 = float(value1)
        value2 = float(value2)

        if value2 == 0:
            return "Error: Time (value2) cannot be zero."

        if value1 < 0 or value2 < 0:
            return "Error: Negative values for time or distance are not physically valid."

        if option == "Distance":
            distance = value1 * value2
            return f"Distance: {distance} meters"
        elif option == "Velocity":
            velocity = value1 / value2
            return f"Velocity: {velocity} m/s"
        elif option == "Time":
            time = value1 / value2
            return f"Time: {time} seconds"
        else:
            return "Invalid option."

    except ValueError:
        return "Error: Please enter valid numerical values."

def calculate_mruv(option, vi, tiempo, aceleracion):
    try:
        vi = float(vi)
        tiempo = float(tiempo)
        aceleracion = float(aceleracion)

        if tiempo < 0:
            return "Error: Time cannot be negative."
        if aceleracion < 0:
            return "Error: Acceleration cannot be negative."
        if vi < 0:
            return "Error: Initial velocity cannot be negative."

        if option == "Distance (∆x)":
            # Calculate distance (displacement)
            distancia = vi * tiempo + (aceleracion * tiempo**2) / 2
            return f"Distance: {distancia} meters"

        elif option == "Final Velocity (Vf)":
            # Calculate final velocity
            vf = vi + aceleracion * tiempo
            return f"Final Velocity: {vf} m/s"

        elif option == "Time (∆t)":
            # Ensure acceleration is not zero to avoid division by zero
            if aceleracion == 0:
                return "Error: Acceleration must not be zero to calculate time."

            vf = vi + aceleracion * tiempo  # Assuming Vf is derived from this formula
            delta_time = (vf - vi) / aceleracion
            return f"Time: {delta_time} seconds"

        elif option == "Acceleration (α)":
            # Ensure time is not zero to avoid division by zero
            if tiempo == 0:
                return "Error: Time cannot be zero when calculating acceleration."
            
            alpha = (vi + aceleracion * tiempo - vi) / tiempo
            return f"Acceleration: {alpha} m/s²"

        elif option == "Initial Velocity (Vi)":
            # Calculate initial velocity from final velocity and acceleration
            vf = vi + aceleracion * tiempo  # Assuming you want to calculate Vf first
            vi = vf - aceleracion * tiempo
            return f"Initial Velocity: {vi} m/s"

        else:
            return "Invalid option."

    except ValueError:
        return "Error: Please enter valid numerical values."

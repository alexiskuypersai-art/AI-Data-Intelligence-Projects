"""
Goal: Implement a decision-making system for an autonomous exploration drone.
Key Concepts: Type Casting, Boolean Logic, Conditional Branching (if/elif/else).
Example: 
    Input: Battery=15, Signal=8, Obstacle=no -> Output: ALERT: Immediate return to base!
"""

def run_drone_diagnostic():
    print("--- 🛸 DRONE DIAGNOSTIC SYSTEM ---")

    # 1. Data Acquisition & Casting
    try:
        battery = float(input("Battery level (0-100): "))
        signal = int(input("Signal strength (0-10): "))
        has_obstacle = input("Obstacle detected? (yes/no): ").lower() == "yes"

        # 2. Decision Logic
        # Priority 1: Critical Safety Check
        if battery < 20 or signal < 3:
            print("ALERT: Immediate return to base!")

        # Priority 2: Environmental Obstruction
        elif battery >= 20 and signal >= 3 and has_obstacle:
            print("STATUS: Waiting (Obstacle detected).")

        # Priority 3: Optimal Performance Mode
        elif battery > 80 and signal > 8 and not has_obstacle:
            print("STATUS: High-performance exploration.")

        # Priority 4: Default Operation
        else:
            print("STATUS: Standard exploration.")
            
    except ValueError:
        print("ERROR: Invalid input. Please enter numeric values for battery and signal.")

if __name__ == "__main__":
    run_drone_diagnostic()

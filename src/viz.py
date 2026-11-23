import matplotlib.pyplot as plt

def hist_cholesterol(df):
    """Plottar ett histogram med fördelningen på kolesterolnivåer"""
    fig, ax = plt.subplots(figsize=(9,4))
    
    ax.hist(df["cholesterol"], bins=20)
    ax.set_title("Antal personer med respektive kolesterolhalt")
    ax.set_xlabel("Kolesterolhalt")
    ax.set_ylabel("Antal personer")
    ax.grid(True, axis="y", color="0.3")
    plt.show()
    
def box_length(df):
    """Plottar ett låddiagram över längd mellan kön"""
    fig, ax = plt.subplots(figsize=(8,4))

    ax.boxplot([df[df["sex"] == "M"]["height"],
                df[df["sex"] == "F"]["height"]], vert=False, widths=0.6)
    ax.set_yticklabels(["Män", "Kvinnor"])
    ax.set_title("Fördelning av längd mellan kön")
    ax.set_xlabel("Längd")
    plt.show()
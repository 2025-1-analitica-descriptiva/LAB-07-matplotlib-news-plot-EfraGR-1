"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv("files/input/news.csv", index_col=0)

    est_lines = {
        "Television": {"color": "dimgray", "ancho": 2, "z": 1},
        "Newspaper": {"color": "grey", "ancho": 2, "z": 1},
        "Internet": {"color": "tab:blue", "ancho": 3, "z": 2},
        "Radio": {"color": "lightgrey", "ancho": 2, "z": 1},
    }

    fig, axm = plt.subplots()

    for medio, props in est_lines.items():
        axm.plot(
            data[medio],
            label=medio,
            color=props["color"],
            linewidth=props["ancho"],
            zorder=props["z"],
        )

    axm.set_title("How people get their news", fontsize=16)
    axm.spines["top"].set_visible(False)
    axm.spines["left"].set_visible(False)
    axm.spines["right"].set_visible(False)
    axm.get_yaxis().set_visible(False)

    year_init, year_end = data.index[0], data.index[-1]

    for medio, props in est_lines.items():
        
        y_init = data.loc[year_init, medio]
        
        y_end = data.loc[year_end, medio]

        axm.scatter(year_init, y_init, color=props["color"], zorder=props["z"])
        
        axm.text(year_init - 0.2, y_init, f"{medio} {y_init}%", ha="right", va="center", color=props["color"])

        axm.scatter(year_end, y_end, color=props["color"], zorder=props["z"])
        
        axm.text(year_end + 0.2, y_end, f"{y_end}%", ha="left", va="center", color=props["color"])

    plt.tight_layout()

    
    os.makedirs("files/plots", exist_ok=True)
    
    plt.savefig("files/plots/news.png")
    plt.show()

pregunta_01()
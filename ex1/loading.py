try:
    import importlib
    import numpy
    import pandas
    import matplotlib.pyplot as plt
except ImportError:
    pass


def importation() -> dict[str, bool]:
    status = {}
    dictionnaire = {"pandas": "Data manipulation ready",
                    "numpy": "Numerical computation ready",
                    "requests": "Network access ready",
                    "matplotlib": "Visualization ready", }
    for x, z in dictionnaire.items():
        try:
            nom_mod = importlib.import_module(x)
            status[x] = True
            print(f"[OK] {x} ({nom_mod.__version__}) - {z}")
        except ImportError:
            print(f"[MISSING] {x}")
            status[x] = False
    return status


def gen_random() -> numpy.ndarray:
    donnes = numpy.random.rand(1000)
    return donnes


if __name__ == "__main__":
    print("=== Check des logiciels ===")
    status = importation()
    if not (status["numpy"] and status["pandas"] and status["matplotlib"]):
        print("Dependances manquantes..., veuillez installer pour continuer")
    else:
        print()
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        print("Generating visualization...")
        donnees = gen_random()
        df = pandas.DataFrame(donnees)
        print()
        print("=== Affiche des donnees ===")
        print(df)
        plt.plot(donnees, color="black", ls="--",
                 marker="o", markerfacecolor="pink")
        plt.grid(color="black")
        plt.savefig("matrix.png")
        print()
        print("Analysis complete!")
        print("Resultat saved to: matrix.png")

import numpy as np
import matplotlib.pyplot as plt

region_names = []
pie_contents = []
labels = []

region_names.append("SR_ee")
pie_contents.append([1.2494, 94.6162, 0.102598, 0.348517, 3.57871, 0.10454])
labels.append(["NonDefined", "PhotonConv", "DalitzDec", "ElMagProc", "BottomMeson", "CCbarMeson"])

region_names.append("SR_em")
pie_contents.append([1.65003, 89.8253, 0.403919, 0.386493, 0.592743, 6.82993, 0.31161])
labels.append(["NonDefined", "PhotonConv", "ElMagProc", "LightMeson", "CharmedMeson", "BottomMeson", "CCbarMeson"])

region_names.append("SR_mm")
pie_contents.append([23.536, 11.6183, 62.1779, 2.66785])
labels.append(["PhotonConv", "CharmedMeson", "BottomMeson", "BottomBaryon"])

for (region, content, label) in zip(region_names, pie_contents, labels):
    pie_dict = {}

    for (a,b) in zip(content, label):
        pie_dict[b] = a

    sorted_pie_dict = {k: v for k, v in sorted(pie_dict.items(), key=lambda item: item[1])}

    short_dict = {"Heavy Flavor": 0.0, "Other": 0.0}

    print(sorted_pie_dict)


    for k, v in zip(sorted_pie_dict.keys(), sorted_pie_dict.values()):
        if "Meson" in k or "Baryon" in k:
            short_dict["Heavy Flavor"] += v
            print(f"{k} in HF")
        elif "ElMagProc" in k or "Dalitz" in k or "Non" in k or "Tau" in k or "Pi" in k or "Kaon" in k or "Prompt" in k:
            short_dict["Other"] += v
            print(f"{k} in Other")
        else:
            short_dict[k] = v


    plt.title(f"Truth Origins for Non-Prompt Background, Region: {region}")
    plt.pie(short_dict.values(), labels=short_dict.keys(), autopct='%1.1f%%')
    plt.savefig(f"nonpromptorigin_{region}.png")
    plt.show()

import numpy as np
import matplotlib.pyplot as plt

region_names = []
pie_contents = []
labels = []

region_names.append("SR_ee")
pie_contents.append([1.2494, 94.6162, 0.102598, 0.348517, 3.57871, 0.10454])
labels.append(["Unknown", "UnknownMuon", "IsoMuon", "NonIsoMuon", "CharmedMesonPart", "BottomBaryonPart"])

region_names.append("SR_em")
pie_contents.append([1.65003, 89.8253, 0.403919, 0.386493, 0.592743, 6.82993, 0.31161])
labels.append(["Unknown", "UnknownMuon", "NonIsoMuon", "BBbarMesonPart", "CCbarMesonPart", "CharmedMesonPart", "BottomBaryonPart"])

region_names.append("SR_mm")
pie_contents.append([23.536, 11.6183, 62.1779, 2.66785])
labels.append(["UnknownMuon", "CCbarMesonPart", "CharmedMesonPart", "BJet"])

for (region, content, label) in zip(region_names, pie_contents, labels):
    pie_dict = {}

    thresh = 0.5

    for (a,b) in zip(content, label):
        if a > thresh:
            pie_dict[b] = a

    short_dict = {k: v for k, v in sorted(pie_dict.items(), key=lambda item: item[1])}

    plt.title(f"Truth Types for Non-Prompt Background, Region: {region}")
    plt.pie(short_dict.values(), labels=short_dict.keys(), autopct='%1.1f%%')
    plt.savefig(f"nonprompttype_{region}.png")
    plt.show()

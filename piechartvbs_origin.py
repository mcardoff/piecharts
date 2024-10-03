import numpy as np
import matplotlib.pyplot as plt

region_names = []
pie_contents = []
labels = []

filtering = True

# # ttbar - inclusive
# region_names.append("SR_ee (inclusive)")
# pie_contents.append([1.2494, 94.6162, 0.102598, 0.348517, 3.57871, 0.10454])
# labels.append(["NonDefined", "PhotonConv", "DalitzDec", "ElMagProc", "BottomMeson", "CCbarMeson"])

# region_names.append("SR_em (inclusive)")
# pie_contents.append([1.65003, 89.8253, 0.403919, 0.386493, 0.592743, 6.82993, 0.31161])
# labels.append(["NonDefined", "PhotonConv", "ElMagProc", "LightMeson", "CharmedMeson", "BottomMeson", "CCbarMeson"])

# region_names.append("SR_mm (inclusive)")
# pie_contents.append([23.536, 11.6183, 62.1779, 2.66785])
# labels.append(["PhotonConv", "CharmedMeson", "BottomMeson", "BottomBaryon"])

# # ttbar - nonallhad
# region_names.append("SR_ee (nonallhad)")
# pie_contents.append([1.40897, 91.4717, 0.672524, 6.44681])
# labels.append(["NonDefined", "PhotonConv", "ElMagProc", "BottomMeson"])

# region_names.append("SR_em (nonallhad)")
# pie_contents.append([2.2745, 84.741, 0.552893, 0.52645, 0.715245, 10.6421, 0.547884])
# labels.append(["NonDefined", "PhotonConv", "ElMagProc", "LightMeson", "CharmedMeson", "BottomMeson", "CCbarMeson"])

# region_names.append("SR_mm (nonallhad)")
# pie_contents.append([15.8294, 15.3516, 68.819])
# labels.append(["PhotonConv", "CharmedMeson", "BottomMeson"])

# # ttbar - dilep
# region_names.append("SR_ee (dilep)")
# pie_contents.append([1.07775, 97.9987, 0.212958, 0.493649, 0.216988])
# labels.append(["NonDefined", "PhotonConv", "DalitzDec", "BottomMeson", "CCbarMeson"])

# region_names.append("SR_em (dilep)")
# pie_contents.append([0.826447, 96.5307, 0.207445, 0.201912, 0.431182, 1.80232])
# labels.append(["NonDefined", "PhotonConv", "ElMagProc", "LightMeson", "CharmedMeson", "BottomMeson"])

# region_names.append("SR_mm (dilep)")
# pie_contents.append([47.5189, 41.5109, 10.9703])
# labels.append(["PhotonConv", "BottomMeson", "BottomBaryon"])

# charged higgs
# region_names.append("Electrons (Charged Higgs)")
# pie_contents.append([1.78982e-05, 0.00298484, 97.2497, 0.410656, 0.0769651, 0.00535025, 0.0420895, 1.66519, 0.21954, 0.327544])
# labels.append(["Unknown", "KnownUnknown", "IsoElectron", "ChargeFlipIsoElectron", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay"])

# region_names.append("Muons (Charged Higgs)")
# pie_contents.append([1.09792, 8.94487, 5.69732, 2.34909, 50.8905, 18.0308, 12.8541, 0.104786, 0.00475399, 0.025889])
# labels.append(["Unknown", "KnownUnknown", "PromptMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike", "TauDecayLike", "BHadronDecayLike"])

#iff from charged higgs
region_names.append("iff el no filtering")
pie_contents.append([1.78982e-05, 0.00298484, 97.2497, 0.410656, 0.0769651, 0.00535025, 0.0420895, 1.66519, 0.21954, 0.327544])
labels.append(["Unknown", "KnownUnknown", "IsoElectron", "ChargeFlipIsoElectron", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay"])

region_names.append("iff mu no filtering")
pie_contents.append([1.09792, 8.94487, 5.69732, 2.34909, 50.8905, 18.0308, 12.8541, 0.104786, 0.00475399, 0.025889])
labels.append(["Unknown", "KnownUnknown", "PromptMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike", "TauDecayLike", "BHadronDecayLike"])

# region_names.append("iff el no prompt el")
# pie_contents.append([0.000650763, 0.108526, 14.9311, 2.79839, 0.194531, 1.53034, 60.545, 7.98228, 11.9092])
# labels.append(["Unknown", "KnownUnknown", "ChargeFlipIsoElectron", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay"])

# region_names.append("iff mu no prompt el")
# pie_contents.append([1.09792, 8.94487, 5.69732, 2.34909, 50.8905, 18.0308, 12.8541, 0.104786, 0.00475399, 0.025889])
# labels.append(["Unknown", "KnownUnknown", "PromptMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike", "TauDecayLike", "BHadronDecayLike"])

# region_names.append("iff el no prompt mu")
# pie_contents.append([1.78982e-05, 0.00298484, 97.2497, 0.410656, 0.0769651, 0.00535025, 0.0420895, 1.66519, 0.21954, 0.327544])
# labels.append(["Unknown", "KnownUnknown", "IsoElectron", "ChargeFlipIsoElectron", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay"])

# region_names.append("iff mu no prompt mu")
# pie_contents.append([1.16426, 9.48527, 2.49101, 53.9651, 19.1201, 13.6306, 0.111116, 0.00504121, 0.027453])
# labels.append(["Unknown", "KnownUnknown", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike", "TauDecayLike", "BHadronDecayLike"])

region_names.append("iff el no prompt lep")
pie_contents.append([0.000650763, 0.108526, 14.9311, 2.79839, 0.194531, 1.53034, 60.545, 7.98228, 11.9092])
labels.append(["Unknown", "KnownUnknown", "ChargeFlipIsoElectron", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay"])

region_names.append("iff mu no prompt lep")
pie_contents.append([1.16426, 9.48527, 2.49101, 53.9651, 19.1201, 13.6306, 0.111116, 0.00504121, 0.027453])
labels.append(["Unknown", "KnownUnknown", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike", "TauDecayLike", "BHadronDecayLike"])

# region_names.append("iff lep no prompt el")
# pie_contents.append([0.354499, 2.95807, 10.1161, 1.83727, 1.89596, 0.131798, 1.79437, 57.4316, 11.2227, 12.2139, 0.0337912, 0.00153307, 0.00834867])
# labels.append(["Unknown", "KnownUnknown", "ChargeFlipIsoElectron", "PromptMuon", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike", "TauDecayLike", "BHadronDecayLike"])

# region_names.append("iff lep no prompt mu")
# pie_contents.append([0.0142151, 0.118616, 96.0638, 0.405648, 0.0760266, 0.00528501, 0.0719528, 2.30296, 0.450022, 0.489768, 0.001355, 6.14747e-05, 0.000334775])
# labels.append(["Unknown", "KnownUnknown", "IsoElectron", "ChargeFlipIsoElectron", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike", "TauDecayLike", "BHadronDecayLike"])

region_names.append("iff lep no prompt lep")
pie_contents.append([0.361134, 3.01343, 10.3055, 1.93145, 0.134265, 1.82796, 58.5065, 11.4328, 12.4425, 0.0344237, 0.00156176, 0.00850493])
labels.append(["Unknown", "KnownUnknown", "ChargeFlipIsoElectron", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike", "TauDecayLike", "BHadronDecayLike"])

for (region, content, label) in zip(region_names, pie_contents, labels):
    pie_dict = {}
    for (a,b) in zip(content, label):
        pie_dict[b] = a
        
    short_dict = {"Heavy Flavor": 0.0, "Other": 0.0, "Prompt": 0.0, "Misc Lep": 0.0}
    # print(region)
    if filtering:
        for k, v in zip(pie_dict.keys(), pie_dict.values()):
            if ("Meson" in k or "Baryon" in k or "Hadron" in k):
                short_dict["Heavy Flavor"] += v
                # print(f"{k} in HF")
            elif "Unknown" in k or "Light" in k:
                short_dict["Other"] += v
                # print(f"{k} in Other")
            elif "Iso" in k or "PromptMuon" in k:
                short_dict["Prompt"] += v
                # print(f"{k} in Prompt")
            elif "NonMuonLike" in k or "TauDecay" in k or "ElectronFromMuon" in k:
                short_dict["Misc Lep"] += v
                # print(f"{k} in Misc Lep")
            # elif v < 1.0:
            #     short_dict["Other"] += v
            else:
                short_dict[k] = v
                # print(f"{k} added manually")
    else:
        short_dict = pie_dict

    sorted_pie_dict = {k: v for k, v in sorted(short_dict.items(), key=lambda item: item[1])}

    for item in list(sorted_pie_dict):
        if abs(sorted_pie_dict[item]) < 1.0e-6:
            del sorted_pie_dict[item]

    fname = f"nonpromptorigin_{region.replace(' ', '_')}.png"
    plt.title(f"Truth Origins for Non-Prompt Background, Region: {region}")
    plt.pie(sorted_pie_dict.values(), labels=sorted_pie_dict.keys(), autopct='%1.1f%%')
    plt.savefig(fname)
    plt.show()

import numpy as np
import matplotlib.pyplot as plt

def insertadd(dic, key, value):
    if key in dic:
        dic[key] += value
    else:
        dic[key] = value

region_names = []
pie_contents = []
labels = []

filtering = True

region_names.append("iff_no_prompt_SR")
pie_contents.append([1.12923, 13.7769, 5.26232, 1.66851, 0.209691, 8.85962, 3.5118, 65.4325, 0.149471])
labels.append(["Unknown", "KnownUnknown", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike"])

region_names.append("iff_no_prompt_SR_ee")
pie_contents.append([7.16844, 8.39073, 0.359042, 0.69646, 8.54271, 3.02908, 71.5215, 0.292058])
labels.append(["KnownUnknown", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike"])

region_names.append("iff_no_prompt_SR_mm")
pie_contents.append([3.68453, 13.9757, 3.69038, 11.0984, 6.14576, 61.4053])
labels.append(["Unknown", "KnownUnknown", "ElectronFromMuon", "BHadronDecay", "CHadronDecay", "LightFlavorDecay"])

region_names.append("iff_no_prompt_SR_em")
pie_contents.append([0.818013, 14.668, 4.42015, 1.31685, 0.213289, 8.80695, 4.4103, 65.3464])
labels.append(["Unknown", "KnownUnknown", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay"])

region_names.append("iff_no_prompt_CR_bb_mumuTL")
pie_contents.append([1.88462, 18.289, 0.0786416, 3.2054, 0.588259, 13.2994, 5.49233, 57.1624])
labels.append(["Unknown", "KnownUnknown", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay"])

region_names.append("iff_no_prompt_CR_bb_muelTL")
pie_contents.append([0.0716875, 13.5269, 3.15619, 1.55974, 0.0377519, 9.12817, 3.81829, 68.6593, 0.0418949])
labels.append(["Unknown", "KnownUnknown", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike"])

region_names.append("iff_no_prompt_CR_1b_mumuTL")
pie_contents.append([0.34733, 16.9011, 0.0978526, 3.23862, 0.312876, 14.3933, 3.4057, 61.2765, 0.0266813])
labels.append(["Unknown", "KnownUnknown", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike"])

region_names.append("iff_no_prompt_CR_1b_muelTL")
pie_contents.append([0.205661, 15.203, 1.82104, 1.18163, 0.211068, 11.9045, 3.22937, 66.1306, 0.113014])
labels.append(["Unknown", "KnownUnknown", "PromptPhotonConversion", "ElectronFromMuon", "TauDecay", "BHadronDecay", "CHadronDecay", "LightFlavorDecay", "NonMuonlike"])

for (region, content, label) in zip(region_names, pie_contents, labels):
    pie_dict = {}
    for (a,b) in zip(content, label):
        pie_dict[b] = a
        
    short_dict = {}
    # print(region)
    if filtering:
        for k, v in zip(pie_dict.keys(), pie_dict.values()):
            if ("Meson" in k or "Baryon" in k or "Hadron" in k):
                insertadd(short_dict,"Heavy Flavor", v)
                print(f"{k} in HF")
            elif "Unknown" in k:
                insertadd(short_dict, "Other", v)
                print(f"{k} in Other")
            elif "Iso" in k or "PromptMuon" in k:
                insertadd(short_dict, "Prompt", v)
                print(f"{k} in Prompt")
            elif "NonMuonLike" in k or "TauDecay" in k or "ElectronFromMuon" in k:
                insertadd(short_dict, "Misc Lep", v)
                print(f"{k} in Misc Lep")
            elif v < 0.09:
                insertadd(short_dict, "Other", v)
            else:
                short_dict[k] = v
                print(f"{k} added manually")
    else:
        short_dict = pie_dict

    sorted_pie_dict = {k: v for k, v in sorted(short_dict.items(), key=lambda item: item[1])}

    for item in list(sorted_pie_dict):
        if abs(sorted_pie_dict[item]) < 1.0e-6:
            del sorted_pie_dict[item]

    fname = f"v6ntuples_correctcuts/nonpromptorigin_{region.replace(' ', '_')}.png"
    plt.title(f"NP Truth Origins, Region: {region}")
    plt.pie(sorted_pie_dict.values(), labels=sorted_pie_dict.keys(), autopct='%1.1f%%')
    plt.savefig(fname)
    plt.show()

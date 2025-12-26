# Disease Pathway Explorer using KEGG

import requests

print("🧬 Disease Pathway Explorer (KEGG)")
print("----------------------------------")

# Takes disease name from user
disease_name = input("Enter disease name: ").strip()

#Search disease in KEGG
search_url = f"https://rest.kegg.jp/find/disease/{disease_name}"
search_response = requests.get(search_url)
search_text = search_response.text

# Check if disease exists
if search_text.strip() == "":
    print("❌ Disease not found in KEGG database")
    exit()

# Extract first disease ID
first_line = search_text.split("\n")[0]
disease_id = first_line.split("\t")[0]

print("\n✅ Disease ID found:", disease_id)

# Get pathways linked to disease
pathway_url = f"https://rest.kegg.jp/link/pathway/{disease_id}"
pathway_response = requests.get(pathway_url)
pathway_text = pathway_response.text

if pathway_text.strip() == "":
    print("❌ No pathways associated with this disease")
    exit()

print("\n🧠 Associated Pathways:\n")

pathway_ids = []

for line in pathway_text.split("\n"):
    if line:
        pathway_id = line.split("\t")[1]
        pathway_ids.append(pathway_id)

#Fetch pathway names
for pid in pathway_ids:
    pathway_info_url = f"https://rest.kegg.jp/get/{pid}"
    pathway_info = requests.get(pathway_info_url).text

    for line in pathway_info.split("\n"):
        if line.startswith("NAME"):
            pathway_name = line.replace("NAME", "").strip()
            print(f"{pid} → {pathway_name}")
            break

#Save results to file
with open("disease_pathways.txt", "w") as file:
    file.write(f"Disease: {disease_name}\n")
    file.write(f"Disease ID: {disease_id}\n\n")
    file.write("Associated Pathways:\n")

    for pid in pathway_ids:
        file.write(pid + "\n")

print("\nResults saved to disease_pathways.txt")
print("Project completed successfully!")

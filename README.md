# Fetch_Disease_pathway
The Disease Pathway Explorer is a beginner-friendly bioinformatics project built using Python.

It allows users to input a disease name and automatically retrieves the associated biological pathways using the KEGG (Kyoto Encyclopedia of Genes and Genomes) REST API.

This project helps understand how diseases are linked to molecular pathways and introduces real-world database interaction in bioinformatics.

**🎯 Objectives**

Accept a disease name as user input

Search the disease in the KEGG database

Retrieve the KEGG Disease ID

Fetch pathways associated with the disease

Display pathway IDs and names

Save results to a text file

**Technologies Used**

Python

KEGG REST API

Requests library

📂 Project Structure
Disease-Pathway-Explorer/

│

├── disease_pathway_explorer.py

├── disease_pathways.txt

└── README.md

**🚀 How to Run the Project**

**1️⃣ **Install required library****

pip install requests

**2️⃣ **Run the Python script****

python disease_pathway_explorer.py

**3️⃣ **Enter disease name when prompted****

Example:

Enter disease name: breast cancer

**🧪 Sample Output**
Disease ID found: ds:H00015

Associated Pathways:

path:hsa05224 → Breast cancer

path:hsa05200 → Pathways in cancer

path:hsa05223 → Non-small cell lung cancer


A file named disease_pathways.txt will be created with the results.

📁 Output File

disease_pathways.txt contains:

Disease name

Disease ID

List of associated pathway IDs

**💡 Why This Project is Important**

Introduces real biological databases

Demonstrates API-based data retrieval

Builds foundation for disease–gene–pathway analysis

🌱 Future Improvements

Extract genes involved in each pathway

Visualize disease–pathway relationships

Compare pathways between two diseases

Add error handling and menu options

**🙌 Author**

**Namrata Vishwakarma**

**B.Tech Bioengineering**

**VIT Bhopal University****

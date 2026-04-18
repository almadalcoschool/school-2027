import os
import glob
import shutil

attendees_dir = r"c:\Users\mathieu\almaweb\_attendees"

# 1. Delete old files
old_files = glob.glob(os.path.join(attendees_dir, "*.md"))
for f in old_files:
    if os.path.basename(f) != "_defaults.md":
        os.remove(f)

# 2. Define new speakers
speakers = [
    {
        "name": "Orit Peleg",
        "position": "UC Boulder",
        "website": "https://www.colorado.edu/cs/orit-peleg",
        "category": "Organismal Pattern Formation (from Animals to Microbes)"
    },
    {
        "name": "David Johnson",
        "position": "Eawag",
        "website": "http://www.mca-johnson.com",
        "category": "Organismal Pattern Formation (from Animals to Microbes)"
    },
    {
        "name": "Sara Mitri",
        "position": "University of Lausanne",
        "website": "https://www.unil.ch/mitrilab/home.html",
        "category": "Organismal Pattern Formation (from Animals to Microbes)"
    },
    {
        "name": "Sam Reiter",
        "position": "OIST",
        "website": "https://groups.oist.jp/cnu",
        "category": "Morphogenesis and Developmental Patterning"
    },
    {
        "name": "Nicoletta Petridou",
        "position": "EMBL Heidelberg",
        "website": "https://www.embl.org/groups/petridou/",
        "category": "Morphogenesis and Developmental Patterning"
    },
    {
        "name": "Anna Erzberger",
        "position": "EMBL Heidelberg",
        "website": "https://www.embl.org/groups/erzberger/",
        "category": "Morphogenesis and Developmental Patterning"
    },
    {
        "name": "Thomas Lecuit",
        "position": "Collège de France",
        "website": "https://www.college-de-france.fr/en/chair/thomas-lecuit",
        "category": "Morphogenesis and Developmental Patterning"
    },
    {
        "name": "Luis Morelli",
        "position": "IBioBA MPS Argentina",
        "website": "https://ibioba-mpsp-conicet.gov.ar/luis-morelli/",
        "category": "Temporal Patterns"
    },
    {
        "name": "Mathias Spliid Heltberg",
        "position": "University of Copenhagen",
        "website": "https://nbi.ku.dk/english/staff/?id=581023&vis=medarbejder",
        "category": "Temporal Patterns"
    },
    {
        "name": "Aneta Koseska",
        "position": "MPI Neurobiology",
        "website": "https://www.caesar.de/en/our-research/cellular-computations-and-learning/",
        "category": "Temporal Patterns"
    },
    {
        "name": "Silvia De Monte",
        "position": "ENS",
        "website": "https://www.ibens.ens.psl.eu/?rubrique35",
        "category": "Across Scales and Outside Perspectives on Pattern Formation"
    },
    {
        "name": "Toby Kiers",
        "position": "Vrije Universiteit Amsterdam",
        "website": "https://spun.earth/",
        "category": "Across Scales and Outside Perspectives on Pattern Formation"
    }
]

# 3. Write files
for speaker in speakers:
    surname = speaker['name'].split()[-1]
    filename = f"{surname}.md"
    filepath = os.path.join(attendees_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"name: {speaker['name']}\n")
        f.write(f"position: {speaker['position']}\n")
        f.write(f"image_path: /images/attendees/{surname}.jpg\n")
        f.write(f"website: \"{speaker['website']}\"\n")
        f.write(f"category: \"{speaker['category']}\"\n")
        f.write("---\n")

print("Created new speaker files successfully.")

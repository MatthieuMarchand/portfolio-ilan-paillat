import os
import shutil

def add_project_div(project_title, project_tags, paragraphs):
    file_path = "../index.html"
    pdf = None
    img = None

    # Chercher les fichiers PDF et images dans le dossier courant
    for file in os.listdir('.'):
        if file.endswith('.pdf'):
            pdf = file
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
            img = file

    # Déplacer les fichiers trouvés vers les dossiers de destination
    if pdf is None or img is None:
        print("Fichiers PDF et/ou images non trouvés.")
        return False
    
    shutil.move(pdf, f"../documents/{pdf}")
    shutil.move(img, f"../pictures/{img}")

    # Générer le contenu des paragraphes
    paragraphs_html = ""
    for paragraph in paragraphs:
        paragraphs_html += f"""
        <p>
          {paragraph}
        </p>
        """

    # La nouvelle div à ajouter
    new_div = f"""
        <div class="project">
            <h2>{project_title}</h2>
            <h3>{project_tags}</h3>
            <div class="content">
                <img src="/pictures/{img}" alt="" />
                <div class="paragraphes">
                    {paragraphs_html}
                    <div class="buttons">
                        <a href="/documents/{pdf}" class="cta" target="_blank">générer le pdf</a>
                        <!--<a href="#" class="cta">voir le repository</a>-->
                    </div>
                </div>
            </div>
        </div>
    """

    # Lire le contenu du fichier HTML
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    # Chercher la ligne avec <section id="projects">
    for i, line in enumerate(content):
        if '<section id="projects">' in line:
            # Insérer la nouvelle div juste après cette ligne
            content.insert(i + 1, new_div)
            break

    # Écrire le nouveau contenu dans le fichier HTML
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(content)

def question():
    project_title = input("Titre du projet : ")
    project_tags = input("Tags du projet : ")
    project_tags = "#" + project_tags.replace(" ", " #")
    paragraphs = []
    while True:
        paragraph = input("Paragraphe (laisser vide pour terminer) : ")
        if paragraph == "":
            break
        paragraphs.append(paragraph)
    add_project_div(project_title, project_tags, paragraphs)
    commit = input("Voulez-vous commit les changements ? (y/n) : ")
    if commit.lower() == "y":
        os.system("git add .")
        os.system(f"git commit -m 'Add project div {project_title}'")
        os.system("git push")

question()

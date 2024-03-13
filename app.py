from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'une_cle_secrete'
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('file')  # Obtenir une liste de fichiers
        all_valid_emails = []  # Liste pour cumuler les emails valides de tous les fichiers
        for file in files:
            if file:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                valid_emails = extract_emails(filepath)
                if valid_emails:
                    all_valid_emails.extend(valid_emails)  # Ajoute les emails valides de ce fichier à la liste cumulée
        if all_valid_emails:
            emails_str = ";".join(all_valid_emails)
            flash(f"{len(all_valid_emails)} adresses email extraites avec succès.")
            return render_template('emails.html', emails=emails_str)
        else:
            flash("Aucun e-mail valide trouvé.")
    return render_template('upload.html')

def extract_emails(filepath):
    try:
        df = pd.read_csv(filepath, sep=';', skiprows=1)
        valid_emails = df['email'].dropna().apply(lambda x: x if "@" in x else None).dropna().tolist()
        return valid_emails
    except Exception as e:
        flash(f"Une erreur est survenue lors de l'extraction des e-mails : {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)

class Contact:
    
    def __init__(self, nom, prenom, telephone, email):
        #vérification sample
        if not nom:
            raise ValueError("Le nom est obligatoire")
        if not prenom:
            raise ValueError("Le prenom est obligatoire")
        if not telephone:
            raise ValueError("Le telephone est obligatoire")
        if not email:
            raise ValueError("L'email est obligatoire")
        self.nom = nom
        self.prenom = prenom 
        self._telephone = telephone
        self.email = email

    # --- Sérialisation (Objet -> Dict) ---
    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "telephone": self._telephone,
            "email": self.email
        }

    # --- Désérialisation (Dict -> Objet) ---
    @classmethod
    def from_dict(cls, data):
        # On extrait les données du dictionnaire pour recréer un nouveau Contact
        return cls(data["nom"], data["prenom"], data["telephone"], data["email"])

    ################# Méthodes #################
    def afficher_fiche(self):
        print(f"Contact : {self.nom} {self.prenom} - {self._telephone} - {self.email}")

    def set_telephone(self, nouveau_numero):
        self._telephone = nouveau_numero
        print("Numéro de téléphone mis à jour pour " + self.nom + ".")
    
    def get_telephone(self):
        return self._telephone

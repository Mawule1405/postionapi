from ..repositories.pole_repository import PoleRepository  # Assurez-vous d'importer le repository

class PoleService:
    def __init__(self):
        # Initialisation du repository
        self.pole_repository = PoleRepository()

    def get_nearest_pole(self, longitude: float, latitude: float) -> dict:
        try:
            # Appel à la méthode du repository pour récupérer le poteau et le quartier
            result, quartier = self.pole_repository.get_nearest_pole(longitude, latitude)

            # Si aucun résultat n'est trouvé
            if not result:
                return None

            # Récupération des données du poteau
            fid = result[0]
            longitude = result[1]
            latitude = result[2]
            distance = result[3]
            ville = result[4]
            exploit = result[5]

            # Récupération des données du quartier
            quartier_name = quartier[1] if quartier else None

            return {
                "fid": fid,
                "coordinates": {"longitude": longitude, "latitude": latitude},
                "distance": round(distance, 5),
                "ville": ville,
                "exploit": exploit,
                "quartier": quartier_name
            }

        except Exception as e:
            # Gestion des erreurs
            print(f"Erreur lors de l'exécution du service : {e}")
            return None

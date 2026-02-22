## Exercice : La Persistance avec les Volumes Docker

### Étape 1 : Lancement initial

Démarrez la base de données :

```bash
docker-compose up -d

```

*Le fichier `init.sql` crée la table et insère Alice et Bob automatiquement.*

### Étape 2 : Lecture et Ajout

Vérifiez les données initiales puis ajoutez-en de nouvelles :

```bash
python read_db.py
python populate_more_db.py
python read_db.py

```

*Vous devriez maintenant voir Alice, Bob, Charlie et David.*

### Étape 3 : Le test de destruction

Stopper le conteneur :

```bash
docker-compose down

```

*Ici, le conteneur n'existe plus. Dans un monde sans volumes, les données seraient perdues.*

### Étape 4 : Preuve de persistance

Relancez le service :

```bash
docker-compose up -d

```

Relancez la lecture :

```bash
python read_db.py

```

**Observation :** Charlie et David sont toujours là ! Bien que le conteneur soit tout neuf, il s'est reconnecté au volume `db_data` qui contient l'état précédent de la base.

### Étape 5 : Nettoyage total

Si vous voulez vraiment tout supprimer (y compris les données) :

```bash
docker-compose down -v

```
### Guide du Test de Non-Persistance

#### Modification du fichier `docker-compose.yml`

Modifiez la section `volumes` pour désactiver le stockage persistant :

```yaml
    volumes:
      # - db_data:/var/lib/postgresql/data  <-- Ligne commentée : plus de persistance
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

```

Répétez les étapes 1 à 5 de la section précédente.
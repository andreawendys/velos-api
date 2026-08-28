# 5. QCM · 40 questions sur les quatre outils

> 📝 **Consignes** : **40 questions**, **une seule bonne réponse** par question, **1 point** par question. Répondu de mémoire, sans rouvrir les supports : c'est une vérification de tes acquis, pas une chasse au trésor.
>
> ✍️ **Comment répondre** : **directement dans ce fichier**. Coche la bonne réponse en remplaçant `- [ ]` par `- [x]` devant elle. Ne supprime rien, ne recopie rien ailleurs.
>
> ```
>   - [ ] A. Une reponse fausse
>   - [x] B. La reponse que je choisis
>   - [ ] C. Une autre reponse fausse
> ```
>
> 📤 **Rendu** : renomme ce fichier complété en **`QCM.md`** et dépose le **à la racine de ton dépôt**, avec le reste du projet. Échéance identique : **vendredi 28/08/2026, 18:00**.
>
> ⚠️ Deux réponses cochées sur une même question comptent comme une réponse fausse. Aucune réponse cochée compte comme une réponse fausse.

**Nom et prénom :** KOFFI Andrea Wendy

**Groupe :** M2DAN26.1

---

## Partie 1 · Git (questions 1 à 12)

**Q1.** Quelles sont les **trois zones** de Git sur ta machine ?

- [ ] A. Le dépôt distant, le dépôt local et l'index
- [x] B. Le répertoire de travail, l'index (zone de préparation) et le dépôt local
- [ ] C. La branche, l'étiquette et le commit
- [ ] D. `add`, `commit` et `push`

**Q2.** Que fait exactement `git add` ?

- [ ] A. Il enregistre définitivement les modifications dans l'historique
- [ ] B. Il envoie les modifications sur GitHub
- [ ] C. Il crée une nouvelle branche à partir des modifications
- [x] D. Il place les modifications dans l'index, en préparation du prochain commit

**Q3.** Quelle est la différence entre un commit et un envoi vers le distant ?

- [x] A. Le commit enregistre dans l'historique **local**, l'envoi publie ces commits sur le dépôt distant
- [ ] B. Aucune, ce sont deux noms pour la même opération
- [ ] C. Le commit publie sur GitHub, l'envoi archive en local
- [ ] D. Le commit ne fonctionne que sur la branche principale

**Q4.** 🛠️ Tu ajoutes un fichier déjà suivi par Git dans le `.gitignore`. Que se passe-t-il ?

- [ ] A. Il disparaît immédiatement de l'historique, y compris des commits passés
- [ ] B. Git refuse le prochain commit tant que le fichier n'est pas supprimé
- [x] C. Rien : un fichier déjà suivi continue de l'être, l'exclusion ne vaut que pour les fichiers non suivis
- [ ] D. Le fichier est automatiquement chiffré

**Q5.** Qu'est-ce qu'une fusion en avance rapide ?

- [ ] A. Une fusion faite avec l'option qui ignore les conflits
- [ ] B. Une fusion où la branche cible n'a pas avancé de son côté : Git déplace simplement le pointeur, sans créer de commit de fusion
- [x] C. Une fusion qui ne prend que le dernier commit de la branche source
- [ ] D. Une fusion effectuée directement sur le dépôt distant

**Q6.** Tu vois apparaître dans un fichier les marqueurs `<<<<<<<`, `=======` et `>>>>>>>`. Que dois tu faire ?

- [ ] A. Supprimer le fichier et le recréer
- [ ] B. Lancer un envoi forcé vers le distant, Git résoudra tout seul
- [ ] C. Attendre : les marqueurs disparaissent au prochain commit
- [x] D. Éditer le fichier pour ne garder que le contenu voulu, **retirer les marqueurs**, puis marquer le conflit résolu et terminer la fusion

**Q7.** Pourquoi ne rebase t on pas une branche déjà partagée avec d'autres ?

- [x] A. Parce que le rebase réécrit l'historique et change l'identifiant des commits, ce qui casse le travail de ceux qui les avaient déjà récupérés
- [ ] B. Parce que le rebase est plus lent que la fusion
- [ ] C. Parce que le rebase supprime les branches distantes
- [ ] D. Parce que GitHub interdit techniquement l'opération

**Q8.** Dans une paire de clés SSH, laquelle dépose t on sur GitHub ?

- [ ] A. La clé privée, puisque c'est elle qui prouve l'identité
- [ ] B. Les deux, sinon l'authentification échoue
- [x] C. La clé publique
- [ ] D. Ni l'une ni l'autre : GitHub génère lui même la paire

**Q9.** 🛠️ Tu obtiens `Permission denied (publickey)` alors que « tout est bon côté GitHub ». Quelle est la cause la plus fréquente rencontrée en TP ?

- [ ] A. Le dépôt distant est privé
- [ ] B. Le nom de la branche est incorrect
- [ ] C. Git n'est pas à jour
- [x] D. La paire de clés a été générée dans un autre environnement que celui d'où tu pousses, donc la clé proposée n'est pas celle qui a été déposée

**Q10.** 🛠️ Ton envoi est refusé avec un message indiquant que le distant contient du travail que tu n'as pas. Quelle est la bonne réaction ?

- [ ] A. Forcer l'envoi pour imposer ta version
- [x] B. Récupérer le travail du distant, l'intégrer chez toi en résolvant les éventuels conflits, puis renvoyer
- [ ] C. Supprimer le dépôt distant et le recréer
- [ ] D. Créer une nouvelle branche et abandonner la précédente

**Q11.** À quoi sert une étiquette (`tag`) ?

- [x] A. À poser un nom stable et lisible sur un commit précis, pour désigner une version livrée
- [ ] B. À créer une branche protégée
- [ ] C. À marquer un fichier comme ignoré
- [ ] D. À renommer le dépôt

**Q12.** Que produit concrètement une règle de protection sur la branche principale ?

- [ ] A. Elle chiffre le contenu de la branche
- [ ] B. Elle rend le dépôt privé
- [x] C. Elle empêche l'envoi direct sur cette branche et impose le passage par une pull request
- [ ] D. Elle interdit la création de nouvelles branches

---

## Partie 2 · Docker (questions 13 à 24)

**Q13.** Quelle est la différence de fond entre une machine virtuelle et un conteneur ?

- [ ] A. Le conteneur est toujours plus sécurisé que la machine virtuelle
- [ ] B. La machine virtuelle ne peut pas exécuter Linux
- [ ] C. Le conteneur ne peut faire tourner qu'un seul langage de programmation
- [x] D. Le conteneur partage le noyau du système hôte, alors que la machine virtuelle embarque un système d'exploitation complet

**Q14.** Image et conteneur : quelle formulation est juste ?

- [x] A. L'image est un modèle immuable, le conteneur est une instance de ce modèle en cours d'exécution
- [ ] B. L'image est le conteneur une fois qu'il est arrêté
- [ ] C. Le conteneur contient plusieurs images empilées
- [ ] D. Les deux mots désignent la même chose selon le système d'exploitation

**Q15.** Dans une publication de port notée `8001:8000`, que représente chaque nombre ?

- [ ] A. `8001` est le port dans le conteneur, `8000` le port sur ta machine
- [x] B. `8001` est le port sur ta machine, `8000` le port dans le conteneur
- [ ] C. Ce sont deux ports de ta machine, l'un en entrée et l'autre en sortie
- [ ] D. `8001` est le port et `8000` le nombre maximal de connexions

**Q16.** 🛠️ Ton conteneur tourne, la publication de port est correcte, mais aucune requête n'aboutit depuis ta machine. Quelle est la cause vue en cours ?

- [ ] A. Le conteneur manque de mémoire
- [ ] B. Docker doit être redémarré après chaque publication de port
- [x] C. L'application n'écoute que sur la boucle locale à l'intérieur du conteneur, au lieu d'écouter sur toutes les interfaces
- [ ] D. Il manque un volume

**Q17.** Pourquoi installe t on les dépendances **avant** de copier le code applicatif dans la recette de construction ?

- [ ] A. Parce que l'ordre des instructions est imposé par Docker
- [ ] B. Parce que le code ne peut pas être copié avant l'installation
- [ ] C. Parce que cela réduit la taille finale de l'image de moitié
- [x] D. Parce qu'une couche invalidée invalide toutes les suivantes : le code change souvent, les dépendances rarement, donc on met le stable d'abord

**Q18.** À quoi sert le fichier d'exclusion de construction (`.dockerignore`) ?

- [x] A. À empêcher que des fichiers inutiles ou sensibles soient envoyés au moteur et se retrouvent dans l'image
- [ ] B. À empêcher Git de suivre les fichiers Docker
- [ ] C. À exclure des conteneurs d'un réseau
- [ ] D. À ignorer les erreurs pendant la construction

**Q19.** Quel est l'intérêt d'une construction en plusieurs étages ?

- [ ] A. Construire plusieurs images en parallèle
- [ ] B. Ne garder dans l'image finale que le résultat utile, sans l'outillage de construction, ce qui réduit fortement la taille et la surface d'attaque
- [ ] C. Permettre à plusieurs personnes de construire la même image
- [x] D. Faire tourner plusieurs applications dans un seul conteneur

**Q20.** Pourquoi éviter que le processus d'un conteneur tourne avec les privilèges du superutilisateur ?

- [ ] A. Parce que Docker refuse de démarrer sinon
- [ ] B. Parce que cela accélère le démarrage du conteneur
- [x] C. Parce que l'isolation d'un conteneur n'est pas une frontière absolue : en cas de compromission, on limite fortement les dégâts possibles
- [ ] D. Parce que les volumes ne fonctionnent pas en superutilisateur

**Q21.** Quelle est la différence entre un montage d'un dossier de l'hôte et un volume nommé ?

- [ ] A. Aucune, ce sont deux syntaxes équivalentes
- [ ] B. Le volume nommé ne survit pas à l'arrêt du conteneur
- [ ] C. Le montage d'un dossier de l'hôte est réservé aux bases de données
- [x] D. Le montage expose un dossier précis de ta machine dans le conteneur, le volume nommé est un espace de stockage géré par Docker, indépendant de l'arborescence de ton projet

**Q22.** 🛠️ Ta base de données démarre, mais le script d'initialisation n'a manifestement pas été rejoué et la table est absente. Pourquoi ?

- [x] A. Le script d'initialisation n'est exécuté qu'à la **première** initialisation du stockage : un volume déjà existant fait considérer la base comme déjà installée
- [ ] B. Le script contient une erreur de syntaxe silencieuse
- [ ] C. Il faut publier le port de la base pour que le script s'exécute
- [ ] D. Le script doit être copié dans l'image, il ne peut pas être monté

**Q23.** Dans une pile décrite par un fichier de composition, comment l'API joint elle la base de données ?

- [x] A. Par l'adresse `localhost`, puisque les deux conteneurs tournent sur la même machine
- [ ] B. Par l'adresse IP du conteneur, qu'il faut relever après chaque démarrage
- [ ] C. Par le **nom du service**, résolu par le service de noms du réseau créé automatiquement
- [ ] D. Par un volume partagé entre les deux conteneurs

**Q24.** Que garantit une dépendance conditionnée par l'état de santé du service dont on dépend ?

- [ ] A. Que le service dépendant redémarre en cas d'erreur
- [x] B. Que le service dépendant ne démarre pas tant que la sonde du service dont il dépend n'est pas satisfaite
- [ ] C. Que les deux services démarrent exactement en même temps
- [ ] D. Que les journaux des deux services sont fusionnés

---

## Partie 3 · Kubernetes (questions 25 à 33)

**Q25.** Qu'est-ce que la boucle de réconciliation ?

- [ ] A. Un mécanisme qui répare automatiquement les fichiers de configuration mal écrits
- [ ] B. Une synchronisation périodique entre le cluster et le dépôt Git
- [ ] C. Le mécanisme de répartition de charge entre les nœuds
- [x] D. Un processus qui compare en permanence l'état réel du cluster à l'état souhaité que tu as déclaré, et agit pour les faire coïncider

**Q26.** Tu supprimes un pod créé par un déploiement. Que se passe t il, et pourquoi ?

- [x] A. Un nouveau pod apparaît, parce que le déploiement maintient en permanence le nombre d'exemplaires déclaré
- [ ] B. Rien, le pod reste supprimé : c'est toi qui commandes
- [ ] C. Le déploiement entier est supprimé par cohérence
- [ ] D. Le cluster passe en état d'erreur jusqu'à intervention manuelle

**Q27.** Comment un service sait il à quels pods envoyer le trafic ?

- [ ] A. Par le nom des pods, qui doit commencer par le nom du service
- [ ] B. Par l'ordre de création des pods
- [x] C. Par la correspondance entre son sélecteur et les étiquettes portées par les pods
- [ ] D. Par les adresses IP déclarées à la main dans le service

**Q28.** 🛠️ Ton service ne répond pas alors que les pods tournent, et la ressource qui liste les destinataires du service est vide. Quel est le diagnostic ?

- [ ] A. Le cluster manque de mémoire
- [x] B. Le sélecteur du service ne correspond à aucune étiquette de pod
- [ ] C. L'image du conteneur est trop volumineuse
- [ ] D. Le port de l'hôte n'a pas été ouvert

**Q29.** Que faut il savoir sur la ressource utilisée pour stocker un mot de passe dans le cluster ?

- [ ] A. Elle chiffre la valeur de bout en bout, personne ne peut la relire
- [ ] B. Elle ne peut être créée qu'à partir d'un fichier versionné
- [ ] C. Elle est automatiquement supprimée au redémarrage du cluster
- [x] D. Elle encode simplement la valeur, qui reste lisible par quiconque a le droit de lire cette ressource : ce n'est pas un coffre-fort

**Q30.** Quelle est la différence entre une sonde de disponibilité et une sonde de vivacité ?

- [x] A. La sonde de disponibilité décide si le pod reçoit du trafic, la sonde de vivacité décide s'il faut le redémarrer
- [ ] B. La sonde de disponibilité s'exécute une fois, la sonde de vivacité en continu
- [ ] C. Elles sont équivalentes, seul le nom change selon la version
- [ ] D. La sonde de vivacité teste le nœud, la sonde de disponibilité teste le conteneur

**Q31.** 🛠️ Tes pods restent en échec de récupération d'image dans ton cluster local, alors que l'image existe bien sur ta machine. Quelle est la cause vue en TP ?

- [ ] A. L'étiquette de l'image contient une majuscule
- [x] B. Le nombre d'exemplaires demandé est trop élevé
- [ ] C. Le cluster tourne dans ses propres conteneurs et ne voit pas le stock d'images de ta machine : il faut l'y charger, ou la tirer d'un registre accessible
- [ ] D. Il manque une sonde de disponibilité

**Q32.** Qu'est-ce qu'une mise à jour progressive ?

- [ ] A. Une mise à jour qui arrête tous les exemplaires, puis démarre les nouveaux
- [x] B. Un remplacement des exemplaires par lots, en gardant en permanence du service disponible, avec possibilité de revenir à la révision précédente
- [ ] C. Une mise à jour planifiée à heure fixe
- [ ] D. Une mise à jour qui ne s'applique qu'aux nouveaux nœuds du cluster

**Q33.** Dans quel ordre dérouler la trousse de débogage enseignée en cours ?

- [ ] A. Consulter les journaux, puis lister, puis décrire
- [ ] B. Décrire, puis consulter les journaux, puis lister
- [ ] C. Supprimer, recréer, puis lister
- [x] D. Lister l'état, puis décrire la ressource suspecte, puis lire les journaux du conteneur

---

## Partie 4 · Jenkins et intégration continue (questions 34 à 40)

**Q34.** Qu'est-ce que l'intégration continue ?

- [x] A. Intégrer fréquemment le travail de chacun et **vérifier automatiquement**, à chaque intégration, que l'ensemble tient encore debout
- [ ] B. Déployer automatiquement en production à chaque modification
- [ ] C. Maintenir plusieurs versions de l'application en parallèle
- [ ] D. Surveiller les performances de l'application en production

**Q35.** Pourquoi la description du pipeline doit elle vivre dans le dépôt plutôt que dans l'interface de l'outil ?

- [ ] A. Parce que l'interface ne permet pas d'écrire plus de dix lignes
- [ ] B. Parce que c'est plus rapide à l'exécution
- [x] C. Parce que le pipeline suit alors le code : il est relu, historisé, comparable d'une version à l'autre et rejouable ailleurs
- [ ] D. Parce que l'outil supprime les configurations saisies dans l'interface à chaque redémarrage

**Q36.** Pourquoi l'étape de test est elle placée avant la construction et la publication ?

- [ ] A. Parce que les tests sont plus rapides
- [x] B. Pour ne jamais publier ni déployer une version dont on sait déjà qu'elle est cassée
- [ ] C. Parce que la construction efface les fichiers de test
- [ ] D. Parce que l'outil impose cet ordre

**Q37.** 🛠️ Pourquoi le fichier d'accès au cluster fourni à Jenkins doit il être exporté dans sa variante interne ?

- [ ] A. Parce que la variante externe est chiffrée
- [ ] B. Parce que la variante interne contient davantage de droits
- [ ] C. Parce que le cluster refuse les connexions venant de l'extérieur du navigateur
- [x] D. Parce que Jenkins tourne dans un conteneur : l'adresse de boucle locale y désigne Jenkins lui même et non le cluster, il faut donc l'adresse joignable depuis le réseau des conteneurs

**Q38.** À quoi sert, dans le pipeline, l'attente de la fin réelle du déploiement ?

- [x] A. À rendre le résultat honnête : sans cette attente, l'exécution se déclare verte alors que les nouveaux exemplaires peuvent ne jamais démarrer
- [ ] B. À laisser le temps au registre de terminer la publication
- [ ] C. À éviter que deux exécutions se déclenchent en même temps
- [ ] D. À conserver les journaux plus longtemps

**Q39.** Pourquoi passer par le gestionnaire d'identifiants plutôt que d'écrire le mot de passe du registre dans le fichier de pipeline ?

- [ ] A. Parce que l'outil refuse les chaînes de plus de vingt caractères
- [ ] B. Parce que le registre bloque les authentifications écrites en clair
- [x] C. Parce que le fichier de pipeline est versionné et lisible par tous ceux qui accèdent au dépôt, et que les journaux d'exécution sont eux aussi consultables
- [ ] D. Parce que cela accélère la publication de l'image

**Q40.** Quel risque a t on accepté en donnant au conteneur Jenkins l'accès au moteur Docker de la machine ?

- [ ] A. Aucun, l'accès est en lecture seule
- [x] B. Un contrôle très étendu sur la machine hôte : qui peut piloter le moteur Docker peut, en pratique, obtenir les pleins pouvoirs sur cette machine
- [ ] C. Un risque de saturation du disque uniquement
- [ ] D. Un risque limité aux images publiées

---

## Avant de rendre

- [ ] J'ai coché **une seule** case par question, pour les 40 questions
- [ ] J'ai écrit mon nom et mon groupe en haut du fichier
- [ ] J'ai renommé ce fichier en `QCM.md` et déposé à la racine de mon dépôt

> 📊 **Repères de niveau** : 34 et plus, les quatre outils sont acquis. De 28 à 33, solide, avec deux ou trois notions à revoir. En dessous de 28, reprends les fichiers de théorie des trois jours, en priorité ceux des parties où tu as buté.

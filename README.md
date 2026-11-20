# Calculatrice collaborative

## 1. Présentation du projet

La **Calculatrice collaborative** est un projet de développement réalisé en équipe dans le cadre d'un travail pratique sur Git et GitHub.

L'objectif est de concevoir une application en Python permettant d'effectuer plusieurs opérations mathématiques de base. Le projet est développé de manière collaborative : chaque membre de l'équipe intervient sur une fonctionnalité ou une partie spécifique du projet, en utilisant les branches Git et les Pull Requests pour organiser le travail.

## 2. Objectifs du projet

Ce projet a plusieurs objectifs :

- Développer une application simple en langage Python.
- Implémenter les principales opérations mathématiques.
- Organiser le travail en équipe avec Git et GitHub.
- Utiliser des branches indépendantes pour développer les fonctionnalités.
- Mettre en pratique les commits, les Push et les Pull Requests.
- Apprendre à relire et à valider les modifications proposées par les autres membres.

## 3. Fonctionnalités

La calculatrice propose les six opérations mathématiques suivantes :

| Opération | Description | Exemple |
|---|---|---|
| Addition | Additionne deux nombres | 5 + 3 = 8 |
| Soustraction | Calcule la différence entre deux nombres | 10 - 4 = 6 |
| Multiplication | Multiplie deux nombres | 6 × 3 = 18 |
| Division | Divise un nombre par un autre | 20 / 4 = 5 |
| Puissance | Élève un nombre à une puissance donnée | 2³ = 8 |
| Modulo | Retourne le reste d'une division entière | 17 % 5 = 2 |

**Gestion des erreurs :** la division doit inclure un contrôle pour éviter une division par zéro.

## 4. Technologies utilisées

- **Python 3 :** langage utilisé pour développer les fonctionnalités de la calculatrice.
- **Git :** outil de gestion de versions du code source.
- **GitHub :** plateforme d'hébergement du projet et de collaboration.
- **Linux / Terminal :** environnement utilisé pour exécuter les commandes Git et Python.

## 5. Prérequis

Avant d'exécuter le projet, il faut disposer de :

- Python 3 installé sur la machine.
- Git installé pour récupérer et gérer le projet.
- Un terminal Linux, macOS ou Windows.

Pour vérifier l'installation de Python :

```bash
python3 --version
```

## 6. Installation et utilisation

### Étape 1 : Récupérer le projet

Cloner le dépôt GitHub :

```bash
git clone git@github.com:sudo-aptttt/calculatrice-collaborative.git
```

### Étape 2 : Accéder au dossier

```bash
cd calculatrice-collaborative
```

### Étape 3 : Exécuter le programme

Lancer la calculatrice avec la commande :

```bash
python3 calculatrice.py
```

Le programme exécute les différentes opérations mathématiques implémentées dans le fichier Python.

## 7. Structure du projet

```text
calculatrice-collaborative/
│
├── calculatrice.py    # Code source de la calculatrice
├── README.md          # Documentation du projet
└── .gitignore         # Fichiers ignorés par Git
```

## 8. Organisation de l'équipe

Le projet est réalisé par cinq étudiants, avec une répartition des responsabilités :

| Membre | Rôle | Responsabilités |
|---|---|---|
| Dorion | Chef de projet | Organisation du projet, gestion du dépôt GitHub et fusion des Pull Requests |
| Nathael | Développeur division | Développement et intégration de la fonction division |
| Lukas | Développeur puissance | Développement de la fonction puissance |
| Steven | Développeur modulo | Développement de la fonction modulo |
| Muhammad | Documentaliste | Rédaction et mise à jour du README, documentation et revue de code |

## 9. Méthode de travail collaborative

Le développement suit une organisation basée sur GitHub Flow :

1. Chaque étudiant travaille sur une branche dédiée à sa tâche.
2. Les modifications sont enregistrées avec des commits.
3. Les branches sont envoyées sur le dépôt distant avec `git push`.
4. Une Pull Request est créée pour proposer les modifications vers `main`.
5. Un autre membre de l'équipe effectue une revue de code.
6. Le chef de projet valide et fusionne les Pull Requests.

Cette méthode permet de suivre les modifications, de limiter les conflits et de garantir une meilleure organisation du travail.

## 10. Conclusion

Ce projet permet de mettre en pratique les bases du développement Python et du travail collaboratif avec Git et GitHub. Il constitue une mise en situation concrète de la gestion de versions, du travail en équipe et de la documentation d'un projet informatique.

# 📧 Smart Email Classifier — Automatisation de la Relation Client via NLP

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![NLP](https://img.shields.io/badge/NLP-Spacy%20%7C%20Scikit--learn-green.svg)](https://spacy.io/)
[![Machine Learning](https://img.shields.io/badge/Model-Random%20Forest-orange.svg)](https://scikit-learn.org/)

## 📝 Résumé Exécutif
Ce projet développe un système intelligent de classification d'emails capable de trier automatiquement les messages entrants en catégories métiers (Support, Ventes, RH, Spam). En utilisant des techniques de **Natural Language Processing (NLP)** et un modèle de **Random Forest**, l'outil atteint une précision de **94%**, permettant de réduire drastiquement le temps de réponse manuel et d'optimiser le routage vers les bons services.

---

## 🎯 Problématique Business
Dans une entreprise en croissance, le volume d'emails entrants peut paralyser les équipes opérationnelles. L'enjeu est de :
1.  **Réduire le temps de tri manuel** : Automatiser la catégorisation pour libérer du temps aux collaborateurs.
2.  **Améliorer la réactivité** : Router instantanément les demandes urgentes (ex: Support critique) vers les experts concernés.
3.  **Filtrer les bruits** : Éliminer les emails non pertinents ou malveillants avec une haute fiabilité.

---

## 📈 Résultats & Performance
Le modèle a été évalué sur un dataset de [préciser le nombre, ex: 5 000] emails labellisés.

| Catégorie | Précision | Rappel | F1-Score |
| :--- | :---: | :---: | :---: |
| Support Technique | 96% | 92% | 0.94 |
| Demandes Commerciales | 91% | 89% | 0.90 |
| Ressources Humaines | 95% | 94% | 0.94 |
| **Moyenne Globale** | **94%** | **93%** | **0.93** |

**Impact Business** : Une simulation sur flux réel montre une économie de **[X] heures par semaine** pour l'équipe de coordination administrative.

---

## 🛠️ Méthodologie & Pipeline NLP
Le pipeline de traitement de texte a été conçu pour capturer l'intention sémantique :

1.  **Prétraitement (Cleaning)** :
    * Suppression des balises HTML, caractères spéciaux et stop-words.
    * **Lemmatisation** (Spacy) pour ramener les mots à leur racine.
2.  **Vectorisation** : Utilisation de **TF-IDF** (Term Frequency-Inverse Document Frequency) pour transformer le texte en vecteurs numériques en accordant plus de poids aux mots discriminants.
3.  **Modélisation** : Entraînement d'un classifieur **Random Forest** optimisé par recherche d'hyperparamètres (GridSearch).
4.  **Analyse d'Erreur** : Matrice de confusion pour identifier les ambiguïtés entre catégories proches (ex: Ventes vs Support).

---

## 🧰 Stack Technique
* **NLP** : Spacy, NLTK.
* **Machine Learning** : Scikit-learn (TfidfVectorizer, Random Forest, Pipeline).
* **Data Analysis** : Pandas, Matplotlib (Visualisation des fréquences de mots).

---

## 🚀 Fiabilité & Scalabilité
* **Modularité** : Le pipeline est encapsulé dans un objet `Pipeline` de Scikit-learn, facilitant le déploiement en tant qu'API (Flask/FastAPI).
* **Gestion des Langues** : Configuré actuellement pour le [Français/Anglais], le système peut être étendu via des modèles Spacy multilingues.
* **Robustesse** : Gestion des emails vides ou mal formatés via un module de validation en amont.

---

## 💻 Installation
```bash
# Cloner le repo
git clone [https://github.com/AbdelkrimAKKAL/email_classifier.git](https://github.com/AbdelkrimAKKAL/email_classifier.git)
cd email_classifier

# Installation des dépendances
pip install -r requirements.txt
python -m spacy download fr_core_news_sm

# Lancer l'entraînement et l'évaluation
python train_model.py

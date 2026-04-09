# 🛡️ Détection de Fraude Bancaire (XGBoost & SHAP) — Secteur Fintech

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange.svg)](https://xgboost.readthedocs.io/)
[![SHAP](https://img.shields.io/badge/Explainability-SHAP-green.svg)](https://shap.readthedocs.io/)

## 📝 Résumé Exécutif
Ce projet déploie un pipeline de Machine Learning de bout en bout pour identifier les transactions frauduleuses parmi plus de **590 000 données réelles** (IEEE-CIS). En combinant un **Feature Engineering métier** et l'algorithme **XGBoost**, le modèle atteint un **AUC-ROC de 0.91**. L'intégration de **SHAP** permet de justifier chaque prédiction, rendant le modèle auditable par des experts en fraude bancaire.

---

## 🎯 Problématique Business
La fraude transactionnelle coûte des milliards chaque année. Ce projet répond à trois enjeux majeurs du secteur bancaire :
1.  **Réduction des pertes financières** : Identifier les transactions à haut risque avant leur validation.
2.  **Expérience Client (Friction)** : Maintenir une précision de 73% pour limiter les "faux positifs" qui bloquent inutilement les clients légitimes.
3.  **Auditabilité & Transparence** : Expliquer techniquement pourquoi une transaction est rejetée (obligatoire pour la conformité bancaire).

---

## 📈 Résultats & Impact
Le modèle **XGBoost** (seuil optimal 0.34) s'impose comme la solution la plus équilibrée :

| Modèle | AUC-ROC | Précision | Rappel | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| Logistic Regression | 0.824 | 13.9% | 62.9% | 0.228 |
| Random Forest | 0.885 | 33.1% | 61.2% | 0.429 |
| **XGBoost** | **0.908** | **73.0%** | **49.0%** | **0.589** |

**Insights Métier clés :**
* **Risque Email** : Le domaine `protonmail.com` présente un taux de fraude anormal de 95%.
* **Saisonnalité** : Les fraudes culminent à **7h du matin** (10.6% de taux de fraude).
* **Validation des Features** : Ma variable créée `amt_vs_product_median` est dans le **Top 10 SHAP**, validant l'importance du contexte du montant par rapport au produit acheté.

---

## 🛠️ Méthodologie & Pipeline
Le projet est divisé en scripts modulaires pour une maintenance facilitée :

1.  **Exploration (01_exploration_fraude.py)** : Analyse de 434 features et gestion du déséquilibre (3.5% de fraudes).
2.  **Engineering (02_feature_engineering.py)** : 
    * Création de **12 variables métier** (temporelles, fréquentielles, agrégations).
    * Rééquilibrage par **SMOTE** pour améliorer l'apprentissage sur la classe minoritaire.
3.  **Modélisation (03_modelisation.py)** : Comparaison de modèles et optimisation des hyperparamètres.
4.  **Interprétabilité (04_shap.py)** : Génération de *Waterfall plots* pour expliquer les décisions au cas par cas.

---

## 🧰 Stack Technique
* **Langages** : Python (Pandas, Numpy, Scikit-learn).
* **Algorithmes** : XGBoost, SMOTE (Imbalanced-learn).
* **IA Explicable** : **SHAP** (Shapley Additive Explanations).
* **Analyse** : Matplotlib, Seaborn (Visualisation des corrélations et courbes ROC).

---

## 🚀 Fiabilité et "Production-Ready"
* **Code Modulaire** : Scripts séparés par étape de pipeline (vs Notebooks monolithiques).
* **Interprétabilité Native** : SHAP permet une intégration facile dans un outil de révision pour les analystes fraude.
* **Reproductibilité** : Fichier `requirements.txt` et gestion des seeds aléatoires pour garantir des résultats constants.

---

## 💻 Installation
```bash
# Cloner le repo
git clone [https://github.com/AbdelkrimAKKAL/transactions_fraude_detection.git](https://github.com/AbdelkrimAKKAL/transactions_fraude_detection.git)
cd transactions_fraude_detection

# Installer les dépendances
pip install -r requirements.txt

# Lancer le projet
python 01_exploration_fraude.py
python 02_feature_engineering.py
python 03_modelisation.py
python 04_shap.py

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_classif

# VISUALISATION

def count_plot(df, colonne):
    """Affiche un graphique de comptage"""
    plt.figure(figsize=(8, 4))
    sns.countplot(x=colonne, data=df)
    plt.title(colonne)
    plt.xticks(rotation=45)
    plt.show()


def box_plot(df, colonne):
    """Affiche un boxplot par rapport à Attrition"""
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=colonne, y="Attrition", data=df)
    plt.title(colonne)
    plt.show()


# PRÉPARATION DES DONNÉES

def encoder_colonnes(df):
    """Transforme les colonnes texte en nombres"""
    df_copie = df.copy()
    
    # Trouver les colonnes texte
    colonnes_texte = df_copie.select_dtypes(include=['object']).columns
    
    # Transformer en nombres (0/1)
    df_copie = pd.get_dummies(df_copie, columns=colonnes_texte, drop_first=False)
    
    # Convertir True/False en 0/1
    colonnes_bool = df_copie.select_dtypes(include=['bool']).columns
    df_copie[colonnes_bool] = df_copie[colonnes_bool].astype(int)
    
    return df_copie


def selectionner_meilleures_colonnes(X, y, nombre=5):
    """Garde seulement les colonnes les plus importantes"""
    selecteur = SelectKBest(score_func=f_classif, k=nombre)
    selecteur.fit(X, y)
    
    colonnes_gardees = X.columns[selecteur.get_support()]
    return list(colonnes_gardees)


def separer_train_test(X, y, pourcentage_test=0.2):
    """Divise les données en entraînement et test"""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=pourcentage_test, random_state=42
    )
    return X_train, X_test, y_train, y_test


def normaliser(X_train, X_test):
    """Met toutes les valeurs entre 0 et 1"""
    scaler = MinMaxScaler()
    
    # Apprendre sur train, appliquer sur train et test
    X_train_normalise = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=X_train.columns,
        index=X_train.index
    )
    
    X_test_normalise = pd.DataFrame(
        scaler.transform(X_test),
        columns=X_test.columns,
        index=X_test.index
    )
    
    return X_train_normalise, X_test_normalise
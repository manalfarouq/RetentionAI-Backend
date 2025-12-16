import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns

#* fct pour la visualisation avec count_plot
def count_plot_affichage(dataframe_name, column_name):

    plt.figure(figsize=(8, 4))
    sns.countplot(x=column_name, data=dataframe_name)
    plt.title(f"{column_name}")
    plt.xticks(rotation=45)
    plt.show()

#* fct pour la visualisation avec box_plot
def box_plot_affichage(dataframe_name, column_name):

    plt.figure(figsize=(8, 4))
    sns.boxplot(x=column_name, y="Attrition", data=dataframe_name)
    plt.title(f"{column_name}")
    # plt.xticks(rotation=45)
    plt.show()
    
#* fct pour encode toutes les colonnes catégorielles spécifiées en valeurs numeriques
def encode_categorical(df):
    df_encoded = df.copy()

    # Sélection des colonnes catégorielles
    cat_cols = df_encoded.select_dtypes(include=['object']).columns

    # One-Hot Encoding
    df_encoded = pd.get_dummies(
        df_encoded,
        columns=cat_cols,
        drop_first=False
    )

    # Conversion des booléens en 0/1
    bool_cols = df_encoded.select_dtypes(include=['bool']).columns
    df_encoded[bool_cols] = df_encoded[bool_cols].astype(int)

    return df_encoded    


#* fct pour selectkbest pour choisir les K (nombre) de colonnes les plus pertinentes pour la prédiction
def select_kbest_columns(df_encoded, df_original, k=5):
    from sklearn.feature_selection import SelectKBest, f_classif

    # Target encodée
    y = (df_original['Attrition'] == 'Yes').astype(int)

    # Features : on enlève toute colonne liée à Attrition
    X = df_encoded.drop(
        columns=[col for col in df_encoded.columns if 'Attrition' in col],
        errors='ignore'
    )

    # SelectKBest
    selector = SelectKBest(score_func=f_classif, k=k)
    selector.fit(X, y)

    # Colonnes sélectionnées
    selected_columns = X.columns[selector.get_support()]

    return list(selected_columns)

#* Fonction pour séparer le dataset en train/test
def split_data(X, y, test_size=0.2, random_state=42):
    from sklearn.model_selection import train_test_split
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test


#* Fonction pour la normalisation
def normalisation(X_train, X_test):
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler  
    
    scaler = MinMaxScaler()
    
    # Fit sur train, transform sur train et test
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train), columns=X_train.columns, index=X_train.index
    )
    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test), columns=X_test.columns, index=X_test.index
    )
    
    return X_train_scaled, X_test_scaled

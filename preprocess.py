'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import numpy as np
import pandas as pd

def round_decimals(my_df):
    '''
        Rounds all the numbers in the dataframe to two decimal points

        args:
            my_df: The dataframe to preprocess
        returns:
            The dataframe with rounded numbers
    '''
    # TODO : Round the dataframe
    numeric_cols = my_df.select_dtypes(include=['float64']).columns
    for col in numeric_cols:
        my_df[col] = my_df[col].round(2)
    
    return my_df


def get_range(col, df1, df2):
    '''
        An array containing the minimum and maximum values for the given
        column in the two dataframes.

        args:
            col: The name of the column for which we want the range
            df1: The first dataframe containing a column with the given name
            df2: The first dataframe containing a column with the given name
        returns:
            The minimum and maximum values across the two dataframes
    '''
    # TODO : Get the range from the dataframes
    min_val = min(df1[col].min(), df2[col].min())  # Find the overall minimum
    max_val = max(df1[col].max(), df2[col].max())  # Find the overall maximum
    return [min_val, max_val]  # Return as an array


def combine_dfs(df1, df2):
    '''
        Combines the two dataframes, adding a column 'Year' with the
        value 2000 for the rows from the first dataframe and the value
        2015 for the rows from the second dataframe.

        args:
            df1: The first dataframe to combine
            df2: The second dataframe, to be appended to the first
        returns:
            The dataframe containing both dataframes provided as arg.
            Each row of the resulting dataframe has a column 'Year'
            containing the value 2000 or 2015, depending on its
            original dataframe.
    '''
    # ✅ Créer une copie des DataFrames pour éviter de modifier les originaux
    df1_copy = df1.copy()
    df2_copy = df2.copy()

    # ✅ Ajouter la colonne 'Year' sans modifier les DataFrames d'entrée
    df1_copy['Year'] = 2000  
    df2_copy['Year'] = 2015  

    # ✅ Concaténer les DataFrames et retourner le résultat
    combined_df = pd.concat([df1_copy, df2_copy], ignore_index=True)

    return combined_df  # Retourne le DataFrame combiné


def sort_dy_by_yr_continent(my_df):
    '''
        Sorts the dataframe by year and then by continent.

        args:
            my_df: The dataframe to sort
        returns:
            The sorted dataframe.

    '''
    # TODO : Sort the dataframe

    my_df_copy = my_df.copy()  # Create a copy of the dataframe to avoid modifying the original
    sorted_df = my_df_copy.sort_values(by=['Year', 'Continent'], ignore_index=True)
    return sorted_df  # Return the sorted dataframe


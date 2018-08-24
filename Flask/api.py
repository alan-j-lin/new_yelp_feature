import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# loading pickle files from the model folder
bar_df = pd.read_csv('./model/bar_df.csv', index_col = 0)
similarity_df = pd.read_csv('./model/similarity_df.csv', index_col = 0)
bar_df.set_index('name', inplace = True)

def get_similar_bars(df, candidate_bars, n, threshold = 0.5):
    """
    calculates which bars are most similar to the inputs. Must not return
    the bars that were inputted.

    Parameters
    ----------
    df = cosine_similarity dataframe
    candidate_bars: list of some bars
    n = number of bars to return


    Returns
    -------
    ranked_bars: list of bars ranked in similarity
    """
    bars = [bar for bar in candidate_bars if bar in df.columns]
    if len(bars) == 0:
        return None
    else:
        bars_summed = df[bars].apply(lambda row: np.sum(row), axis=1)
        bars_summed = bars_summed.sort_values(ascending=False)
        ranked_bars = bars_summed.index[bars_summed.index.isin(bars)==False]
        similarity_scores = bars_summed.values
        ranked_bars = ranked_bars.tolist()
        ranked_bars = [ibar for ix, ibar in enumerate(ranked_bars) if similarity_scores[ix] >= threshold]
        if n is None:
            return ranked_bars
        else:
            return ranked_bars[:n]


def get_recommendation(data):

    """
    calculates which bars are the most similar based on input,
    returns dictionary with nearest bars and their corresponding states and cities

    Parameters
    ----------
    data is a dictionary:
    'Bar_List': List of bars
    'Neighbors': Number of neighbors
    'Specific_State': All states if N/A otherwise only bars from state specified
    'Threshold': threshold for the similarity score

    Returns
    -------
    neighbors: dictionary:
    'Names': list of rank ordered bars
    'States': list of states corresponding to bar
    'Cities': list of cities corresponding to bars
    """

    selected_bars = data['Bar_List']
    n_neighbors = int(data['Neighbors'])
    specific_state = data['Specific_State']
    threshold = float(data['Threshold'])

    neighbor_names = [''] * 10
    neighbor_states = [''] * 10
    neighbor_cities = [''] * 10

    filtered_bars = []

    neighbors = {

        'Names': neighbor_names,
        'States': neighbor_states,
        'Cities': neighbor_cities

    }

    for ibar in selected_bars:
        if ibar != '':
            filtered_bars.append(ibar)
        else:
            pass

    if len(filtered_bars) == 0:

        return neighbors

    else:

        if specific_state != 'N/A':
            subset_df = bar_df[bar_df['state'] == specific_state]
            subset_similarity_df = similarity_df.loc[subset_df.index.values]
        else:
            subset_similarity_df = similarity_df

        output_names = get_similar_bars(subset_similarity_df, selected_bars, n_neighbors, threshold)

        if output_names == None:

            return neighbors

        else:

            output_states = []
            output_cities = []

            for name in output_names:
                i_state = bar_df['state'].loc[name]
                i_city = bar_df['city'].loc[name]

                if type(i_state) == str:
                    output_states.append(i_state)
                else:
                    output_states.append('')

                if type(i_city) == str:
                    output_cities.append(i_city)
                else:
                    output_cities.append('')

            for ix in range(len(output_names)):
                neighbor_names[ix] = output_names[ix]
                neighbor_states[ix] = output_states[ix]
                neighbor_cities[ix] = output_cities[ix]


            neighbors = {

                'Names': neighbor_names,
                'States': neighbor_states,
                'Cities': neighbor_cities

            }

            return neighbors

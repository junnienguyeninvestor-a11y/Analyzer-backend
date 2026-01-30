import pandas as pd

# Fetch Data
def data_to_pd(data, columns, column_num) :
    # Convert Data to Pandas DataFrame
    df = pd.DataFrame([row[:column_num] for row in data], columns=columns)
    return df

def pd_to_dict(dataframe, filtering_column, filter_word, groupby_word, get_words_arr) :
    # Individual Name List in Waiting following Account
    dictionary = dataframe[dataframe[filtering_column]==filter_word].groupby(groupby_word)[get_words_arr].apply(lambda x: x.to_dict(orient='list')).to_dict()
    return dictionary


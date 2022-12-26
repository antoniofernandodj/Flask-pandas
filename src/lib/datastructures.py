from typing import List, Dict, Any
from pandas import DataFrame

def dataframe_to_front_end(
    dataframe: DataFrame,
    drop_nan=True,
    drop_nan_axis=1
) -> Dict[str, List[Any]]:
    """
    Recebe um dataframe pandas e retorna um dicionário python ponto
    para ser consumido no front-end
    """
    
    if drop_nan:
        dataframe_dict = dataframe.dropna(axis=drop_nan_axis).to_dict()
    else:
        dataframe_dict = dataframe.to_dict()

    dict_values = dataframe_dict.values()
    
    column_values = [ item.values() for item in dict_values if item ]
    df = {
        'lines': zip(*column_values),
        'keys': dataframe_dict.keys()
    }
    return df
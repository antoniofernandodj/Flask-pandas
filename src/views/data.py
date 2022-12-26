from flask import Blueprint, render_template
from pandas import read_csv
from pathlib import Path
from os.path import join
from ..lib import config as c
from ..lib import datastructures
import seaborn as sns
from matplotlib import pyplot as plt


bp = Blueprint("bp", __name__)


@bp.route("/")
def table():
    file = join(c.CSV_FOLDER, 'ex3.csv')
    dataframe = read_csv(file)
    df = datastructures.dataframe_to_front_end(
        dataframe=dataframe
    )
    sns.lineplot(
        x='Period',
        y='General_abortion_rate',
        data=dataframe
    )
    img = join(c.TEMP_FOLDER, 'temp.png')
    plt.savefig(img)
    
    return render_template(
        'index.html', df=df
    )
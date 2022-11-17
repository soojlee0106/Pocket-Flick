# Pocket-Flick 📽️

ML program that provides movie recommendations, based on plots.

## Used Data

This model is trained using the TMDB 5000 Movie Dataset.
The link to the dataset can be found in <https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata>. The model is inpired by Ibtesam Ahmed's code <https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system>.

## Main algorithm

This model uses the basic weighted rating formula for IMDB.  
NLP is also used to find the similarity of the movie plots to recommend.

## File Information

- movie.py  
Contains the model that gives recommendation on plot similarity.

- plot.py  
Maps out chart that shows most popular films depending on IMDB ratings.

## Local UI development

Run the command below.

```sh
python -m streamlit run [gui.py]
```

The UI should be on <http://localhost:8501/>

# Movie Genre Analysis

This repository contains a Python script for analyzing the distribution of genres within a dataset of movies. The script employs Pandas to categorize movies into distinct genre classifications, with an emphasis on identifying genres that best capture the primary thematic essence of each film.

## Overview

The provided Python script reads data from a CSV file containing information about movies. It performs the following key tasks:

- Removes irrelevant columns to streamline the dataset.
- Extracts and categorizes movies into different genres by creating binary columns.
- Calculates the number of movies for each genre and presents the counts in a dictionary.
- Determines "pure" movies within specific genres, excluding those heavily associated with other genres.

## How to Use

1. Clone this repository to your local machine.
2. Ensure you have the required dependencies installed (`pandas`, `matplotlib`).
3. Replace the `imdb_top_1000.csv` file with your own movie dataset if needed.
4. Run the script using a Python interpreter: `python movie_genre_analysis.py`.
5. Review the console output to gain insights into the distribution of movie genres.

## Dependencies

- Python 3.x
- Pandas
- Matplotlib

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


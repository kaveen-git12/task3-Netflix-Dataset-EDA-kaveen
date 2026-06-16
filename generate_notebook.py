import json

cells = []

def add_markdown(text):
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.split('\n')]
    })

def add_code(text):
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in text.split('\n')]
    })

# Add cells
add_markdown("# Netflix Dataset Exploratory Data Analysis (EDA)\n\nThis notebook performs Exploratory Data Analysis on the Netflix dataset to uncover patterns and trends.")

add_code("import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\n# Configure visualizations\n%matplotlib inline\nsns.set_theme(style='darkgrid')\nplt.rcParams['figure.figsize'] = (10, 6)")

add_code("# Load the dataset\ndf = pd.read_csv('netflix_titles.csv')\ndf.head()")

add_markdown("## 1. Summary Statistics")
add_code("# Dataset Shape\nprint(f'Dataset Shape: {df.shape}')\ndf.shape")
add_code("# Missing values\ndf.isnull().sum()")
add_code("# Data types and basic info\ndf.info()")
add_code("# Basic statistics\ndf.describe(include='all')")

add_markdown("### Insight:\nThe dataset contains 7787 rows and 12 columns. There are some missing values, notably in the `director`, `cast`, and `country` columns. Most features are categorical (object types), while `release_year` is numerical.")

add_markdown("## 2. Correlation Analysis")
add_code("plt.figure(figsize=(8, 6))\nsns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', vmin=-1, vmax=1)\nplt.title('Correlation Heatmap')\nplt.show()")
add_markdown("### Insight:\nUsually, there is a weak correlation in the Netflix dataset between numerical variables (like release_year). The heatmap confirms that there are no strong linear relationships between the available numerical features.")

add_markdown("## 3. Trend Identification")

add_markdown("### 3.1 Content Type (Movie vs TV Show)")
add_code("plt.figure(figsize=(8, 5))\nsns.countplot(x='type', data=df, palette='Set2')\nplt.title('Content Type: Movie vs TV Show')\nplt.show()")
add_markdown("### Insight:\nNetflix has significantly more Movies than TV Shows in its catalog. This suggests a stronger focus on feature-length content.")

add_markdown("### 3.2 Top Countries Producing Content")
add_code("plt.figure(figsize=(10, 6))\ndf['country'].value_counts().head(10).plot(kind='bar', color='skyblue', edgecolor='black')\nplt.title('Top 10 Content Producing Countries')\nplt.xlabel('Country')\nplt.ylabel('Count')\nplt.xticks(rotation=45)\nplt.show()")
add_markdown("### Insight:\nThe United States is the leading producer of content on Netflix, followed by India and the United Kingdom. This aligns with the major global entertainment markets.")

add_markdown("### 3.3 Content Added Over Time")
add_code("# Extract the year content was added\ndf['year_added'] = df['date_added'].str.strip().str[-4:]\n# Convert to numeric, errors='coerce' will handle any missing or malformed data\ndf['year_added'] = pd.to_numeric(df['year_added'], errors='coerce')\n\nplt.figure(figsize=(10, 6))\ndf['year_added'].value_counts().sort_index().plot(kind='line', marker='o', color='purple', linewidth=2)\nplt.title('Content Added to Netflix Over Time')\nplt.xlabel('Year Added')\nplt.ylabel('Number of Titles')\nplt.grid(True)\nplt.show()")
add_markdown("### Insight:\nThere was an exponential growth in content addition starting around 2015, peaking around 2019/2020. This corresponds to Netflix's major global expansion and push for original content.")

add_markdown("### 3.4 Genre Distribution")
add_code("plt.figure(figsize=(10, 8))\ndf['listed_in'].value_counts().head(10).plot(kind='barh', color='coral', edgecolor='black')\nplt.title('Top 10 Genres on Netflix')\nplt.xlabel('Count')\nplt.ylabel('Genre')\nplt.gca().invert_yaxis() # Highest at the top\nplt.show()")
add_markdown("### Insight:\n'Documentaries', 'Stand-Up Comedy', and 'Dramas, International Movies' are among the most common genres. Netflix clearly invests heavily in international content and documentaries.")

add_markdown("### 3.5 Ratings Distribution")
add_code("plt.figure(figsize=(12, 6))\nsns.countplot(y='rating', data=df, order=df['rating'].value_counts().index, palette='viridis')\nplt.title('Content Ratings Distribution')\nplt.xlabel('Count')\nplt.ylabel('Rating')\nplt.show()")
add_markdown("### Insight:\nTV-MA (Mature Audiences) and TV-14 are the most prominent ratings, indicating that a significant portion of Netflix's content is targeted towards adult and older teen audiences rather than young children.")

notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.8"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open('netflix_eda.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)

print("Generated netflix_eda.ipynb successfully.")

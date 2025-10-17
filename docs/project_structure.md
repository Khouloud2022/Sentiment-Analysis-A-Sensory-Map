scent-of-tunisia/
├── data/                  # Raw and processed data files
│   ├── raw/               # Scraped data (CSVs from Twitter/X, Instagram, TripAdvisor)
│   │   ├── twitter_scents.csv
│   │   ├── insta_scents.csv
│   │   └── tripadvisor_reviews.csv
│   └── processed/         # Cleaned data ready for analysis
│       └── cleaned_data.csv
├── notebooks/             # Jupyter/Colab notebooks for experimentation
│   ├── scrape.ipynb       # Data collection scripts (Twitter/X Instagram, TripAdvisor)
│   ├── sentiment_analysis.ipynb  # Sentiment processing (TextBlob, AraBERT)
│   └── mapping.ipynb      # GIS mapping (uMap exports)
├── src/                   # Reusable Python scripts/modules
│   ├── __init__.py        # Makes src a package (optional)
│   ├── scrape.py          # Functions for web scraping
│   ├── sentiment.py       # Sentiment analysis functions
│   └── mapping.py         # Mapping and visualization functions
├── maps/                  # Output maps and visuals
│   ├── tunis_scent_map.html  # Exported uMap files
│   └── sentiment_chart.png   # Generated charts (e.g., from Matplotlib)
├── docs/                  # Documentation beyond README
│   └── project_structure.md  # This file
├── .gitignore             # Git ignore file (e.g., ignore data/raw/)
├── requirements.txt       # Python dependencies (e.g., tweepy, instaloader, textblob)
├── README.md              # Project overview, setup instructions
└── LICENSE                # MIT or your chosen license
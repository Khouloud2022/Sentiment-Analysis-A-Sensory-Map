# The Scent of Tunisia A Sensory City Map
> Analyzing Urban Spaces with Sensory Sentiment Analysis

## 🎯 Overview
The Scent of Tunisia is an open-source project that maps the olfactory (sense of smell) experiences of Tunisian urban spaces using sentiment analysis on social media data. By scraping geotagged posts from Twitter/X and Instagram, we uncover how scents—like jasmine in the medina, spices in souks, or sea breezes in Sousse—shape emotions, memories, and perceptions of cities.
This hybrid approach combines web scraping, NLP sentiment analysis, and free GIS mapping to create an interactive sensory city map. It's designed for limited resources: no paid tools, runs on Google Colab, and focuses on Arabic/French/English posts.

## 🚀 Objectives
- Collect real-time olfactory mentions from social media in Tunisian cities.
- Analyze sentiment tied to scents (e.g., "spices = positive/nostalgic").
- Visualize **scent-sentiment hotspots** on interactive maps.
- Promote **inclusive urban design** by highlighting sensory equity in the Global South.

## 📊 Data Sources
- Twitter/X & Instagram: Geotagged posts with keywords like ريحة (smell), odeur, jasmine, souk.
- Web Scraping: Free APIs (Twitter Basic Tier) + manual/Instaloader.
- No proprietary data—fully ethical and open.

## 🛠️ Tech Stack
| Category          | Tools                          |
|-------------------|--------------------------------|
| Scraping          | Tweepy, Instaloader            |
| Sentiment         | TextBlob, AraBERT (Hugging Face) |
| Analysis          | Pandas, Google Colab           |
| Mapping           | uMap (OpenStreetMap), QGIS     |
| Visualization     | Google Data Studio, Matplotlib |

## 📂 Project Structure

```
Sentiment-Analysis-A-Sensory-Map/
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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


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
├── data/              # Scraped CSVs (tweets, posts)
├── notebooks/         # Colab notebooks: scrape.ipynb, analyze.ipynb, map.ipynb
├── src/
│   ├── scrape.py      # Web scraping scripts
│   ├── sentiment.py   # Analysis pipeline
│   └── mapping.py     # uMap export
├── maps/              # Generated interactive maps
├── requirements.txt   # Dependencies
└── README.md
```


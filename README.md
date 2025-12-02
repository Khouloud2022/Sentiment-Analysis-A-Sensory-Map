// ...existing code...
# The Scent of Tunisia — A Sensory City Map


## TL;DR
This repository implements an end-to-end pipeline to collect geotagged social-media posts, extract olfactory mentions, run language-aware sentiment analysis, and produce GIS-ready outputs for visualization. Key artifacts and entry points are listed below.

## Architecture (high level)
- Data ingestion: scrapers export CSV/GeoJSON into [data/raw/](data/raw/).
- ETL / preprocessing: cleaning, deduplication, language detection, tokenization and scent-tag extraction.
- NLP: language-specific processing (AraBERT for Arabic, transformer/textblob fallback for French/English).
- Geo processing & visualization: GeoJSON and uMap exports for interactive maps.
- Notebooks: exploratory work and reproducible experiments in [notebooks/](notebooks/).

See the documented project layout: [docs/project_structure.md](docs/project_structure.md).

## Reproducibility & dev environment
- Python deps: install from [requirements.txt](requirements.txt).
- Recommended: create a venv and pin package versions in the existing requirements file.

Quick setup:
```sh
# shell
python -m venv .venv
.venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

## Data layout (important files)
- Raw Data files: [data/raw/tunisia_sensory_full_20251202_204147.csv](data/raw/tunisia_sensory_full_20251202_204147.csv), [data/raw/tunisia_sensory_map_20251202_204147.geojson](data/raw/tunisia_sensory_map_20251202_204147.geojson)
- Processed sample: [data/tunisia_natural_comments_10000_20251201_194300.csv](data/tunisia_natural_comments_10000_20251201_194300.csv)
- Notebooks for generators/analysis: [notebooks/Comments_Generator_v0_4.ipynb](notebooks/Comments_Generator_v0_4.ipynb), [notebooks/Comments_Generator_v0_2 (3).ipynb](notebooks/Comments_Generator_v0_2%20(3).ipynb)

## Data pipeline (concise steps)
1. Ingest CSV/JSON into data/raw/.
2. Canonicalize timestamps, normalize Unicode, remove bots and exact duplicates.
3. Detect language and route to language-specific text pipeline.
4. Run scent-mention extractor (keyword + pattern matching + simple NER).
5. Compute sentiment: AraBERT finetune or transformer inference for Arabic; TextBlob/HuggingFace models for FR/EN.
6. Geospatial join: snap points to neighborhoods, aggregate sentiment hotspots.
7. Export GeoJSON and uMap HTML for visualization.

## Processing details (implementation notes)
- Language routing: prefer a compact fasttext or langdetect step to route heavy model inference.
- Arabic pipeline: normalization (remove tatweel, normalize Alef variants), tokenization with Farasa or HuggingFace tokenizer, then AraBERT inference.
- Sentiment score: store both continuous score and categorical label (pos/neu/neg); keep model version and seed in metadata.
- Provenance: every processed row should include original source filename, original_id, processed_at, model_version.

## Outputs & visualization
- GeoJSON exports for direct GIS workflows: [data/raw/tunisia_sensory_map_20251202_204147.geojson](data/raw/tunisia_sensory_map_20251202_204147.geojson)
- uMap/HTML for public maps (exports placed in /maps for distribution).
- Aggregation matrices: [data/raw/tunisia_sensory_matrix_20251202_204147.csv](data/raw/tunisia_sensory_matrix_20251202_204147.csv)

## Running experiments
- Use the notebooks in [notebooks/](notebooks/) for reproducible experiments and small-scale model runs.
- For production-style runs, wrap preprocessing and inference into CLI scripts (place under src/ per [docs/project_structure.md](docs/project_structure.md)).

## CI / Testing
- Add unit tests for tokenization, language routing and sentiment-normalization functions.
- Treat CSV fixtures as test inputs (small samples of [data/raw/...csv](data/raw/)).

## Contributing & License
- Follow code style and include tests for new parsing/model code.
- See license: [LICENSE/LICENSE](LICENSE/LICENSE).

## Quick links
- Kaggle Dataset Link: [Kaggle - The Scent of Tunisia](https://www.kaggle.com/datasets/ounikhouloud/tunisia-sensory-data) 
- Project structure: [docs/project_structure.md](docs/project_structure.md)
- Requirements: [requirements.txt](requirements.txt)
- Notebooks: [notebooks/Comments_Generator_v0_4.ipynb](notebooks/Comments_Generator_v0_4.ipynb)
- Raw data examples: [data/raw/tunisia_sensory_full_20251202_204147.csv](data/raw/tunisia_sensory_full_20251202_204147.csv), [data/raw/tunisia_sensory_map_20251202_204147.geojson](data/raw/tunisia_sensory_map_20251202_204147.geojson)
- Processed sample: [data/tunisia_natural_comments_10000_20251201_194300.csv](data/tunisia_natural_comments_10000_20251201_194300.csv)

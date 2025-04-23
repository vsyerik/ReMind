# ReMind

A Python toolkit for analyzing personal journal entries and extracting insights.

ReMind is a tool for analyzing journal entries and providing insights about your writing patterns, emotional tone, and recurring themes.

## Project Structure

The project consists of two main components:

1. **Journal Analysis**: Analyze journal entries for patterns, emotional tone, and recurring themes.
2. **Data Processing Scripts**: Utilities for cleaning and ingesting journal data from various sources.

## Installation

```bash
# Clone the repository
git clone https://github.com/vsyerik/ReMind.git
cd ReMind

# Install dependencies
pip install -r requirements.txt
```

## Features

- Analyzes journal entries from markdown files
- Identifies common words, tags, and questions
- Provides sentiment analysis of your entries
- Generates weekly summaries and insights
- Uses AI to provide deeper emotional insights

## Usage

To run the analysis on your journal entries:

```bash
python -m main
```

## Configuration

Edit the `config.yaml` file to customize:
- Custom stopwords for word analysis
- Journal directory path
- Analysis timeframe

## Components

### Data Processing Scripts

The `scripts` directory contains utilities for:
- Cleaning journal entries (removing YAML frontmatter, simplifying links, etc.)
- Ingesting data from various sources

## Testing

Run tests with any of the following methods:

```bash
# Method 1: Using unittest discover
python -m unittest discover

# Method 2: Using the run_tests.py script
python run_tests.py

# Method 3: Using setup.py
python setup.py test

# Method 4: Using pytest (requires pytest to be installed)
pip install pytest
pytest
```

The project includes configuration for both unittest and pytest testing frameworks.

## License

MIT

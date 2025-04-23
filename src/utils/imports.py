"""
NLTK resource initialization for ReMind Pulse.

This module ensures that the required NLTK resources are downloaded
before they are used in the application.
"""

import nltk
import os
from nltk.downloader import Downloader

# Check if resources are already downloaded before attempting to download them
downloader = Downloader()

# Download required NLTK resources if not already downloaded
if not downloader.is_installed('stopwords'):
    nltk.download('stopwords')
if not downloader.is_installed('punkt'):
    nltk.download('punkt')
if not downloader.is_installed('punkt_tab'):
    nltk.download('punkt_tab')

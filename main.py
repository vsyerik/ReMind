#!/usr/bin/env python3
"""
ReMind - A toolkit for analyzing personal journal entries.

This is the main entry point for the ReMind application.
"""

from src.pulse import main as pulse_main
from dotenv import load_dotenv

load_dotenv()

def main():
    """Run the ReMind Pulse application."""
    pulse_main()

if __name__ == '__main__':
    main()

# Text-Based Thumbnails Dataset Generation

## Overview

This repository focuses on the generation of text-based thumbnails using the Gemini Text-Based AI model. The process involves creating essays on various topics, including the topic itself, author information (name and email), and introductory and summary sections. The generated content is saved as Word documents with various font types. Thumbnails are then extracted using the Thumbcache Viewer tool.

## Dataset Generation

1. **text generation:**
   - Utilized the Gemini Text-Based AI model to create essays covering various topics.
   - Each essay includes the topic, author information, introduction, and summary.

2. **document saving:**
   - Implemented a Python script to save generated texts into Word documents.
   - Created 10 different font types, resulting in 1000 DOCX files per type.

3. **thumbnail extraction:**
   - Used the Thumbcache Viewer tool to extract thumbnails in Extra Large (256), Large (96), and Medium (48) icon views.

4. **mapping script:**
   - Developed a Python script to map extracted thumbnails back to their original file names.
   - Organized the dataset into folders based on thumbnail views (extra large, large, medium).

5. **train-test split:**
   - A Python script (`train_test_split.py`) is included for splitting the dataset into train and test sets using a custom method.

## Goal

The primary objective is to generate a text-based thumbnails dataset containing comprehensive essays. This dataset serves as a valuable resource for training AI models, specifically aimed at enhancing characters within thumbnails. Researchers and developers can leverage this dataset for image processing and character recognition applications.

## Usage

Explore, utilize, and contribute to this repository for research and educational purposes. If you have any questions or suggestions, please open an issue.

**Note:** Respect copyright and licensing restrictions when using and distributing the generated dataset.

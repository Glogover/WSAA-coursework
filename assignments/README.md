# Web Services & Applications – Assignments

This repository contains coursework assignments completed for the **Web Services & Applications** module.  
The assignments demonstrate the use of **Python**, **REST APIs**, **JSON data processing**, and **GitHub API integration**.

The work focuses on interacting with external web services, processing returned data, and automating tasks using Python scripts.

Repository:  
https://github.com/Glogover/WSAA-coursework

---

# Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Assignments](#assignments)
- [Installation](#installation)
- [Usage](#usage)
- [Security Note](#security-note)
- [Repository Structure](#repository-structure)
- [Author](#author)
- [License](#license)

---

# Overview

The purpose of this repository is to demonstrate practical use of **web services and APIs** in Python.

Across the assignments, the following concepts are explored:

- Making HTTP requests using Python
- Working with REST APIs
- Processing JSON data
- Using external data sources
- Automating updates to GitHub repositories via the GitHub API
- Basic data analysis and logic implementation

---

# Technologies Used

- Python 3
- Requests library
- JSON data handling
- GitHub REST API
- Deck of Cards API
- CSO Ireland API datasets

---

# Assignments

## Assignment 2 – Card Draw Simulation

File: `assignment2-carddraw.py`

This program simulates drawing **five cards from a shuffled deck** using the Deck of Cards API.

The program:

- Requests a shuffled deck from an external API
- Draws five cards
- Displays the cards drawn
- Checks for common poker combinations:
  - Pair
  - Triple
  - Flush
  - Straight

The program uses the `collections.Counter` class to analyse card values and suits.

---

## Assignment 3 – CSO Dataset Processing

File: `assignment03-cso.ipynb`  
Dataset: `cso.json`

This program retrieves the dataset for the "exchequer account (historical series)" from the **Central Statistics Office** (CSO), and stores it into a file called "cso.json".

---

## Assignment 4 – GitHub API Automation

Files:

- `assignment04-github.py`
- `assignment04-github.txt`

This program demonstrates how to interact with the **GitHub REST API** using Python by replacing "Andrew" with "Marcin" in assignment04-github.txt.

The script:

1. Connects to the GitHub API
2. Retrieves a file from the repository
3. Decodes the file from Base64
4. Searches for the text `"Andrew"`
5. Replaces it with `"Marcin"`
6. Updates the file in the repository with a new commit

The script authenticates using a GitHub API token stored in a configuration file.

Example text file used by the script:

```
Andrew found a strange key in the park one afternoon.
He wondered what door it might open.
After walking for a while, he noticed a tiny old box under a tree.
The key fit perfectly and the box slowly opened.
Inside was a note that said: “Congratulations, Andrew — you found the adventure.”
```

---

# Security Note

The repository **does not include the configuration file containing API keys**.

The script `assignment04-github.py` expects a local configuration file similar to:

```
config4.py
```

Example structure:

```python
apikeys = {
    "githubkey": "YOUR_GITHUB_TOKEN"
}
```

This file is intentionally excluded from the repository to protect sensitive credentials.

---

# Repository Structure

```
WSAA-coursework
│
├── assignment2-carddraw.py
├── assignment03-cso.ipynb
├── assignment04-github.py
├── assignment04-github.txt
├── cso.json
└── README.md
```

---

# Author

Marcin Kaminski

GitHub:  
https://github.com/Glogover

---

# License

This project is provided for **educational purposes** as part of coursework for the Web Services & Applications module at Atlantic Technological University (ATU).
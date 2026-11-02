# Data Redundancy Removal System

**A Python-based data validation and deduplication application using SHA-256 hashing, Flask, and SQLite.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.x-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite" alt="SQLite">
  <img src="https://img.shields.io/badge/Hashing-SHA--256-green" alt="SHA-256">
  <img src="https://img.shields.io/badge/Status-Development-orange" alt="Development">
</p>

## Project Overview

The **Data Redundancy Removal System** is a web-based application developed in Python to identify duplicate records, validate user input, and prevent redundant data from being stored in a database.

The system uses SHA-256 hashing to generate unique fingerprints for normalized records. Before inserting a new record, it checks whether an identical record already exists.

This project demonstrates practical implementation of data validation, hashing algorithms, database integration, and web application development.

## Key Features

- **Duplicate Detection:** Identifies previously stored records.
- **SHA-256 Hashing:** Generates unique fingerprints for normalized input data.
- **Data Validation:** Checks required fields and basic email formatting.
- **Data Normalization:** Handles case differences and unnecessary surrounding spaces.
- **Database Integration:** Stores unique records using SQLite.
- **Web Dashboard:** Provides a simple interface for submitting and viewing records.
- **Duplicate Prevention:** Uses a unique database constraint to prevent repeated hashes.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Web application framework |
| SQLite | Database management |
| SHA-256 | Duplicate fingerprint generation |
| HTML5 | Frontend structure |
| CSS3 | User interface styling |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
Data-Redundancy-System/
│
├── app.py                  # Flask application
├── database.py             # Database operations
├── deduplication.py        # Validation and duplicate detection
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Excluded files
│
├── database/
│   └── records.db          # Local SQLite database
│
├── templates/
│   └── index.html          # Web interface
│
└── static/
    └── style.css           # Application styling
```

## How It Works

The application follows a straightforward data processing workflow:

1. A user submits a name and email address.
2. The application validates the submitted information.
3. Input values are normalized to handle case and whitespace differences.
4. A SHA-256 hash is generated from the normalized data.
5. The database is checked for an existing matching hash.
6. If a duplicate is found, the application rejects the new record.
7. If the record is unique, it is inserted into the SQLite database.
8. The dashboard displays the stored records.

## Installation and Setup

### Prerequisites

- Python 3
- Kali Linux, Linux, macOS, or Windows
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/rashidabdullah5737-ai/Data-Redundancy-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Data-Redundancy-System
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

Linux / Kali Linux / macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python3 app.py
```

### 7. Open the Application

Visit the following address in your browser:

```text
http://127.0.0.1:5000
```

## Testing and Validation

The following scenarios have been manually tested:

| Test Case | Expected Result |
|---|---|
| Submit a valid new record | Record accepted |
| Submit the same record again | Duplicate rejected |
| Submit uppercase variations | Duplicate detected |
| Submit values with extra surrounding spaces | Duplicate detected |
| Submit an empty name | Validation error |
| Submit an invalid email format | Validation error |

## Database Design

The application uses an SQLite database with a `records` table.

| Field | Description |
|---|---|
| id | Unique record identifier |
| name | Submitted name |
| email | Submitted email |
| data_hash | SHA-256 fingerprint with a unique constraint |
| created_at | Record creation timestamp |

The unique constraint on `data_hash` provides an additional database-level safeguard against duplicate entries.

## Current Scope and Future Improvements

The current implementation is a local Flask and SQLite prototype.

Planned improvements include:

- Cloud database integration.
- CSV bulk data upload and processing.
- Advanced data validation.
- False-positive classification.
- Improved duplicate detection for similar records.
- User authentication and access control.
- Cloud deployment and scalability improvements.
- Automated unit and integration testing.

## Learning Outcomes

Through this project, I have gained practical experience with:

- Python application development.
- Flask web application development.
- SHA-256 hashing.
- Data validation and normalization.
- SQL and SQLite database operations.
- Duplicate record detection.
- Git and GitHub version control.

## Author

**Abdullah Rashid**

Cybersecurity Enthusiast | VAPT | Security Research | Python Development

- GitHub: [rashidabdullah5737-ai](https://github.com/rashidabdullah5737-ai)
- Project Repository: [Data-Redundancy-System](https://github.com/rashidabdullah5737-ai/Data-Redundancy-System)
- LinkedIn: [Abdullah Rashid](https://www.linkedin.com/in/abdullah-rashid-a1554b388/)

## Acknowledgement

Developed as part of my **CodeAlpha internship project**, focusing on practical Python development, data processing, and database management.

---

**Project Status:** Local prototype implemented. Cloud integration and advanced features are planned.



# Week 2 – Logistics Data Collection, Cleaning & Preprocessing

## Objective
This project demonstrates a complete logistics/supply-chain data preprocessing pipeline using Python.

## Reference Dataset
**DataCo Smart Supply Chain for Big Data**

The project simulates data collection, profiling, cleaning, missing-value handling, outlier detection, normalization, validation, and documentation.

## Technologies
- Python
- pandas
- NumPy
- scikit-learn
- Jupyter Notebook
- Matplotlib

## Preprocessing Steps
1. Data collection simulation
2. Dataset inspection
3. Column-name standardization
4. Duplicate detection/removal
5. Data-type correction
6. Missing-value analysis
7. Missing-value treatment
8. Categorical-data cleaning
9. IQR-based outlier detection
10. Outlier treatment
11. Feature scaling/standardization
12. Data validation

## Repository Structure
```text
week-2-logistics-data-preprocessing/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── reports/
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run
1. Download the authorized/public DataCo dataset.
2. Place `DataCoSupplyChainDataset.csv` in `data/raw/`.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run:
   `python src/preprocessing.py`
5. Or open the Jupyter notebook in `notebooks/`.

## Note
The raw source dataset is intentionally not bundled here. Download it from its authorized/public source and place it in `data/raw/`.

## Author
Aditya

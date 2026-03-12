# AMPidentifier

> A Python toolkit for Antimicrobial Peptide (AMP) prediction and physicochemical assessment

```
////////////////////////////////////////////////////////////////////////
//                                                                    //
//      _    __  __ ____  _     _            _   _  __ _              //
//     / \  |  \/  |  _ \(_) __| | ___ _ __ | |_(_)/ _(_) ___ _ __    //
//    / _ \ | |\/| | |_) | |/ _` |/ _ \ '_ \| __| | |_| |/ _ \ '__|   //
//   / ___ \| |  | |  __/| | (_| |  __/ | | | |_| |  _| |  __/ |      //
//  /_/   \_\_|  |_|_|   |_|\__,_|\___|_| |_|\__|_|_| |_|\___|_|      //
//                                                                    //
////////////////////////////////////////////////////////////////////////
```

---

## About

**AMPidentifier** is an open-source, modular Python toolkit for predicting Antimicrobial Peptides (AMPs) from amino acid sequences. It combines three pre-trained Machine Learning models (Random Forest, SVM, Gradient Boosting) with an ensemble voting system, and computes dozens of physicochemical descriptors via `modlamp`.

Users can run predictions with the built-in models, combine them in ensemble mode, or integrate external `.pkl` models for side-by-side comparison.

---

## Related Projects

| Project | Description | Link |
|---------|-------------|------|
| **AMPidentifier CLI** | Full command-line version with training scripts, benchmarking, and extended documentation | [github.com/madsondeluna/AMPidentifier](https://github.com/madsondeluna/AMPidentifier) |
| **AMPidentifier Web Server** | Browser-based interface for AMP prediction (no installation required) | [github.com/madsondeluna/AMPidentifierServerBETA](https://github.com/madsondeluna/AMPidentifierServerBETA) |

---

## Installation

```bash
pip install ampidentifier
```

We recommend using a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows
pip install ampidentifier
```

---

## Quick Start

```bash
# Single model (Random Forest, default)
ampidentifier --input my_sequences.fasta --output_dir ./results

# Ensemble voting (recommended)
ampidentifier --input my_sequences.fasta --output_dir ./results --ensemble

# Compare SVM with an external model
ampidentifier --input my_sequences.fasta --output_dir ./results --model svm --external_models /path/to/my_model.pkl
```

---

## Arguments

| Argument                | Description                                                                  | Required | Default |
|-------------------------|------------------------------------------------------------------------------|:--------:|:-------:|
| `-i, --input`           | Path to the input FASTA file                                                 | Yes      | -       |
| `-o, --output_dir`      | Path to the output directory                                                 | Yes      | -       |
| `-m, --model`           | Internal model to use: `rf`, `svm`, `gb`                                     | No       | `rf`    |
| `--ensemble`            | Enable majority-vote ensemble across all internal models                     | No       | Flag    |
| `-e, --external_models` | One or more paths to external `.pkl` models for comparison (comma-separated) | No       | -       |

---

## Key Features

- **Three pre-trained ML models:** Random Forest, Gradient Boosting, SVM
- **Ensemble voting:** Majority vote across all models for improved robustness
- **External model support:** Load custom `.pkl` models for comparison
- **Physicochemical descriptors:** Compute and export an extensive set of sequence features via `modlamp`
- **Fully open-source and modular:** Each component can be used independently

---

## Pre-Trained Model Performance

Best values per metric in **bold**.

| Metric      | Random Forest (RF) | SVM    | Gradient Boosting (GB) |
|-------------|-------------------:|-------:|-----------------------:|
| Accuracy    | **0.8845**         | 0.8740 | 0.8585                 |
| Precision   | **0.8910**         | 0.8880 | 0.8665                 |
| Recall      | **0.8762**         | 0.8558 | 0.8475                 |
| F1-Score    | **0.8836**         | 0.8716 | 0.8569                 |
| MCC         | **0.7692**         | 0.7484 | 0.7172                 |
| AUC-ROC     | **0.9503**         | 0.9356 | 0.9289                 |

**Recommended:** use `--ensemble` for most robust predictions (Accuracy: 87.47%, Sensitivity: 85.96%, Specificity: 88.98%).

---

## Outputs

| File | Description |
|------|-------------|
| `physicochemical_features.csv` | Computed physicochemical descriptors for each input sequence |
| `prediction_comparison_report.csv` | AMP/non-AMP predictions with confidence scores per model and consensus |

---

## Project Structure

```text
amp_identifier/
├── __init__.py
├── core.py               # Main prediction workflow
├── data_io.py            # FASTA input reader
├── feature_extraction.py # Physicochemical descriptor computation
├── prediction.py         # Model loading and inference
└── reporting.py          # CSV report generation
```

---

## Contributors

| Name | Role | Affiliation |
|------|------|-------------|
| Madson A. de Luna-Aragão, MSc | Lead developer; architecture; ML; docs | UFMG |
| Rafael L. da Silva, BSc | Collaborator; preprocessing; pipeline testing | UFPE |
| Ana M. Benko-Iseppon, PhD | Advisor; study design; biological validation | UFPE |
| João Pacífico, PhD | Co-Advisor; computational review; evaluation | UPE |
| Carlos A. dos Santos-Silva, PhD | Co-Advisor; pipeline testing; review | CESMAC |

---

## Funding & Acknowledgments

- Officially registered under **UFPE** - Universidade Federal de Pernambuco, Brazil
- Supported by **FACEPE** - Fundação de Amparo à Pesquisa do Estado de Pernambuco
- **INPI Registration:** BR 51 2025 005859-4

---

## How to Cite

```text
Luna-Aragão, M. A., da Silva, R. L., Pacífico, J., Santos-Silva, C. A. & Benko-Iseppon, A. M.
(2025). AMPidentifier: A Python toolkit for predicting antimicrobial peptides using ensemble
machine learning and physicochemical descriptors.
https://github.com/madsondeluna/AMPidentifier
```

---

## License

This project is licensed under the terms specified in the repository. All rights reserved.
© Madson A. de Luna Aragão et al., 2025.

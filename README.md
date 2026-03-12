# AMPidentifier

> A Python toolkit for Antimicrobial Peptide (AMP) prediction and physicochemical assessment

[![PyPI version](https://img.shields.io/pypi/v/ampidentifier.svg)](https://pypi.org/project/ampidentifier/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org)
[![NumPy](https://img.shields.io/badge/NumPy-array-blue?logo=numpy)](https://numpy.org)
[![Pandas](https://img.shields.io/badge/Pandas-dataframes-150458?logo=pandas)](https://pandas.pydata.org)
[![Biopython](https://img.shields.io/badge/Biopython-sequences-green)](https://biopython.org)
[![modlAMP](https://img.shields.io/badge/modlAMP-descriptors-purple)](https://modlamp.org)

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

## About

**AMPidentifier** is an open-source, modular Python toolkit for predicting Antimicrobial Peptides (AMPs) from amino acid sequences. It combines three pre-trained Machine Learning models (Random Forest, SVM, Gradient Boosting) with an ensemble voting system, and computes dozens of physicochemical descriptors via `modlamp`.

Users can run predictions with the built-in models, combine them in ensemble mode, or integrate external `.pkl` models for side-by-side comparison.

AMPidentifier is officially published on the Python Package Index (PyPI) at https://pypi.org/project/ampidentifier/ and can be installed directly via `pip install ampidentifier`. PyPI publication ensures that every release is versioned, indexed, and permanently accessible, which is essential for reproducibility in scientific workflows: researchers can cite a specific version and reproduce results exactly, regardless of when or where the analysis is run.

## Related Projects

| Project | Description | Link |
|---------|-------------|------|
| **AMPidentifier CLI** | Full command-line version with training scripts, benchmarking, and extended documentation | [github.com/madsondeluna/AMPidentifier](https://github.com/madsondeluna/AMPidentifier) |
| **AMPidentifier Web Server** | Browser-based interface for AMP prediction (no installation required) | [github.com/madsondeluna/AMPidentifierServerBETA](https://github.com/madsondeluna/AMPidentifierServerBETA) |

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

> Available on PyPI: https://pypi.org/project/ampidentifier/

## Quick Start

```bash
# Single model (Random Forest, default)
ampidentifier --input my_sequences.fasta --output_dir ./results

# Ensemble voting (recommended)
ampidentifier --input my_sequences.fasta --output_dir ./results --ensemble

# Compare SVM with an external model
ampidentifier --input my_sequences.fasta --output_dir ./results --model svm --external_models /path/to/my_model.pkl
```

## Usage Examples

The examples below use this sample FASTA file (`test_peptides.fasta`) containing known AMPs and non-AMP peptides for demonstration:

```
>Magainin-2|Xenopus_laevis|Cationic_amphipathic_helix
GIGKFLHSAKKFGKAFVGEIMNS
>LL-37|Homo_sapiens|Cathelicidin_family
LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES
>Melittin|Apis_mellifera|Venom_peptide
GIGAVLKVLTTGLPALISWIKRKRQQ
>Insulin_Chain_B|Homo_sapiens|Peptide_hormone
FVNQHLCGSHLVEALYLVCGERGFFYTPKT
>Glucagon|Homo_sapiens|Peptide_hormone
HSQGTFTSDYSKYLDSRRAQDFVQWLMNT
>Vasoactive_intestinal_peptide|Homo_sapiens|Neuropeptide
HSDAVFTDNYTRLRKQMAVKKYLNSILN
```

### Usage Example - Google Colab / Jupyter Notebook

Click the badge to open the demo notebook directly in Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1W5uMh5GXGXnu8I9rvGH4cUAU31tUJ15Q?usp=sharing)

Or run the cells below manually in any Colab notebook:

```python
# Cell 1: Install
!pip install ampidentifier
```

```python
# Cell 2: Create the example FASTA file
fasta_content = """>Magainin-2|Xenopus_laevis|Cationic_amphipathic_helix
GIGKFLHSAKKFGKAFVGEIMNS
>LL-37|Homo_sapiens|Cathelicidin_family
LLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES
>Melittin|Apis_mellifera|Venom_peptide
GIGAVLKVLTTGLPALISWIKRKRQQ
>Insulin_Chain_B|Homo_sapiens|Peptide_hormone
FVNQHLCGSHLVEALYLVCGERGFFYTPKT
>Glucagon|Homo_sapiens|Peptide_hormone
HSQGTFTSDYSKYLDSRRAQDFVQWLMNT
>Vasoactive_intestinal_peptide|Homo_sapiens|Neuropeptide
HSDAVFTDNYTRLRKQMAVKKYLNSILN
"""

with open("test_peptides.fasta", "w") as f:
    f.write(fasta_content)

print("FASTA file created with 6 sequences (3 known AMPs + 3 non-AMPs)")
```

```python
# Cell 3: Run with default model (Random Forest)
# Import the pipeline function directly from the package
import os
from amp_identifier.core import run_prediction_pipeline

os.makedirs("./results_rf", exist_ok=True)

run_prediction_pipeline(
    input_file="test_peptides.fasta",
    output_dir="./results_rf",
    internal_model_type="rf",   # Random Forest: best single-model AUC-ROC (0.9503)
    use_ensemble=False,
    external_model_paths=[],
)
```

```python
# Cell 4: Run with ensemble mode (recommended)
# Combines RF + SVM + GB via majority voting for maximum robustness
import os
from amp_identifier.core import run_prediction_pipeline

os.makedirs("./results_ensemble", exist_ok=True)

run_prediction_pipeline(
    input_file="test_peptides.fasta",
    output_dir="./results_ensemble",
    internal_model_type="rf",   # ignored when use_ensemble=True
    use_ensemble=True,          # activates majority vote across all three models
    external_model_paths=[],
)
```

```python
# Cell 5: Inspect results
# Runs ensemble first if output does not exist yet, then displays results
import os
import pandas as pd
from amp_identifier.core import run_prediction_pipeline

report_path   = "./results_ensemble/prediction_comparison_report.csv"
features_path = "./results_ensemble/physicochemical_features.csv"

if not os.path.exists(report_path):
    os.makedirs("./results_ensemble", exist_ok=True)
    run_prediction_pipeline(
        input_file="test_peptides.fasta",
        output_dir="./results_ensemble",
        internal_model_type="rf",
        use_ensemble=True,
        external_model_paths=[],
    )

report = pd.read_csv(report_path)
print("=== Ensemble Prediction Report ===")
print(report.to_string(index=False))

features = pd.read_csv(features_path)
print(f"\n=== Physicochemical Features ===")
print(f"Shape: {features.shape[0]} sequences x {features.shape[1]} descriptors")
print(features[['ID', 'Length', 'Charge', 'HydrophRatio']].to_string(index=False))
```

```python
# Cell 6: Compare all three internal models individually
import os
import pandas as pd
from amp_identifier.core import run_prediction_pipeline

for model in ["rf", "svm", "gb"]:
    os.makedirs(f"./results_{model}", exist_ok=True)

    run_prediction_pipeline(
        input_file="test_peptides.fasta",
        output_dir=f"./results_{model}",
        internal_model_type=model,
        use_ensemble=False,
        external_model_paths=[],
    )

    report = pd.read_csv(f"./results_{model}/prediction_comparison_report.csv")
    pred_col = [c for c in report.columns if c.startswith("pred_")][0]
    amp_count = int(report[pred_col].sum())
    print(f"[{model.upper()}] Predicted AMPs: {amp_count}/6")
```

## Arguments

| Argument                | Description                                                                  | Required | Default |
|-------------------------|------------------------------------------------------------------------------|:--------:|:-------:|
| `-i, --input`           | Path to the input FASTA file                                                 | Yes      | none    |
| `-o, --output_dir`      | Path to the output directory                                                 | Yes      | none    |
| `-m, --model`           | Internal model to use: `rf`, `svm`, `gb`                                     | No       | `rf`    |
| `--ensemble`            | Enable majority-vote ensemble across all internal models                     | No       | Flag    |
| `-e, --external_models` | One or more paths to external `.pkl` models for comparison (comma-separated) | No       | none    |

## Key Features

- **Three pre-trained ML models:** Random Forest, Gradient Boosting, SVM
- **Ensemble voting:** Majority vote across all models for improved robustness
- **External model support:** Load custom `.pkl` models for comparison
- **Physicochemical descriptors:** Compute and export an extensive set of sequence features via `modlamp`
- **Fully open-source and modular:** Each component can be used independently

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

## Outputs

| File | Description |
|------|-------------|
| `physicochemical_features.csv` | Computed physicochemical descriptors for each input sequence |
| `prediction_comparison_report.csv` | AMP/non-AMP predictions with confidence scores per model and consensus |

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

## Contributors

| Name | Role | Affiliation |
|------|------|-------------|
| Madson A. de Luna-Aragão, MSc | Lead developer; architecture; ML; docs | UFMG |
| Rafael L. da Silva, BSc | Collaborator; preprocessing; pipeline testing | UFPE |
| Ana M. Benko-Iseppon, PhD | Advisor; study design; biological validation | UFPE |
| João Pacífico, PhD | Co-Advisor; computational review; evaluation | UPE |
| Carlos A. dos Santos-Silva, PhD | Co-Advisor; pipeline testing; review | CESMAC |

## Funding & Acknowledgments

- Officially registered under **UFPE** - Universidade Federal de Pernambuco, Brazil
- Supported by **FACEPE** - Fundação de Amparo à Pesquisa do Estado de Pernambuco
- **INPI Registration:** BR 51 2025 005859-4

## How to Cite

```text
Luna-Aragão, M. A., da Silva, R. L., Pacífico, J., Santos-Silva, C. A. & Benko-Iseppon, A. M.
(2025). AMPidentifier: A Python toolkit for predicting antimicrobial peptides using ensemble
machine learning and physicochemical descriptors.
https://github.com/madsondeluna/AMPidentifier
```

## License

This project is licensed under the terms specified in the repository. All rights reserved.
© Madson A. de Luna Aragão et al., 2025.

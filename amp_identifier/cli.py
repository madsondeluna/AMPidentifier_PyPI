# amp_identifier/cli.py
# Entry point for the 'ampidentifier' command installed via pip.

import argparse
import os
from amp_identifier.core import run_prediction_pipeline

BANNER = r"""

////////////////////////////////////////////////////////////////////////
//                                                                    //
//      _    __  __ ____  _     _            _   _  __ _              //
//     / \  |  \/  |  _ \(_) __| | ___ _ __ | |_(_)/ _(_) ___ _ __    //
//    / _ \ | |\/| | |_) | |/ _` |/ _ \ '_ \| __| | |_| |/ _ \ '__|   //
//   / ___ \| |  | |  __/| | (_| |  __/ | | | |_| |  _| |  __/ |      //
//  /_/   \_\_|  |_|_|   |_|\__,_|\___|_| |_|\__|_|_| |_|\___|_|      //
//                                                                    //
////////////////////////////////////////////////////////////////////////

"""


def main():
    print(BANNER)

    parser = argparse.ArgumentParser(
        description="AMPidentifier: Antimicrobial Peptide prediction and analysis.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-i", "--input", required=True, type=str,
                        help="Path to the input FASTA file.")
    parser.add_argument("-o", "--output_dir", required=True, type=str,
                        help="Directory where result files will be saved.")
    parser.add_argument("-m", "--model", type=str, default="rf",
                        choices=["rf", "svm", "gb"],
                        help="Internal model to use (default: rf).")
    parser.add_argument("--ensemble", action="store_true",
                        help="Use all internal models with majority voting.")
    parser.add_argument("-e", "--external_models", nargs="*", type=str, default=[],
                        help="Paths to external .pkl models for comparison.")

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        print(f"Created output directory: {args.output_dir}")

    run_prediction_pipeline(
        input_file=args.input,
        output_dir=args.output_dir,
        internal_model_type=args.model,
        use_ensemble=args.ensemble,
        external_model_paths=args.external_models,
    )


if __name__ == "__main__":
    main()

import xarray as xr
import pandas as pd


def cdf_to_csv(cdf_file, csv_file):
    """
    Converts a CDF file to a CSV file.

    Args:
        cdf_file (str): The path to the input CDF file.
        csv_file (str): The path to the output CSV file.
    """
    cdf_file = ACESII_36364_l3_MPI_ENU (1)
    try:
        # Open the CDF file using xarray
        ds = xr.open_dataset(cdf_file)

        # Convert to a pandas DataFrame
        df = ds.to_dataframe()

        # Write the DataFrame to a CSV file
        df.to_csv(csv_file)

        print(f"Successfully converted {cdf_file} to {csv_file}")

    except Exception as e:
        print(f"Error during conversion: {e}")

# Example usage:
# cdf_to_csv("input.cdf", "output.csv")
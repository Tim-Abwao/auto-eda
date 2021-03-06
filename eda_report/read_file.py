from pathlib import Path

import pandas as pd

from eda_report.exceptions import InputError


def df_from_file(filename):
    """Reads a *csv* or *excel* file, and loads its contents as a
    :class:`pandas.DataFrame`.

    This is basically a wrapper around the
    :func:`pandas.read_csv` and :func:`pandas.read_excel` methods
    respectively.

    :param filename: A file name, or the path to a file.
    :type filename: str
    :raises InputError: If the input file is not a valid csv or excel file.
    :return: A pandas ``DataFrame`` with the file's contents.
    :rtype: :class:`pandas.DataFrame`
    """
    file = Path(filename)

    if file.suffix == ".csv":
        return pd.read_csv(file)
    elif file.suffix == ".xlsx":
        return pd.read_excel(file, engine="openpyxl")
    else:
        raise InputError(f"Invalid input file: {filename}")

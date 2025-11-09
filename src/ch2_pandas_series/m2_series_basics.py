"""Pandas Series Basics"""

import pandas as pd
import common_utils as util

# ##############################################################################
# Pandas Series Basics
# ##############################################################################
# 1. Series can be created from lists, NumPy arrays, dictionaries, and
#    scalar values
# 2. Series have a variety of attributes and methods that can be used to
#    manipulate and analyze the data
# 3. Series can be indexed and sliced like NumPy arrays
# 4. Series support vectorized operations and broadcasting
# 5. Series can handle missing data using NaN values
# ##############################################################################
# Pandas Datatypes
# ##############################################################################
# 01. int64               64-bit integer                same as NumPy int64
# 02. float64             64-bit floating point         same as NumPy float64
# 03. bool                Boolean (True/False)          same as NumPy bool
# 04. boolean             Nullable Boolean              allows NaN values
# 05. Int64               Nullable integer              allows NaN values
# 06. Float64             Nullable floating point       allows NaN values
# ##############################################################################
# 07. object              Python object                 same as NumPy object
# 08. string              String (new in Pandas 1.0)    allows NaN values
# 09. category            Categorical variable          similar to R factors
# ##############################################################################
# 10. datetime64[ns]      Date and time                 same as NumPy datetime64
# 11. timedelta[ns]       Difference between datetimes  same as NumPy timedelta64
# 12. period[M]           Period (new in Pandas 1.1)    same as NumPy period[M]
# ##############################################################################

students = pd.Series([None, "Bob", "Charlie"], name="Students", dtype="string")
cgpa = pd.Series([8.6, None, 9.4], name="CGPA", dtype="Float64")
ages = pd.Series([20, 21, None], name="Ages", dtype="Int64")

util.print_delimiter()
print(f"{util.cy_colored('STUDENTS SERIES')}        : \n{students}")
print(f"{util.cy_colored('STUDENTS SERIES DTYPE')}  : {students.dtype}")
print(f"{util.cy_colored('STUDENTS SERIES INDEX')}  : {students.index}")
print(f"{util.cy_colored('STUDENTS SERIES VALUES')} : {students.values}")

util.print_delimiter()
print(f"{util.mg_colored('CGPA SERIES')}            : \n{cgpa}")
print(f"{util.mg_colored('CGPA SERIES DTYPE')}      : {cgpa.dtype}")
print(f"{util.mg_colored('CGPA SERIES INDEX')}      : {cgpa.index}")
print(f"{util.mg_colored('CGPA SERIES VALUES')}     : {cgpa.values}")

util.print_delimiter()
print(f"{util.ye_colored('AGES SERIES')}            : \n{ages}")
print(f"{util.ye_colored('AGES SERIES DTYPE')}      : {ages.dtype}")
print(f"{util.ye_colored('AGES SERIES INDEX')}      : {ages.index}")
print(f"{util.ye_colored('AGES SERIES VALUES')}     : {ages.values}")

util.print_delimiter()
cgpa_as_int = cgpa.astype("Int64")
print(f"{util.gr_colored('CGPA SERIES AS INT64')}   : \n{cgpa_as_int}")

util.print_delimiter()
cgpa_as_string = cgpa.astype("string")
print(f"{util.bu_colored('CGPA SERIES AS STRING')}  : \n{cgpa_as_string}")

util.print_delimiter()

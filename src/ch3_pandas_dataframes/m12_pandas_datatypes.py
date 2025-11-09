"""Pandas DataTypes"""

# ##############################################################################
# Pandas DataTypes
# ##############################################################################
# S.No       Category            DataType         Description         Bit Size
# ##############################################################################
# 1          Numeric             int8/Int8        Integer             8 bits
# 2          Numeric             int16/Int16      Integer             16 bits
# 3          Numeric             int32/Int32      Integer             32 bits
# 4          Numeric             int64/Int64      Integer             64 bits
# 5          Numeric             float16/Float16  Floating Point      16 bits
# 6          Numeric             float32/Float32  Floating Point      32 bits
# 7          Numeric             float64/Float64  Floating Point      64 bits
# 8          Boolean             bool/Boolean     Boolean             1 bit
# 9          Categorical         category         Categorical Data    N/A
# 10         Text/String         object           Text/String         N/A
# 11         Text/String         string           Text/String         N/A
# 12         Timeseries          datetime64       Date and Time       N/A
# 13         Timeseries          timedelta64      Difference in Time  N/A
# 14         Timeseries          period           Period Data         N/A
# ##############################################################################
# Note:
#   - int8/Int8, int8 is numPy datatype while Int8 is Pandas nullable datatype.
#   - For more details, refer to the official Pandas documentation on data types
#     https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#dtypes
# ###############################################################################

# ##############################################################################
# DataFrame Memory Optimization with Appropriate DataTypes
# ##############################################################################
# 1. Drop Unnecessary Columns (when possible, avoid reading them in at all)
# 2. Convert object types to numeric, or datetime types when possible
# 3. Downcast numeric types to smaller types when possible
# 4. Use nullable types (e.g., Int8, String) when dealing with missing data
# 5. Use appropriate datetime types for date and time data
# 6. Use categorical types for columns with a limited number of unique values
# ##############################################################################

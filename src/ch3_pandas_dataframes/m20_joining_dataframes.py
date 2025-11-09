"""Joining DataFrames in Pandas"""

import pandas as pd

# Read Products DataFrame
raw_products = pd.read_csv(r"D:\Python\numpy-pandas-practice\data\input\groceries\products.csv")
raw_products["ModifyDate"] = pd.to_datetime(raw_products["ModifyDate"])
products_1 = raw_products.head(226)
products_2 = raw_products.tail(226)

# Read Categories DataFrame
categories = pd.read_csv(r"D:\Python\numpy-pandas-practice\data\input\groceries\categories.csv")
print("Categories DataFrame:")
print(categories.head())

# ##############################################################################
# Appending/Combining DataFrames Using concat Method
# ##############################################################################
# 1. The concat() function in Pandas is used to concatenate or append DataFrames
#    along a particular axis (rows or columns).
# 2. In this example, we will concatenate two DataFrames (products_1 and products_2)
#    along the rows (axis=0) to create a single DataFrame containing all products
#    from both DataFrames.
# 3. The ignore_index=True parameter is used to reset the index in the resulting
#    DataFrame, so that it has a continuous index starting from 0.
# 4. If the structures of the DataFrames being concatenated are different (e.g.,
#    different columns), Pandas will fill in missing values with NaN.
# ##############################################################################
products = pd.concat([products_1, products_2], ignore_index=True)
print("\nCombined Products DataFrame:")
print(products.head())

# ##############################################################################
# Joining categories DataFrames Using merge Method
# ##############################################################################
# 1. The merge() function in Pandas is used to join two DataFrames based on a common
#    column or index.
# 2. In this example, we will merge the products DataFrame with the categories DataFrame
#    based on the "CategoryID" column, which is common to both DataFrames.
# 3. The how="inner" parameter specifies that we want to perform an inner join,
#    which means that only the rows with matching values in both DataFrames will be
#    included in the resulting DataFrame.
#    a. The resulting DataFrame will contain all columns from both DataFrames, with
#       the rows matched based on the "CategoryID" column.
#    b. If there are any columns with the same name in both DataFrames (other than
#       the join key), Pandas will add suffixes to distinguish them.
# 4. The how="left" parameter specifies that we want to perform a left join,
#    which means that all rows from the left DataFrame (products) will be included
#    in the resulting DataFrame, along with matching rows from the right DataFrame
#    (categories). If there is no match, NaN values will be filled in for the columns
#    from the right DataFrame.
# 5. The how="right" parameter specifies that we want to perform a right join,
#    which means that all rows from the right DataFrame (categories) will be included
#    in the resulting DataFrame, along with matching rows from the left DataFrame
#    (products). If there is no match, NaN values will be filled in for the columns
#    from the left DataFrame.
# 6. The how="outer" parameter specifies that we want to perform a full outer join,
#    which means that all rows from both DataFrames will be included in the resulting
#    DataFrame. If there is no match, NaN values will be filled in for the columns from
#    the DataFrame that does not have a matching row.
# ##############################################################################
print("\nProducts DataFrame Structure:")
print(products.info())

print("\nCategories DataFrame Structure:")
print(categories.info())

groceries = products.merge(categories, how="inner", on="CategoryID")
print("\nGroceries DataFrame (Created by Inner Join on Products & Categories Dataframes):")
print(groceries.head())

print("\nGroceries DataFrame Structure (After Inner Join):")
print(groceries.info())

# ##############################################################################
# Joining categories DataFrames Using join Method Based on Index
# ##############################################################################
students = pd.DataFrame(
    {
        "StudentID": [2, 3, 4],
        "Name": ["Bob", "Charlie", "David"],
        "Comments": ["Science", "Sports", "Arts"],
    }
)
students.set_index("StudentID", inplace=True)

marks = pd.DataFrame(
    {
        "StudentID": [1, 2, 3],
        "Marks": [85, 98, 68],
        "Comments": ["Good", "Excellent", "Average"],
    }
)
marks.set_index("StudentID", inplace=True)

joined_student_marks = students.join(marks, how="inner", rsuffix="2")
print("\nStudent Marks DataFrame (Created by Joining Students & Marks Dataframes on Index):")
print(joined_student_marks)

# This can also be achieved using merge method
merged_student_marks = students.merge(
    marks, how="inner", left_index=True, right_index=True, suffixes=("1", "2")
)
print("\nStudent Marks DataFrame (Created by Merging Students & Marks Dataframes on Index):")
print(merged_student_marks)

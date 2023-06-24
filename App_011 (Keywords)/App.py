# Python Keywords are in "keyword" package.
# Keywords can't be assigned to variables.
# First import the package:

import keyword

# Then get keyword list and assign this list to a variable.
python_keywords = keyword.kwlist

# Print keywords
print(python_keywords)

# To check for keywords you can use: keyword.iskeyword()
# Example:

keyword.iskeyword('global')

keyword.iskeyword("python")
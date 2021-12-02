from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
a = "Aptio Setup Utility - Copyright (C) 2016 American Megatrends, Inc. \nRestore Defaults\n "
x = 'Restore User Defaults'


Partial_Ratio = fuzz.partial_ratio(a.lower(),x.lower())
print(Partial_Ratio)






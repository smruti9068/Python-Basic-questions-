'''Adictionary which maps country names to Internet top-level domains (TLDs) is given as follows:
 tlds = {‘Canada’: ‘ca’, ‘United States’: ‘us’, ‘Mexico’: ‘mx’}
 Perform the following tasks and display the results:
 a) Check whether the dictionary contains the key ‘Canada’.
 b) Check whether the dictionary contains the key ‘France’.
 c) Iterate through the key-value pairs and display them in a two-column format.
 d) Add the key–value pair ‘Sweden’ and ‘sw’ (incorrect TLD).
 e) Update the value for the key ‘Sweden’ to ‘se’ (correct TLD).
 f) Use dictionary comprehension to reverse the keys and values.'''
tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
# a) Check for 'Canada'
print('Canada' in tlds)
# b) Check for 'France'
print('France' in tlds)
# c) Display key-value pairs
for country, tld in tlds.items():
    print(f"{country:15} {tld}") # country string to occupy 15 character spaces
# d) Add incorrect TLD for Sweden
tlds['Sweden'] = 'sw'
# e) Correct the TLD for Sweden
tlds['Sweden'] = 'se'
# f) Reverse keys and values
reversed_tlds = {v: k for k, v in tlds.items()}
print(reversed_tlds)

#  Dictionaries are dynamic (they can grow or shrink) and mutable (you can modify their contents). great for situations where you need to look up values based on specific keys
# Some useful methods for dictionaries include:
# d.get(key, default): Returns the value associated with the key (or the default value if the key is not found).
# d.items(): Returns a list of key-value pairs.
# d.keys(): Returns a list of keys.
# d.values(): Returns a list of values.
# d.pop(key): Removes the key-value pair and returns the value.
# d.update(other_dict): Updates the dictionary with key-value pairs from another dictionary.
# 

MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

print(MLB_team['Boston'])  # Output: 'Red Sox'
print(MLB_team.items())
print(MLB_team.keys())
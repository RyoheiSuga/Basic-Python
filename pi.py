text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

list = list(map(len, text.replace(",","").replace(".","").split()))
list_a = ''.join(map(str, list))
print(list_a)
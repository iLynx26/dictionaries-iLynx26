# According to the specifications, we need to create and print a dictionary.
# Let's create the dictionary with the provided market shares and print its contents.

# Creating the dictionary with search engine market shares
search_engines_market_share = {
    "Yahoo!": 2.09,
    "Google": 90.15,
    "Bing": 3.23,
    "Baidu": 2.2
}

# Printing the elements of the dictionary as specified
for search_engine, market_share in search_engines_market_share.items():
    print(f"{search_engine}: {market_share}")

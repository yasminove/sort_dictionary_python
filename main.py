stocks = {
  'GOOG': 234.43,
  'FB': 132.54,
  'AAPL': 543.21,
  'YAHOO': 23.34
}

# get the minimum value

print(min(zip(stocks.values(), stocks.keys())))

# get the maximum value

print(max(zip(stocks.values(), stocks.keys())))

# sort the dictionary prices

print(sorted(zip(stocks.values(), stocks.keys())))


# sort the dictionary keys alphabatically

print(sorted(zip(stocks.keys(), stocks.values())))

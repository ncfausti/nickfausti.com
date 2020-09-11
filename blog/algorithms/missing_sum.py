def find_missing(input):
  n = len(input)
  
  return (((n+1) * (n+2)) / 2) - sum(input)

# Gauss sum formula

assert sum([1,2,3,4,5]) == (5*6) / 2

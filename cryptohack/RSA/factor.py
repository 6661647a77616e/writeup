from primefac import primefac

# The number to factorize
n = 510143758735509025530880200653196460532653147

# Factorize the number
factors = list(primefac(n))

# Sort the factors (to ensure we get the smaller one first)
factors.sort()

# Print the smaller factor
print(f"The smaller prime factor is: {factors[0]}")
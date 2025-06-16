from math import comb


red = 2
green = 3
blue = 2

total = red + green + blue


none_blue = comb(red + green, 2)


total_ways = comb(total, 2)


probability =none_blue / total_ways


print(f"The probability that none of the balls drawn is blue is: {probability:.2f}")


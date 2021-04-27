def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count +=1
    return count
# Author = TECH_IN_SECONDS

text = input("Enter a string = ").lower()

for char in "abcdefghijklmnopqrstuvwxyz":
    percent = 100 * count_char(text, char)/len(text)
    print(f"{char} -> {round(percent,2)}%")



# Enter a string = Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under the GNU General Public License (GPL). This tutorial gives enough understanding on Python programming language.

# a -> 6.13%
# b -> 1.23%
# c -> 2.15%
# d -> 3.07%
# e -> 9.51%
# f -> 0.0%
# g -> 5.52%
# h -> 2.45%
# i -> 6.13%
# j -> 0.31%
# k -> 0.31%
# l -> 4.6%
# m -> 1.53%
# n -> 7.06%
# o -> 4.91%
# p -> 3.37%
# q -> 0.0%
# r -> 5.83%
# s -> 3.68%
# t -> 4.91%
# u -> 3.99%
# v -> 1.53%
# w -> 0.31%
# x -> 0.0%
# y -> 1.23%
# z -> 0.0%
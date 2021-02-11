string = "abcdef"
string_2 = "ghijkl"

print(string.translate(string.maketrans(string, string_2)))


from string import ascii_letters
a = ascii_letters
print(a)

s = "Hello"
print(s.center(11))

food = {"korean":"bbq", "italian":"pizza"}
print(food.get("korean", "world"))

print(round(5.4))
print(round(5.5))

print(list(enumerate(string)))
print(list(enumerate(list(enumerate(string)))))

print(list(map(chr,range(100,150))))

print(list(map(ord,ascii_letters)))

nums = [1,-2,-4,-6,5]
for i in map(abs,nums):
    print(f'Positive number:{i}')
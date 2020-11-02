
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Aa', 'Bb', 'Cc', 'Oo', 'Tt']
print(friends)

friends.append("Cr")
print(friends)

# adding the item to list with specific index
friends.insert(1, "Kl")
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.remove("Tt")
print(friends)
friends.pop()  # remove the last item of the list
print(friends)
friends.clear()  # removing all the item from the list
print(friends)

friends = ['Aa', 'Bb', 'Cc', 'Oo', 'Tt', 'Aa']
print(friends.index('Cc'))  # find the index of item

print(friends.count('Aa'))

friends.sort()  # sort the item in ascending order
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()  # sort the item in reverse
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

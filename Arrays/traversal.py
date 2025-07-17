arr = [10, 20, 30, 40, 50]

# -----------------------------
# 1. Traversal using for loop
# -----------------------------
print("Traversal using for loop:")
for i in range(len(arr)):
    print(arr[i], end=' ')
print()  # newline

# -----------------------------
# 2. Traversal using while loop
# -----------------------------
print("Traversal using while loop:")
i = 0
while i < len(arr):
    print(arr[i], end=' ')
    i += 1
print()

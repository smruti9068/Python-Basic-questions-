''' Given the sets {10, 20, 30} and {5, 10, 15, 20}, use the mathematical set operators to produce the
 following sets:
 a) {30},
 b) {5, 15, 30}
 c) {5, 10, 15, 20, 30}
 d) {10, 20}00'''
set1 = {10, 20, 30}
set2 = {5, 10, 15, 20}

print(set1 - set2)  # a) {30}
print(set1 ^ set2)  # b) {5, 15, 30}
print(set1 | set2)  # c) {5, 10, 15, 20, 30}
print(set1 & set2)  # d) {10, 20}

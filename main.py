def check_list_elements_recursive(L1, L2):
    if not L1:
        return True
    if L1[0] in L2:
        return check_list_elements_recursive(L1[1:], L2)
    return False
L1 = [1, 2, 3]
L2 = [3, 1, 2, 4, 5]

# перевірка чи всі елементи з L1 є в L2 за допомогою рекурсивної функції
if check_list_elements_recursive(L1, L2):
    print("Всі елементи зі списку L1 входять у список L2")
else:
    print("Не всі елементи зі списку L1 входять у список L2")



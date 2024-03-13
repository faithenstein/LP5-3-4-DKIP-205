# Лабораторная работа №5
# Выполняли Бахтин Данила, Бритвин Антон
# ДКИП-205
# Вариант 3-4

def hex_sum_table():
    print("Hex Addition Table:")
    for i in range(16):
        for j in range(16):
            print(f"{hex(i)} + {hex(j)} = {hex(i + j)}")
        print("")

def hex_mult_table():
    print("Hex Multiplication Table:")
    for i in range(16):
        for j in range(16):
            print(f"{hex(i)} * {hex(j)} = {hex(i * j)}")
        print("")

hex_sum_table()
hex_mult_table()
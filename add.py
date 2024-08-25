def sum(x, y):
    answer = x + y
    return answer

def addition():
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    total = sum(a, b)
    print(f'Sum of {a} and {b} is {total}')

## JANGAN UBAH KOD DI BAWAH ##
if __name__ == "__main__":
    addition()


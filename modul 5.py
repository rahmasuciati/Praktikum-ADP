def input_array():
    valid = False
    while not valid:
        A = list(map(int, input("Masukkan elemen array A (bilangan bulat 0-9): ").split()))
        B = list(map(int, input("Masukkan elemen array B (bilangan bulat 0-9): ").split()))
        valid = all(0 <= num <= 9 for num in A) and all(0 <= num <= 9 for num in B)
        if not valid:
            print("Elemen array tidak valid. Mohon masukkan kembali.")
    return A, B

def display_arrays(A, B):
    OnlyInA = [num for num in A if num not in B]
    OnlyInB = [num for num in B if num not in A]
    InBoth = [num for num in A if num in B]
    
    print("Array yang hanya berada di A:", OnlyInA)
    print("Array yang hanya berada di B:", OnlyInB)
    print("Array yang berada di A dan B:", InBoth)

def main():
    A, B = input_array()
    display_arrays(A, B)

if __name__ == "__main__":
    main()
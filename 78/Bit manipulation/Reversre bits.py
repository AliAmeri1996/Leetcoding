def reverseBits(n: int) -> int:
    result = 0
    for _ in range(32):
        result <<= 1        # Shift result left to make room for the next bit
        result |= (n & 1)   # Add the last bit of n to result
        n >>= 1             # Shift n right to process the next bit
    return result

print(reverseBits(0b00000000000000000000000000010101))




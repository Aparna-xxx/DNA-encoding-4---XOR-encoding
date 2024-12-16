def encode_strings_binary(a: str, b: str):
    ascii_a = [ord(char) for char in a]
    ascii_b = [ord(char) for char in b]
    print("Step 1: Convert strings to ASCII")
    print(f"A (ASCII): {ascii_a}")
    print(f"B (ASCII): {ascii_b}\n")

    binary_a = [format(value, '08b') for value in ascii_a]  # 8-bit binary representation
    binary_b = [format(value, '08b') for value in ascii_b]  # 8-bit binary representation
    print("Step 2: Convert ASCII to Binary")
    print(f"A (Binary): {binary_a}")
    print(f"B (Binary): {binary_b}\n")

    xor_result = [
        format(int(ba, 2) ^ int(bb, 2), '08b')
        for ba, bb in zip(binary_a, binary_b)
    ]
    print("Step 3: Perform XOR")
    print(f"A ⊕ B (XOR Result): {xor_result}\n")

    # Assume address 1 for A and address 2 for B
    address_a = "0001"
    address_b = "0010"
    xor_address = f"1|{address_a}|{address_b}"

    print("Step 4: Assign Address Blocks")
    print(f"Address of A: 0|{address_a}")
    print(f"Address of B: 0|{address_b}")
    print(f"Address of A ⊕ B: {xor_address}\n")

    strand_a = {"payload": binary_a, "address": f"0|{address_a}"}
    strand_b = {"payload": binary_b, "address": f"0|{address_b}"}
    strand_xor = {"payload": xor_result, "address": xor_address}

    print("Step 5: Encoded Strands")
    print(f"A Strand: {strand_a}")
    print(f"B Strand: {strand_b}")
    print(f"A ⊕ B Strand: {strand_xor}")

    return strand_a, strand_b, strand_xor


def decode_lost_strand(lost: str, strand_a, strand_b, strand_xor):
    print(f"\nDecoding when {lost} is lost:\n")

    if lost == "A":
        print("Recovery Process for A:")
        # Recover A using B and A ⊕ B
        recovered_a = [
            format(int(xor, 2) ^ int(b, 2), '08b')
            for xor, b in zip(strand_xor["payload"], strand_b["payload"])
        ]
        print("  Step 1: XOR A ⊕ B with B to recover A")
        print(f"  A ⊕ B (Binary): {strand_xor['payload']}")
        print(f"  B (Binary): {strand_b['payload']}")
        print(f"  Recovered A (Binary): {recovered_a}")

    elif lost == "B":
        print("Recovery Process for B:")

        recovered_b = [
            format(int(xor, 2) ^ int(a, 2), '08b')
            for xor, a in zip(strand_xor["payload"], strand_a["payload"])
        ]
        print("  Step 1: XOR A ⊕ B with A to recover B")
        print(f"  A (Binary): {strand_a['payload']}")
        print(f"  A ⊕ B (Binary): {strand_xor['payload']}")
        print(f"  Recovered B (Binary): {recovered_b}")

    elif lost == "A ⊕ B":
        print("Recovery Process for A ⊕ B:")

        recovered_xor = [
            format(int(a, 2) ^ int(b, 2), '08b')
            for a, b in zip(strand_a["payload"], strand_b["payload"])
        ]
        print("  Step 1: XOR A with B to recover A ⊕ B")
        print(f"  A (Binary): {strand_a['payload']}")
        print(f"  B (Binary): {strand_b['payload']}")
        print(f"  Recovered A ⊕ B (Binary): {recovered_xor}")

    print("\nDecoding complete.\n")



a = input("Enter string A: ")

while True:
    b = input(f"Enter string B (length must be {len(a)}): ")
    if len(b) != len(a):
        print(f"Error: String B must have the same length as A ({len(a)}). Please try again.")
    else:
        break


strand_a, strand_b, strand_xor = encode_strings_binary(a, b)


decode_lost_strand("A", strand_a, strand_b, strand_xor)
decode_lost_strand("B", strand_a, strand_b, strand_xor)
decode_lost_strand("A ⊕ B", strand_a, strand_b, strand_xor)

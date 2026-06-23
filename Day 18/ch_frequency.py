def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch, count in freq.items():
        print(f"{ch} → {count}")

char_frequency("machinelearning")
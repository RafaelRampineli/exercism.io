def distance(strand_a, strand_b):
    if len(strand_a) > len(strand_b):
        raise ValueError("First strand longer than second strand")
    elif len(strand_a) < len(strand_b):
        raise ValueError("Second strand longer than first strand")
    else:
        return len(([position for position in range(0, len(strand_a), 1) if strand_a[position] != strand_b[position]]))
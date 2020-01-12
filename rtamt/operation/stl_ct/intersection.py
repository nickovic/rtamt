from rtamt.enumerations.bool_ops import BooleanOperator

def intersection(a, b, op):
    ans = []
    i = j = 1

    hi = None

    while i < len(a) and j < len(b):
        a_start = a[i - 1][0]
        a_end = a[i][0]
        b_start = b[j - 1][0]
        b_end = b[j][0]

        a_val = a[i-1][1]
        b_val = b[i-1][1]

        lo = max(a_start, b_start)
        hi = min(a_end, b_end)

        val = float("nan")
        if lo <= hi:
            if op == BooleanOperator.AND:
                val = min(a_val, b_val)
            elif op == BooleanOperator.OR:
                val = max(a_val, b_val)
            elif op == BooleanOperator.IMPLIES:
                val = max(-a_val, b_val)
            elif op == BooleanOperator.XOR:
                val = abs(a_val - b_val)
            elif op == BooleanOperator.IFF:
                val = -abs(a_val - b_val)

            ans.append((lo, val))

        if a_end < b_end:
            i += 1
        else:
            j += 1

    if hi is not None:
        ans.append((hi, val))

    return ans

class BitOperator(object):

    def getOnBits(self, num):
        # Stores the number of set bits from 0 -> whatever nth term
        m4 = 0x1 | (0x1 << 8) | (0x1 << 16) | (
            0x1 << 24)  # masking across the 4 bytes
        m1 = 0xFF
        s4 = (num & m4) + ((num >> 1) & m4) + ((num >> 2) & m4) + ((num >> 3) & m4) + \
            ((num >> 4) & m4) + ((num >> 5) & m4) + \
            ((num >> 6) & m4) + ((num >> 7) & m4)
        res = (s4 & m1) + ((s4 >> 8) & m1) + \
            ((s4 >> 16) & m1) + ((s4 >> 24) & m1)
        # return s1;
        return res


# For testing your code uncomment below lines.

b = BitOperator()
print(b.getOnBits(10))

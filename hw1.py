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

# Comment or delete this before submitting.

""""
0000 0001 0000 0001 0000 0001 0000 0001 //m4, masking across the 4 bytes
0000 0000 0000 0000 0000 0000 1111 1111 //m1, masking only 1 byte, the Least Significant Byte (LSB)
m1 = 1111 1111 8 bit mask 

//Using letters we can visualize the arrangement of bits 

pqrs tuvw pqrs tuvw pqrs tuvw pqrs tuvw // num
0000 0001 0000 0001 0000 0001 0000 0001 //m4
---------------------------------------- &
0000 000w 0000 000w 0000 000w 0000 000w //num&m4

pqrs tuvw pqrs tuvw pqrs tuvw pqrs tuvw // num
---------------------------------------- >> 1
0pqr stuv wpqr stuv wpqr stuv wpqr stuv // num >> 1
0000 0001 0000 0001 0000 0001 0000 0001 //m4
---------------------------------------- &
0000 000v 0000 000v 0000 000v 0000 000v //(num>>1)&m4
.
.
pqrs tuvw pqrs tuvw pqrs tuvw pqrs tuvw // num
---------------------------------------- >> 7
0000 000p qrst uvwp qrst uvwp qrst uvwp // num >> 7
0000 0001 0000 0001 0000 0001 0000 0001 //m4
---------------------------------------- &
0000 000p 0000 000p 0000 000p 0000 000p //(num>>7)&m4

0000 abcd 0000 efgh 0000 ijkl 0000 mnop // s4
0000 0000 0000 0000 0000 0000 1111 1111 //m1 
--------------------------------------- &
0000 0000 0000 0000 0000 0000 0000 mnop

0000 0000 0000 abcd 0000 efgh 0000 ijkl // s4 >> 8
0000 0000 0000 0000 0000 0000 1111 1111 //m1 
--------------------------------------- &
0000 0000 0000 0000 0000 0000 0000 ijkl

.
.

0000 0000 0000 0000 0000 0000 0000 abcd // s4 >> 24
0000 0000 0000 0000 0000 0000 1111 1111 //m1 
--------------------------------------- &
0000 0000 0000 0000 0000 0000 0000 abcd

0000 0000 0000 0000 0000 0000 0000 mnop //0 to 8
0000 0000 0000 0000 0000 0000 0000 ijkl //0 to 8
0000 0000 0000 0000 0000 0000 0000 efgh //0 to 8
0000 0000 0000 0000 0000 0000 0000 abcd //0 to 8
--------------------------------------- +
sum

S4 contains 4 bytes, thus 1 of them will contain the number of 1s found in the corresponding byte of x. 
So it's obvious that each byte of s4 contains the same number of 1s as its corresponding byte of x.
In the following formula: int s1 = (s4&m1) + (s4>>8) + (s4>>16) + (s4>>24);
Right shifting s4 to 8 bits will give the number of 2's in byte 2 of x, and so on for 4 bytes. 
Now, 1 byte of s4 will have the number of 1's in the corresponding byte of x. The total number of 1s in x is 
then obtained by adding all.
"""

import ldpc_lu as l
import numpy as np
# Initial
n = 12
d_v = 2
d_c = 4
snr = 0

# Generate check matrix H
H = l.build_H(n,d_v,d_c)
# Generate generation matrix G based on H
H, G = l.build_G(H)
print("The check matrix H is: \n", H)
print("The generation matrix G is: \n", G)

# Generate test bit
k = n//d_c*d_v
x = np.random.randint(2, size=k)
print("The message bit: \n", x)

# Encode
y = l.encoder(G,x)
#print(y)

# BPSK
z = l.BPSK(y,snr)
#print(z)

# LLR
var = 10 ** (-snr / 10)
receive = 2 * z / var
#print(receive)

# Decode
x1 = l.belief_pro_LDPC(receive, H)
print("The decoded message bit: \n", x1)
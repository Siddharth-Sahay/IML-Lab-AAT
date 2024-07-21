from fractions import Fraction

def probability_black_ball(w_A, b_A, w_B, b_B):
    P_W_A = Fraction(w_A, w_A + b_A)
    P_B_A = Fraction(b_A, w_A + b_A)
    P_B_given_W_A = Fraction(b_B, w_B + 1 + b_B)
    P_B_given_B_A = Fraction(b_B + 1, w_B + b_B + 1)
    P_B = P_W_A * P_B_given_W_A + P_B_A * P_B_given_B_A
    
    return P_B

if __name__ == '__main__':
    w_A = 3
    b_A = 4
    w_B = 4
    b_B = 5
    result = probability_black_ball(w_A, b_A, w_B, b_B)
    print(result)
print(probability_black_ball(3, 4, 4, 5))

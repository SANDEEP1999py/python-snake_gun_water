# two option for getting this 
# 1.  using of the random sample library
# 2. generate number with the pseudo random number generator algorithms (LCG)
def LCG_algo(range_value):
    a = 120345671 
    seed = 1
    increment = 13451 # needs to be odd 
    m = 2**17 # using the large prime or power of 2
    x_new = a
    x_new_list = []
    for i in range(0,range_value):
        # Equation of the LCG
        # x_(n+1) = (x_(n) * a + increment ) % m 
        x_new = (x_new*seed + increment) % m
        x_new_list.append(x_new % 3 ) # random number between 0,1,2
    return x_new_list


if __name__ == "__main__":
    LCG_algo()

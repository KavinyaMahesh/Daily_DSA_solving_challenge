def print_n_to_1(current):
        #base case
        if current < 1:
            return

        print(current, end=' ')

        print_n_to_1(current - 1)

if __name__ == "__main__":
    
    n = 10
    print_n_to_1(n)
    

N = int(input("Enter the number of gloves: "))
tags = list(map(int, input("Enter the total tags ").split()))

# dict to count the tag
tag_counts = {}
for tag in tags:
    tag_counts[tag]= tag_counts.get(tag,0)+1
   

# Initialize the total Income 
total_income = 0.0

# calculate the income from the pairs 
for tag, count in tag_counts.items():
    # number of the singles and pairs
    pairs = count //2
    singles = count %2

# Income from the pairs 
    total_income += pairs*(tag+0.1*tag)
# Income from singles
    total_income += singles*(tag*0.5)

print(f"{total_income:.2f}")


def print_pattern(N):
    total_row= (N*2)-1
    middle_row = N
    for i in range(1, total_row+1):
        if i < middle_row:
            print("* " + "  " *(i-2) + ("* " if i > 1 else " "))
        elif i == middle_row:
            print("* " *N)
        else:
            print("* " + "  "*(total_row-i-1) + ("* " if i < total_row else ""))
N = int(input("Enter the Number of line for the pattern"))
print_pattern(N)
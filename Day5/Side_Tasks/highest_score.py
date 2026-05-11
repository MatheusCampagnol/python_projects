student_scores = [180, 124, 165, 173, 189, 169, 146]

sum = 0
max_score = 0
score = 0

def main():
    global sum
    for score in student_scores:
        sum += score
    print(sum)    

def max():
    global max_score, score
    for score in student_scores:
        if score > max_score:
            max_score = score
        else:
            pass
    print(f"Max score is:  {max_score}")

if __name__ == "__main__":
    main()
    max()
while True:
    user_input = input("Please Enter Your String: ")
    if user_input=='x':
        break
    count_ones = 0
    count_zeros = 0
    for char in user_input:
      if char == "1":
        count_ones += 1
      elif char == "0":
        count_zeros += 1
      else:
        print(f"Invalid character: {char}. Please enter only 0s and 1s.")
    print(f"Number of 1s: {count_ones}")
    print(f"Number of 0s: {count_zeros}")

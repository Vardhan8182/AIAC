def cm_to_inches(cm):
    return cm / 2.54

cm_input = float(input("Enter length in centimeters: "))
inches = cm_to_inches(cm_input)
print(f"{cm_input} cm is equal to {inches} inches.")

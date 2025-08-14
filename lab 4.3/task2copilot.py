def cm_to_inches(cm):
    return cm / 2.54

if __name__ == "__main__":
    cm = float(input("Enter length in centimeters: "))
    inches = cm_to_inches(cm)
    print(f"{cm} cm is {inches:.2f} inches.")
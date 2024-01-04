file_name = None
tries = 5
while tries > 0:
    try:
        file_name_given = input("please enter the file's name:  ").strip()
        file_name = open(file_name_given,"r")
        print(file_name.read())
        break
    except FileNotFoundError:
        tries -= 1
        if tries:
            print("Please Make Sure The Name And Path Given Are Valid")
            print(f"you have {tries} tries left")
    except:
        tries -= 1
        if tries:
            print("something went wrong, please try again")
            print(f"you have {tries} tries left")
    finally:
        if file_name is not None and file_name.readable():
            file_name.close()
            print("\nfile closed")
        elif tries == 0:
            print("you're out of tries")
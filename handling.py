import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))


''' Opening Files, When We Open The File Using 'With' it Automatically Closes 
The File When U're Done With it, That's Why it's Considered As a Good Practice. '''


'''  Reading Files  '''
with open('test.txt','r') as f:
    #Printing The Name of The File
    print(f.name,"\n===================")

    #Printing The Mode That We Opened The File With
    print(f.mode,"\n===================")

    #Checking Whether The File is Closed
    print(f.closed,"\n===================") # Returns False in This Case

    #Reading The Content of The File
    content = f.read()
    print(content,"\n===================")

    ''' When We Use read(), it Reads The Entire Content of The File, 
    Leaving The File Pointer Positioned at The End of The File, Same Thing
    if We Use readline() The Pointer Moves To The Next Line. 
    If We Then Try To Use read() Again, it Starts Reading From The 
    Current Position of The File Pointer, Which is Already at The End
    in Case We Used read() and at The Next Line in Case We Used readline(). 
    As a Result, Nothing Gets Printed Out if You Try To Print Out The
    Content of f.read(). So We need to use The seek() Method To Reset 
    The File Pointer, We Can Use The tell() Method To Check What is The 
    Current Position Of The File Pointer.                                                   ''' 
    #Specifying The Size Which We Want To Read Giving The read() Method an Arg
    print(f"The Pointer Before Using The seek() Method:  {f.tell()}") 
    f.seek(0)
    print(f"The Pointer After Using The seek() Method:  {f.tell()}") # 0
    hundred = f.read(100)
    #This Prints Out The First 100 Characters Of The Text File
    print(f"first hundred characters are:  \n{hundred}","\n===================")

    #Making a Good Use Of read() Method So We Don't End Up With Memory Problems
    f.seek(0)
    size_to_read = 10
    to_read = f.read(size_to_read) # Now The Pointer is Pointing To The 11th char
    # Iterating Through The Text By Ten Chars At a Time
    # The len(to_read) Becomes 0 When The Pointers Reaches To The End Of Text
    while len(to_read) > 0: 
        print(to_read,end='') # Printing The 10 Chars it's Holding
        to_read = f.read(size_to_read) # Containing The Next 10 chars

    #Getting all The Lines of The Text As a List
    f.seek(0)
    content_list = f.readlines()
    print(content_list,"\n===================")

    #Getting The Line Which is Being Pointed To Using readline()
    f.seek(0) # Moving The Pointer To The First Line
    first = f.readline()  # First Line in This Case
    second = f.readline() # Second Line 
    third = f.readline()  # and The Third One
    print(first,second,third,end="===================\n")
    
    ''' if We're Dealing With Some Very Large Files We Might End Up With 
        A Memory Problem if We Try To Read The File All At Once Using The
        read() Method. That's When Iterating Comes in Handy           '''
    f.seek(0)
    for line in f:
        print(line,end='') 
    print("\n===================")


''' Writing into Files '''
''''''
with open('test1.txt' ,'w') as f:
    # Writing a Text on a File
    f.write('test') # Now The Pointer is at The End Of The File Text
    # We Can Use seek() The Same As We Used it Before
    f.seek(0) # Now The Pointer is At The Begining Of The File Text
    f.write('test') # This Overrides The First 'test' We Wrote
    f.seek(0)
    f.write('R') # Now The Text is Rest Because 'R' overrode 't'


''' Copying a Text File Into Another '''
with open('test.txt','r') as rf:
    with open('test1.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


''' Copying a Picture '''
with open('Tech Addicted.jpg', 'rb') as rfile:
    with open('Tech Addicted 1.jpg','wb') as wfile:
        for line in rfile:
            wfile.write(line)



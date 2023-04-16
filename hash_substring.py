# python3

def readd_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choise=input();
    if choise=='I':
        template=input();
        string=input();
    elif choise=='F':
        f=open("tests/06","r");
        template=f.readline();
        string=f.readline();
    ret_arr=template+" "+string;
    return ret_arr
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    # this is the sample return, notice the rstrip function
    #return (template.rstrip(), string.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    pattern_hash=0;
    text_hash=0;
    h=1;
    i=0;
    j=0;
    data=[];
    for i in range(len(pattern)-1):
        h=(h*256)%7
    for i in range(len(pattern)):
        pattern_hash=(pattern_hash*256+ord(pattern[i]))%7
        text_hash=(text_hash*256+ord(text[i]))%7
    for i in range(len(text)-len(pattern)+1):
        if pattern_hash==text_hash:
            for j in range(len(pattern)):
                if text[i+j]==pattern[j]:
                    j+=1;
                else:
                    break;
            if j==len(pattern):
                data.append(i);
        if i<(len(text)-len(pattern)):
            text_hash=(256*(text_hash-ord(text[i])*h)+ord(text[i+len(pattern)]))%7;
            if text_hash<0:
                text_hash=text_hash+7;
    # and return an iterable variable
    return data


# this part launches the functions
if __name__ == '__main__':
    arr=readd_input();
    l=arr.split();
    template=l[0];
    string=l[1];
    data=get_occurrences(template,string);

    print_occurrences(data);


MAX_CHARS=256
def max(a,b):
    return a if a>b else b
def badCharHeuristic(pat,size,badchar):
    for i in range(MAX_CHARS):
        badchar[i]=-1
    for i in range(size):
        badchar[ord(pat[i])]=i
def patternsearch(text,pat):
    m=len(pat)
    n=len(text)
    badchar=[-1]*MAX_CHARS
    badCharHeuristic(pat,m,badchar)
    s=0
    while s <= (n-m):
        j=m-1
        while j>=0 and pat[j]==text[s+j]:
            j-=1
        if j<0:
            print("\n pattern occurs at position=",s)
            s+=m-badchar[ord(text[s+m])] if (s+m)<n else 1
        else:
            s+=max(1,j-badchar[ord(text[s+j])])
text=input("enter the text:").rstrip('\n')
pat=input("enter the pattern:").rstrip('\n')
patternsearch(text,pat)
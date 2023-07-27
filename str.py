def merge_the_tools(string, k):
    # your code goes here
        lis = []
        for i in range(0,len(string),k):
            lis.append(string[i:(i + k)])
        
        for j in lis:
            s = ""
            for k in j:
                if k not in s:
                    s += k
            print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
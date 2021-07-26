def romanToInt(s):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    letters=["I","V","X","L","C","D","M"]
    num=0
    for i in range(len(s)):
        if s[i] not in letters:
            break
        val=d[s[i]]
        if i!=0 and d[s[i]]>d[s[i-1]]:
            val=val-d[s[i-1]]*2
        num=num+val
    return num
    
s="MCDLXXVI"
print(romanToInt(s))
        
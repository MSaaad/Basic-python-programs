name=input('Enter a Sentence:') #My name is
Rem_spaces=name.replace(' ','') #MyNameis
text=sorted(Rem_spaces) #['M','y','n','a',...]
print(Rem_spaces)
upper=[]
lower=[]
for word in text:
    if word==word.lower():
        if word not in lower:   #Will Search for lowerCase
            lower.append(word)
    else:        
        if word not in upper:   #Will search for upperCase
            upper.append(word)
        
print('LowerCase =',lower)
print('UpperCase =',upper)
        

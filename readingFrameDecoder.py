#Wrote this while drunk as a funny for one of my classes. Hopefully I can see the letters by the time I'm finished.

#Array order is U-C-A-G.
#Whilst I could use an easier to modify version, I am not planning on using this for xenogenetics any time soon, so this will do great.
aminoAcidEncoder=['|','a','v','l','i','p','m','f','w','g','s','t','c','n','q','y','d','e','k','r','h']
codeTable= [[[7,7,3,3],[10,10,10,10],[15,15,0,0],[12,12,0,8]],[[3,3,3,3],[5,5,5,5],[20,20,15,15],[19,19,19,19]],[[4,4,4,6],[11,11,11,11],[13,13,18,18],[10,10,19,19]],[[2,2,2,2],[1,1,1,1],[16,16,17,17],[9,9,9,9]]]
#Now this I actually plan on making an input if I ever return to this. This shitty system causes issues later in the code
data=[3,2,4,1,4,4,2,2,1,2,4,2,4,2,2,2,3,4,3,3,3,1,2,1,2,3,3,2,2,4,2,4,1,2,1]
#Thing for catch to play with
catToy=0
#I fucking hate python for loops, they work in a way Im not use to using, so I would rather use a while, its just as effiecent
#Anywho, enough about python, I am looping the 3 possible reading frames first
print("Reading sense frames")
i=0
while(i<3):
    thisLine=""#I gave up on readablity already
    j=0
    while(j<(((len(data)+1-i)/3)+1)):#Ugly fucker, but it should work, and I dont exactly plan on using this for large scale stuff. If I do, this is the first place ill look at after insertion.
        try:
            encoded=codeTable[data[j*3+i]-1][data[j*3+1+i]-1][data[j*3+2+i]-1]
            thisLine+=aminoAcidEncoder[encoded]+","
            if(aminoAcidEncoder[encoded]==6):
                print("Ypure blind")
        except:#Cant be fucked at this point actually fixing my pos
            catToy+=1
        j+=1
    print(str(i)+" sense strand:")
    print(thisLine)
    i+=1
#Antisense shittery (flips data to give antisense)
antiData=[0]*len(data)
i=0
while(i<len(data)):
    if(data[i]<2):
        antiData[i]=data[i]+2
    else:
        antiData[i]=data[i]-2
    i+=1
print("Reading antisense frames")
i=0
while(i<3):
    thisLine=""#I gave up on readablity already
    j=0
    while(j<(((len(antiData)+1-i)/3)+1)):#Ugly fucker, but it should work, and I dont exactly plan on using this for large scale stuff. If I do, this is the first place ill look at after insertion.
        try:
            encoded=codeTable[antiData[j*3+i]-1][antiData[j*3+1+i]-1][antiData[j*3+2+i]-1]
            thisLine+=aminoAcidEncoder[encoded]+","
            if(aminoAcidEncoder[encoded]==6):
                print("Ypure blind")
        except:#Cant be fucked at this point actually fixing my pos
            catToy+=1
        j+=1
    print(str(i)+" antisense strand:")
    print(thisLine)
    i+=1
print("Catch has played with its toy "+str(catToy)+" times!")

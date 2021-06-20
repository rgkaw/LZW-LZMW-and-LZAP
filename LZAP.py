
#funtsi untuk mengkompress
def compress(array):
    last=256
    i=0
    array_len=len(array)
    prev_match=b''
    match=b''
    out=[]
    while(i<array_len):
        match=bytes([array[i]])
        
        while(match in dictionary):
            i=i+1
            try:
                match=match+bytes([array[i]])
            except:
                match=match+bytes([array[i-1]])
                break
        match=match[:-1]
        out.append(dictionary[match])
        if(prev_match+match) not in dictionary:
            x=match
            for j in range(len(x)-1,0,-1):
                dictionary[prev_match+match[:-j]]=last
                last+=1
            dictionary[prev_match+match]=last
            last+=1
        prev_match=match
    return out
def output_to_bytes(array):
    i=0
    bits=0
    bit_chunks=0
    #max length in decimal
    mldec=max(array)
    #max length in binary
    mlbin=1
    x=mldec
    out=[]
    while x>1:
        x=x>>1
        mlbin+=1
    out.append(mlbin)
    while i<len(array):
        while bits<=mlbin:
            j=array[i]
            i=i+1
            x=j
            bit_chunks=(bit_chunks<<mlbin)|j
            bits=bits+mlbin
            if i>=len(array):
                break
        while bits>=8:
            bits=bits-8
            temp=bit_chunks>>(bits)
            out.append(temp)
            bit_chunks=bit_chunks&((2**(bits))-1)
    if i>=len(array):
        if(bits!=0):
            padding=8-bits
            bit_chunks=(bit_chunks<<(padding))|((2**padding)-1)
            out.append(bit_chunks)
            out.append(padding)
        else:
            out.append(0)
    return bytes(out)


#input file
f=open(file=r'text_3.txt',mode='r+b')
input_=f.read()

print("making dictionary...")
#make dictionary
dictionary={bytes([i]):i for i in range(256)}

print("\tinput size\t: ",len(input_),'bytes')

print("compressing...")
output=compress(input_)

print("converting to bytes...")
#convert output list into bytes
output=output_to_bytes(output)
print("saving file....")
print("\toutput size:\t",len(output),"bytes")
#WRITE FILE OUTPUT
f=open(file=r'text_3_LZAP',mode='w+b')
f.write(output)
f.close()
print("done!!")

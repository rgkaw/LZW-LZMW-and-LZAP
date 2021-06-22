
def encode(array):
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


from time import sleep
def get_string(idx):
    a=b''
    for i in dictionary:
        if dictionary[i]==idx:
            a=i
    return a


def decode(array):
    out=b''
    match=b''
    prev_match=b''
    last=256
    try:
        for i in array:
            match=get_string(i)
            out=out+match
            x=b''
            x=(prev_match)+match
            if x not in dictionary:
                dictionary[x]=last
                last+=1
            prev_match=match
    except:
        out=out+(get_string(i))

    return out
def bytes_to_int(array):
    out=[]
    byte_chunk=0
    bits=0
    length=array[0]
    padding=array[-1]
    array=array[1:-1]
    size=len(array)
    i=0
    while i<size-1:
        while (bits<length) & (i<size-1):

            #print(array[i])
            #sleep(1)
            #print(type(byte_chunk))
            byte_chunk=(byte_chunk<<8)+array[i]
            bits=bits+8
            i+=1
           # print('1',byte_chunk,bits)
        while bits>=length:
            bits=bits-length
            temp=byte_chunk>>(bits)
            out.append(temp)
            byte_chunk=byte_chunk&((2**bits)-1)
    byte_chunk=(byte_chunk<<8)+array[i]
    byte_chunk=byte_chunk>>padding
    out.append(byte_chunk)
    return out



def compress():
    print('You choose to compress file. Place file to compress in the same directory as this program.')
    input_file=str(input("Input file (ex :file.txt): "))
    f=open(file=input_file,mode='r+b')
    input_=f.read()
    file_name=''
    for i in input_file:
        if i == '.':
            break
        file_name=file_name+i
    print("making dictionary...")
    #make dictionary
    dictionary={bytes([i]):i for i in range(256)}
    print("\tinput size\t: ",len(input_),'bytes')

    print("compressing...")
    output=encode(input_)

    print("converting to bytes...")
    #convert output list into bytes
    output=output_to_bytes(output)
    print("saving file....")
    print("\toutput size:\t",len(output),"bytes")
    #WRITE FILE OUTPUT
    f=open(file=file_name+'.LZMW',mode='w+b')
    f.write(output)
    f.close()
    print("done!!")


def decompress():
    print('You choose to decompress file. Place file to decompress in the same directory as this program.')
    input_file=input(str("Input file (ex :file.LZMW): "))
    file_name=''
    for i in input_file:
        if i == '.':
            break
        file_name=file_name+i

    f=open(file=input_file,mode='r+b')
    input_=f.read()
    print("\tfile size: ",len(input_),'bytes')
    print("preparing files...")
    input_=bytes_to_int(input_)
    print("creating dictionary...")
    dictionary={bytes([i]):i for i in range(256)}
    print("decompressing...")
    output=decode(input_)
    print("done!")
    print("\toutput size:\t",len(output),'\n')
    f=open(file=file_name+'_LZMW.txt',mode='w+b')
    f.write(output)
    f.close()

while True:
    dictionary={bytes([i]):i for i in range(256)}
    try:
        choice=int(input("1. compress\n2. decompress\n0. exit\n\tyour choice:"))
        try:
            if choice==1:
                compress()
            elif choice==2:
                decompress()
            elif choice==0:
                break
            else:
                print("invalid input")
        except:
            print('cannot find file...')
    except:
        print("invalid input (not integer)")

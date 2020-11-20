import hashlib

def getNsTokenSig(sig,token_salt):
    str1 = "922cd3510ec0bf87928369e0afd14d3d"
    str2 = "0374c840fc3941a38daf5fe1dd9456c8"
    str3 = str1+str2
    cc = bytearray(str3.encode())
    for i in cc:
        print(i)
    nstokensig = hashlib.sha256(bytearray(str3.encode())).hexdigest()
    print(nstokensig)
    return nstokensig

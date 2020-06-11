import secrets
from coincurve import PublicKey, PrivateKey
from sha3 import keccak_256


def generateKey():
    # [type] PrivateKey
    priKey = PrivateKey()
    # [type] bytes
    pubKey = priKey.public_key.format(compressed=False)[1:]
    # address
    addr = keccak_256(pubKey).digest()[-20:]

    return{
        "privateKey": str(priKey.to_hex()),
        "publicKey": str(pubKey.hex()),
        "address": str(addr.hex()),
        "address(EIP-55)": str(addCheckSum(addr))
    }


def addCheckSum(address):
    _address = address.hex()
    formated_address = ""
    addressHash = keccak_256(
        str(address.hex()).encode("UTF-8")).digest()[:40].hex()
    for i in range(40):
        if(int(addressHash[i], 16) >= 8 and int(_address[i], 16) >= 10):
            formated_address += str(_address[i]).upper()
        else:
            formated_address += str(_address[i])
    return formated_address

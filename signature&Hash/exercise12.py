"""
 --------------------------------------------------------------------------------------
    Original Code: Dr. Scott Simmons
    Authors: Marina Amorim, Laura Pareja
    Class: SS Math - Cryptography
    Topic: human_readable_messages
    Date Creation: 02/21/22
    Last Date Modified: 02/02/22


    
 """



def OS2IP(X):
    """Return the integer primitive x for the octet-string X."""
    # the sum below is the same as: int.from_bytes(X, byteorder = 'big')
    return sum([x * 256**i for i, x in enumerate(X[::-1])])

def I2OSP(x, xLen):
    """Map an integer x to an octet-string X of length xLen."""
    assert x < 256**xLen, "integer too large"
    # below is the same as: return x.to_bytes(xLen, byteorder = 'big')
    if x == 0:
        return b'\x00'
    bs = b''
    while x:
        bs += (x % 256).to_bytes(1, byteorder = 'big')
        x //= 256
    return b'\x00' * (xLen - len(bs)) + bs[::-1]


""""
 --------------------------------------------------------------------------------------

    EXERCISE 12: The following integers were obtained by partitioning the bytes version
    of a long human-readable message into pieces and applying OS2IP to each piece in 
    turn. Decode the 3 integers back into a single human-readable message
    assuming that $xLen = 116$.

--------------------------------------------------------------------------------------
"""


m_1= 1725407206559124414262775558036503363064228085318307003328879078787363094423245885746439779754368306393587124793170863467980001097533679809384382517969177269488080616807424955212840365424212959420111398825941435746017065393535568260957387818213402876939831656625655617513727553140
m_2= 287101874499563511517274625693599634164659978647960508961005359525734553050793584577215512179449180764094683149204979666322538790035994601590541117759527904133629733463936649070787697899716452610376032894463212129223492366548874418088170509640147500836911687180980832066830360864
m_3= 4036157892442068336082369800710226842901895235006035033530534455492109324426834792892671498674394861228244517069702057


message = I2OSP(m_1, 116) 
message+= I2OSP(m_2, 116)  
message+= I2OSP(m_3, 116) 


#print(message.decode('utf8'))

# « Les mathématiciens n'étudient pas des objets,
#  mais des relations entre les objets; il leurest 
# donc indifférent de remplacer ces objets par d'autres, 
# pourvu que les relations ne changent pas. La atière ne 
# leur importe pas, la forme seule les intéresse. » -- Henri Poincaré







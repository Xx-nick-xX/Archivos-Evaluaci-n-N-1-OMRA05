aclNum = int(input("¿cual es el número IPv4 ACL?"))
if aclNum >=1 and aclNum <=99:
    print("este es un ACL IPv4 estándar.")
elif aclNum >=100 and aclNum <=199:
    print("este es un ACL IPv4 extendida")
else:
    print("esta ACL IPv4 no es extendida o estandar.")
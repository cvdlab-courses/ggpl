x = [.1,-.05,.001,-.05]
a = QUOTE(x*5)
aa = PROD([a,a])
aaa = PROD([aa,a])
VIEW(aaa)


b = CUBOID([1,2,3])
d = STRUCT([b,T(1)(4.0),b])
VIEW(d)


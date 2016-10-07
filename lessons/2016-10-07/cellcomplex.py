X = [.1,-.05,.001,-.05]
a = QUOTE(X*5)
aa = PROD([a,a])
aaa = PROD([aa,a])
VIEW(aaa)

variable1="Esta es la cadena que queres"
StrVoc="aeiou"
StrVoc+=StrVoc.upper()

def Vocal_Find(variable1,StrVoc):
	ComList=[]
	for i in variable1:
		for u in StrVoc:
			if i == u:
				ComList.append(i)
	StrFunList=str(ComList)

	return StrFunList

print(Vocal_Find(variable1,StrVoc))

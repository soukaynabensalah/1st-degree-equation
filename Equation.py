a=int(input("entrer le 1er coefficient"))
b=int(input("entrer le 2ème coefficient"))
c=int(input("entrer le 3ème coefficient"))
∆=b^2-4*a*c
if ∆>0 :
  print("les solutions de cette équation est :",(-b+sqrt(∆))/2*a or (-b-sqrt(∆))/2*a)
elif ∆=0 :
  print("la solution de cette équation est :",-b/2*a)
else
  print("pas de solution")

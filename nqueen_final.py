



import numpy as np
global N
#N=8
N=int(input("pleas enter the number of Queen:"))

def NQueensol(n):
  solslist=[]
  if n==0:
    solslist=[[]]
    return solslist

  subsol=NQueensol(n-1)

  for sol in subsol:
    for row in range(1,N+1):
      if CheckPlace(row,sol):
        solslist.append(sol+[[row,n]])
  
  return solslist
  



def CheckPlace(row,queens):
  col=len(queens)+1
  for q in queens:
    rq=q[0]
    cq=q[1]

    if (col-cq)==-(row-rq):
      return False
    if (col-cq)==(row-rq):
      return False

    if rq==row:
      return False
    if cq==col:
      return False

  return True



def printnqueen(solslist):

  if len(solslist)!=0 and solslist!=[[]]:
    counter=1
  else:
    counter=0



  
  for s in solslist:
    print("solution number",counter)
    print(s,"\n")
    m=np.zeros((N,N))
    print("Chessbaord :")

    for i in range(0,N):
      r=s[i][0]
      c=s[i][1]

      m[r-1][c-1]=m[r-1][c-1]+1

    print(m)
    counter=counter+1

  if len(solslist)!=0 and solslist!=[[]]:
    print("\nThe number of total solutions is ---->",len(solslist))
  else:
    print("There is no solution!")

  





solutions = NQueensol(N)
printnqueen(solutions)
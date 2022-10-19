

import random as rnd
import matplotlib.pyplot as plt

populationSize=500
n=10
mu_rate=0.8
epoch=300

def population(population_size,n):
  population=[]
  for i in range(population_size):
    NewMemeber=[]
    for j in range(n):
      NewMemeber.append(rnd.randint(1,n))
    NewMemeber.append(0)
    population.append(NewMemeber)

  return population

def cross_over(population_list):
  for i in range(0,len(population_list),2):

    child1=population_list[i][:len(population_list[0])//2]+population_list[i+1][len(population_list[0])//2:len(population_list[0])-1]+[0]
    child2=population_list[i+1][:len(population_list[0])//2]+population_list[i][len(population_list[0])//2:len(population_list[0])-1]+[0]

    population_list.append(child1)
    population_list.append(child2)
   



  return population_list

def mutation(population_list,mutation_rate,n):

    choosen_child=[i for i in range(len(population_list)//2,len(population_list))]

    for i in range(len(population_list)//2):
      random_number=rnd.randint(0,(len(population_list)//2)-1)
      choosen_child[random_number],choosen_child[i]=choosen_child[i],choosen_child[random_number]
    choosen_child=choosen_child[:int(len(choosen_child)*mutation_rate)]

    for i in choosen_child:
      new_ch=rnd.randint(0,n-1)
      new_val=rnd.randint(1,n)
      population_list[i][new_ch]=new_val

    return population_list

def NQueenSolution(population_list,n):

  conflict_number=0
  for i in range(0,len(population_list)):
    conflict_number=0
    for j in range(0,n):
      for  l in  range(j+1,n):
        if population_list[i][j]==population_list[i][l]:
          conflict_number+=1
        if abs(j-l)==abs(population_list[i][j]-population_list[i][l]):
          conflict_number+=1
    population_list[i][-1]=conflict_number
  for i in range(len(population_list)):
    min=i
    for j in range(i,len(population_list)):
      if population_list[j][n]<population_list[min][n]:
        min=j
      temp=population_list[i]
      population_list[i]=population_list[min]
      population_list[min]=temp


  return population_list

def cheessboard(res):
    l = len(res)
    plt.figure(figsize=(6, 6))
    plt.scatter([x+1 for x in range(l - 1)], res[:l - 1])
    for i in range(l):
        plt.plot([0.5, l - 0.5], [i + 0.5, i + 0.5], color = "k")
        plt.plot([i + 0.5, i + 0.5], [0.5, l - 0.5], color = "k")



i=0
solutions=[]
while i<5:
  # print('iteration--->'i+1)
  population1=population(populationSize,n)
  sol_number=0
  iteration=0
  while sol_number<1:
    
    population1=cross_over(population1)
    population1=mutation(population1,mu_rate,n)
    population1=NQueenSolution(population1,n)
    population1=population1[:len(population1)//2]

    if population1[0][n]==0:
      if (population1[0][0:n] in solutions)==False:

        print("solution founded",population1[0][0:n])
        solutions.append(population1[0][0:n])
        sol_number+=1
        cheessboard(population1[0])
      break
    if iteration>epoch:
      break
    iteration+=1
    # print(iteration)
  if sol_number==1:
    i+=1




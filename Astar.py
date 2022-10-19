

def AStarSearch(start, goal , adjac_lis, h):
  cost={start:0}
  closed=[]
  opened=[(start,8)]
  
  while True:
    
    fn=[i[1] for i in opened]
    chosen_index=fn.index(min(fn))
    node=opened[chosen_index][0]
    closed.append(opened[chosen_index])
    # print("closed",closed)
    del opened[chosen_index]
    if closed[-1][0] == goal:
      break

    for item in adjac_lis[node]:
      if item[0] in [closed_item[0] for closed_item in closed]:
        # print("item[0]",item[0])
        continue
      cost.update({item[0]:cost[node] + item[1]})
      # print("cost",cost)
      fn = cost[node] + h[item[0]] + item[1]
      temp = [item[0], fn]
      opened.append(temp)



  t_node= goal
  optimal_path=[goal]
  for i in range(len(closed)-2,-1,-1):
    check_node = closed[i][0]
    if t_node in [childeren[0] for childeren in adjac_lis[check_node]]:
      childeren_costs = [temp[1] for temp in adjac_lis[check_node]]
      childeren_nodes = [temp[0] for temp in adjac_lis[check_node]]

      if cost[check_node] + childeren_costs[childeren_nodes.index(t_node)] == cost[t_node]:
        optimal_path.append(check_node)
        t_node = check_node

  optimal_path.reverse()
  return optimal_path

  

if __name__ == "__main__":
  adjac_lis = {
    'A': [('B', 1),  ('D', 4)],
    'B': [('A',1),('C',2),('D', 2)],
    'C': [('E', 2)],
    'D': [('A',1),('C',3),('E',3)]
  }
  h = {'A': 8, 'B': 6, 'C': 3, 'D': 2,'E': 0 }

  op_path=AStarSearch('A','E',adjac_lis,h)

  print("optimal Path: " + str(op_path))


name = '_________'
n = 20
lastele = ['O']
for i in range(0,n):
  print('---------')
  print('|',name[0],name[1],name[2],'|')
  print('|',name[3],name[4],name[5],'|')
  print('|',name[6],name[7],name[8],'|')
  print('---------')  
  cord = input("Enter coordinates")
  if cord == "one two":
    print("You should enter numbers!")
    continue
  if cord == "one one":
    print("You should enter numbers!")
    continue
  if cord == "one three":
    print("You should enter numbers!")
    continue
  if cord == "two one":
    print("You should enter numbers!")
    continue
  if cord == "two two":
    print("You should enter numbers!")
    continue
  if cord == "two three":
    print("You should enter numbers!")
    continue
  if cord == "three one":
    print("You should enter numbers!")
    continue
  if cord == "three three":
    print("You should enter numbers!")
    continue
  if cord == "three three":
    print("You should enter numbers!")
    continue
    
  c1 = int(cord[0])
  c2 = int(cord[2])
  if c1 > 3 or c2 > 3:
    print("Coordinates should be from 1 to 3!")
    continue

  if c1 == 1 and c2 == 1:#1,1
    if name[6] == 'X' or name[6] == 'O':
      print("This cell is occupied! Choose another one!")
      continue
    if(i == 0):
      X = 'X'
      name = name[:6] + X + name[7:]
      lastele.append('X')
      
    else:
        if lastele[-1] == 'X':
            X = 'O'
            name = name[:6] + X + name[7:]
            lastele.append('O')
            
        else:
            X = 'X'
            name = name[:6] + X + name[7:]
            lastele.append('X')
            

      

  if c1 == 1 and c2 == 2:#1,2
    if name[3] == 'X' or name[3] == 'O':
      print("This cell is occupied! Choose another one!")
      continue
    if(i == 0):
      X = 'X'
      name = name[:3] + X + name[4:]
      lastele.append('X')
      
    else:
        if lastele[-1] == 'X':
            X = 'O'
            name = name[:3] + X + name[4:]
            lastele.append('O')
            
        else:
            X = 'X'
            name = name[:3] + X + name[4:]
            lastele.append('X')
            

  if c1 == 1 and c2 == 3:#1,3
    if name[0] == 'X' or name[0] == 'O':
      print("This cell is occupied! Choose another one!")
      continue
    if(i == 0):
      X = 'X'
      name = X + name[1:]
      lastele.append('X')
      
    else:
        if lastele[-1] == 'X':
            X = 'O'
            name = X + name[1:]
            lastele.append('O')
            
        else:
            X = 'X'
            name = X + name[1:]
            lastele.append('X')
            

  if c1 == 2 and c2 == 1:#2,1
    if name[7] == 'X' or name[7] == 'O':
      print("This cell is occupied! Choose another one!")
      continue
    if(i == 0):
      X = 'X'
      name = name[:7] + X + name[8]
      lastele.append(X)
      
    else:
        if lastele[-1] == 'X':
            X = 'O'
            name = name[:7] + X + name[8]
            lastele.append(X)
            
        else:
            X = 'X'
            name = name[:7] + X + name[8]
            lastele.append(X)
            

  if c1 == 2 and c2 == 2:#2,2
    if name[4] == 'X' or name[4] == 'O':
      print("This cell is occupied! Choose another one!")
      continue
    if (i == 0):
      X = 'X'
      name = name[:4] + X + name[5:]
      lastele.append(X)
      
    else:
        if lastele[-1] == 'X':
            X = 'O'
            name = name[:4] + X + name[5:]
            lastele.append(X)
            
        else:
            X = 'X'
            name = name[:4] + X + name[5:]
            lastele.append(X)
            

  if c1 == 2 and c2 == 3:#2,3
    if name[1] == 'X' or name[1] == 'O':
      print("This cell is occupied! Choose another one!")
      continue
    if(i == 0):
      X = 'X'
      name = name[:1] + X + name[2:]
      lastele.append(X)
      
    else:
        if lastele[-1] == 'X':
            X = 'O'
            name = name[:1] + X + name[2:]
            lastele.append(X)
            
        else:
            X = 'X'
            name = name[:1] + X + name[2:]
            lastele.append(X)
            

  if c1 == 3 and c2 == 1:#3,1
    if name[8] == 'X' or name[8] == 'O':
      print("This cell is occupied! Choose another one!")
      continue
    if(i == 0):
      X = 'X'
      name = name[:8] + X
      lastele.append(X)
      
    else:
        if lastele[-1] == 'X':
            X = 'O'
            name = name[:8] + X
            lastele.append(X)
            
        else:
            X = 'X'
            name = name[:8] + X
            lastele.append(X)
            
  
  if c1 == 3 and c2 == 2:#3,2
    if name[5] == 'X' or name[5] == 'O':
      print("This cell is occupied! Choose another one!")
      continue
    if(i == 0):
      X = 'X'
      name = name[:5] + X + name[6:]
      lastele.append(X)
      
    else:
        if lastele[-1] == 'X':
            X = 'O'
            name = name[:5] + X + name[6:]
            lastele.append(X)
            
        else:
            X = 'X'
            name = name[:5] + X + name[6:]
            lastele.append(X)
            

  if c1 == 3 and c2 == 3:#3,3
    if name[2] == 'X' or name[2] == 'O':
      print("This cell is occupied! Choose another one!")
      continue
    if(i == 0):
      X = 'X'
      name = name[:2] + X + name[3:] 
      lastele.append(X)
      
    else:
        if lastele[-1] == 'X':
            X = 'O'
            name = name[:2] + X + name[3:] 
            lastele.append(X)
            
        else:
            X = 'X'
            name = name[:2] + X + name[3:] 
            lastele.append(X)
  print(name)
  print('---------')
  print('|',name[0],name[1],name[2],'|')
  print('|',name[3],name[4],name[5],'|')
  print('|',name[6],name[7],name[8],'|')
  print('---------')
  
  if name[0] == '_':
    print('Game not finished')
  elif name[1] == '_':
    print('Game not finished')
  elif name[2] == '_':
    print('Game not finished')
  elif name[3] == '_':
    print('Game not finished')
  elif name[4] == '_':
    print('Game not finished')
  elif name[5] == '_':
    print('Game not finished')  
  elif name[6] == '_':
    print('Game not finished')
  elif name[7] == '_':
    print('Game not finished')
  elif name[8] == '_':
    print('Game not finished')

  elif (name[0] == name[4] == name[8]):
    if name[0] == 'X':    
      print('X wins')
      break
    else:
      print('O wins')
      break
  elif (name[2] == name[4] == name[6]):
    if name[2] == 'X':
      print('X wins')
      break
    else:
      print('O wins')
      break
  elif (name[0] == name[1] == name[2]):
    if name[0] == 'X':
      print('X wins')
      break
    else:
      print('O wins')
      break
  elif (name[3] == name[4] == name[5]):
    if name[3] == 'X':
      print('X wins')
      break
    else:
      print('O wins')
      break
  elif (name[6] == name[7] == name[8]):
    if name[6] == 'X':
      print('X wins')
      break
    else:
      print('O wins')
      break
  elif (name[0] == name[3] == name[6]):
    if name[0] == 'X':
      print('X wins')
      break
    else:
      print('O wins') 
      break
  elif (name[1] == name[4] == name[7]):
    if name[1] == 'X':
      print('X wins')
      break
    else:
      print('O wins')
      break
  elif (name[2] == name[5] == name[8]):
    if name[2] == 'X':
      print('X wins')
      break
    else:
      print('O wins')
      break
    

                
  else :
    print("Draw")
    break

  
    

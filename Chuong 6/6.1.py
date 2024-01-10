for i in range(1, 6):
  h = ""
  for j in range(1, 7):
    if j == 1 or j == 2 or j == 5 or j ==6:
      h = h + "*"
    else:
      if i ==3:
        h = h + "*"
      else:
        h = h + " "

  e = ""
  for j in range(1, 7):
      if j == 1 or j == 2:
          e = e + "*"
      else:
          if i ==1 or i ==3 or i ==5:
              e = e + "*"
          else:
              e = e + " "

  l1 = ""
  for j in range(1,7):
      if j == 1 or j == 2:
          l1 = l1 + "*"
      else:
          if i == 5:
              l1 = l1 + "*"
          else:
              l1 = l1 +" "

  l2 = ""
  for j in range(1,7):
      if j == 1 or j == 2:
          l2 = l2 + "*"
      else:
          if i == 5:
              l2 = l2 + "*"
          else:
              l2 = l2 +" "

  o = ""
  for j in range(1,7):
      if j == 1 or j == 2 or j == 5 or j == 6:
          o = o + "*"
      else:
          if i == 1 or i == 5:
              o = o + "*"
          else:
              o = o + " "
  hello = h + "  " + e + "  " + l1 + "  " + l2 + "  " + o
  print(hello)
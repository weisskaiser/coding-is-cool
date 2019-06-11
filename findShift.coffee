A = 'abcdae'
B = 'cdaeab'

shiftMatch = (a, b) =>
  
  return -1 if typeof a is 'undefined' or typeof b is 'undefined'
  
  return -1 if not a? or not b?
  
  return -1 if a.length isnt b.length
    
  j = 0
  i = b.indexOf a[0]
  
  while i >= 0
    
    k = i
    left = a.length - 1
    
    while left > 0
      
      if a[++j] is b[++k % b.length]
        
        left--
      
      else
        
        break
    
    if left == 0
      
      return i
  
    j = 0
    i = b.indexOf a[0], i+1
  
  return -1

console.log shiftMatch A, B

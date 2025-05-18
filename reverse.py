class Solutions(object):
  def reverseString(self,s):
   left,right=0,lens(s)-1
    while left < right:
     s[left],s[right]=s[right],s[left]
     left +=1
     right-=1

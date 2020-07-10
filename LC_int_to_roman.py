# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:04:05 2020

@author: Necro
"""
#m1

def int_rom_1(intg):
    my_dict= {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
    
    
    
    
    ans=""
    
    for k in my_dict:
        while intg>=k:
            ans=ans+my_dict[k]
            intg=intg-k
            
    return(ans)

#m2
def int_rom_2(intg):
    keys=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    value=['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    ans=""
    i=0
    while intg>0:
        if keys[i]<=intg:
            intg=intg-keys[i]
            ans=ans+value[i]
        else:
            i=i+1
    return(ans)


def main():
   #testcases
   sol_dict={3:"III",4:"IV",9:"IX",58:"LVIII",1994:"MCMXCIV"}
   print("M1")
   for k in sol_dict:
       if int_rom_1(k)==sol_dict[k]:
           print("Test case for ",k,"passed")
       else:
           print("Test case for ",k,"did not pass")
   print("M2")
   for k in sol_dict:
       if int_rom_2(k)==sol_dict[k]:
           print("Test case for ",k,"passed")
       else:
           print("Test case for ",k,"did not pass")
   
if __name__ == '__main__':

    main()
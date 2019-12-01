#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output
boat_side='Right'
missionaries_on_right=3
cannibals_on_right=3
missionaries_on_left=0
cannibals_on_left=0
mis='\U0001f482'
can='\U0001f479'
wave='\U0001f30a'
boat='\U0001f6A2'
#### Your code ####
#print('M = '+str(missionaries_on_left)+' C = '+str(cannibals_on_left)+'|-----B|'+'M = '+str(missionaries_on_right)+' C = '+str(cannibals_on_right))
print(mis*missionaries_on_left+can*cannibals_on_left+' '+wave+wave+wave+boat+' '+mis*missionaries_on_right+can*cannibals_on_right)
while(True):
    print('Enter the number of missionaries:')
    missionaries=int(input())
    print('Enter the number of cannibals:')
    cannibals=int(input())
    if((missionaries+cannibals)<1 or (missionaries+cannibals)>2):
        print('Invalid move')
        continue
    if(boat_side == 'Right'):
        if(missionaries_on_right<missionaries or cannibals_on_right<cannibals):
            print('Invalid move')
            continue;
        missionaries_on_right=missionaries_on_right-missionaries
        cannibals_on_right=cannibals_on_right-cannibals
        missionaries_on_left=missionaries_on_left+missionaries
        cannibals_on_left=cannibals_on_left+cannibals
        if(missionaries_on_right>0 and missionaries_on_left>0):
            if(missionaries_on_left<cannibals_on_left or missionaries_on_right<cannibals_on_right):
                print('YOU LOSE')
                break
        if(missionaries_on_left ==3 and cannibals_on_left==3):
            print('YOU WIN')
            break
        boat_side='Left'
        clear_output()
        #print('M = '+str(missionaries_on_left)+' C = '+str(cannibals_on_left)+'|B-----|'+'M = '+str(missionaries_on_right)+' C = '+str(cannibals_on_right))
        print(mis*missionaries_on_left+can*cannibals_on_left+' '+boat+wave+wave+wave+' '+mis*missionaries_on_right+can*cannibals_on_right)
        continue
       
       
       
    if(boat_side == 'Left'):
        if(missionaries_on_left<missionaries or cannibals_on_left<cannibals):
            print('Invalid move')
            continue;
        missionaries_on_left=missionaries_on_left-missionaries
        cannibals_on_left=cannibals_on_left-cannibals
        missionaries_on_right=missionaries_on_right+missionaries
        cannibals_on_right=cannibals_on_right+cannibals
        if(missionaries_on_right>0 and missionaries_on_left>0):
            if(missionaries_on_left<cannibals_on_left or missionaries_on_right<cannibals_on_right):
                print('YOU LOSE')
                break
        if(missionaries_on_right>0 and missionaries_on_left>0):
            if(missionaries_on_left ==3 and cannibals_on_left==3):
                print('YOU WIN')
                break
        boat_side='Right'
        clear_output()
        #print('M = '+str(missionaries_on_left)+' C = '+str(cannibals_on_left)+'|-----B|'+'M = '+str(missionaries_on_right)+' C = '+str(cannibals_on_right))
        print((mis*missionaries_on_left)+(can*cannibals_on_left)+' '+wave+wave+wave+boat+' '+(mis*missionaries_on_right)+(can*cannibals_on_right))
        continue


# In[ ]:





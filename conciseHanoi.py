# aryan kolapkar
# 190260010
# aryan_kolapkar

def conciseHanoi(n):
    order_list1={'A':'C','C':'B','B':'A'}#['A','B','C']
    order_list2={'A':'B','B':'C','C':'A'}#['A','C','B']

    disc_states={'A':[*range(2,n+1,1)],'B':[],'C':[]} #initially
    one_state='A'#0
    if n%2==0:
        order_list=order_list1
    else:
        order_list=order_list2
    while disc_states['B']!=[*range(1,n+1,1)]:
        # do step 1
        if n%2==0:#even anticlock
            print('{} {} 1'.format(one_state,order_list[one_state]))
            one_state=order_list[one_state]
            #order_list=order_list1
        else:
            print('{} {} 1'.format(one_state,order_list[one_state]))
            one_state=order_list[one_state]
            #order_list =order_list2
        
        # check if solution alfready attained
        if disc_states['B']==[*range(2,n+1,1)]:
            return None#disc_states

        one_pole=one_state#order_list[one_state] 

        copy_dict=disc_states.copy()
        copy_dict.pop(one_pole)

        copy_order =order_list.copy()
        copy_order.pop(one_pole)
        copy_order=list(copy_dict.keys())
        # do step 2
        if len(copy_dict[copy_order[0]])!=0 and len(copy_dict[copy_order[1]])!=0:
            if copy_dict[copy_order[0]][0]>copy_dict[copy_order[1]][0]:
                q=copy_dict[copy_order[1]][0]
                copy_dict[copy_order[1]].remove(q)
                copy_dict[copy_order[0]].insert(0,q)
                print('{} {} {}'.format(copy_order[1],copy_order[0],q))
            else:
                q=copy_dict[copy_order[0]][0]
                copy_dict[copy_order[0]].remove(q)
                copy_dict[copy_order[1]].insert(0,q)  
                print('{} {} {}'.format(copy_order[0],copy_order[1],q))              
        elif len(copy_dict[copy_order[0]])==0:
            q=copy_dict[copy_order[1]][0]
            copy_dict[copy_order[1]].remove(q)
            copy_dict[copy_order[0]].insert(0,q)
            print('{} {} {}'.format(copy_order[1],copy_order[0],q))
        elif len(copy_dict[copy_order[1]])==0:
            q=copy_dict[copy_order[0]][0]
            copy_dict[copy_order[0]].remove(q)
            copy_dict[copy_order[1]].insert(0,q)
            print('{} {} {}'.format(copy_order[0],copy_order[1],q))
        
        disc_states[copy_order[0]]=copy_dict[copy_order[0]]
        disc_states[copy_order[1]]=copy_dict[copy_order[1]]

if __name__ == "__main__":
    n=input()
    conciseHanoi(int(n))
   
   
        
        

        
                
    
        







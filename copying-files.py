with open('hamburger-menu.PNG','rb') as rf:
    
    with open('copy-first-names1.png','wb') as wf:
        for sater in rf:
            wf.write(sater)
            
with open('first-names.txt','r') as rf:
    
    with open('copy-first-names1.txt','w') as wf:
        for sater in rf:
            wf.write(sater)
            
        
    
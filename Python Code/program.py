
numbers4 = [140, 86, 139, 161, 175, 82, 125, 149, 135, 127, 265, 235, 132, 172, 149, 168, 212, 105, 220, 126, 90, 171, 162, 229, 121, 114, 149, 126, 129, 118, 172, 156, 216, 87, 172, 230, 162, 195, 128, 126, 142, 118, 127, 126];

numbers5 = [312, 5967, 6871, 2753, 5256, 6230, 2595, 6160, 7253,6057,6238,5507,7624,7193,6974,6362,5631,6915,6575,6490,4999,7760,6682,5689,7085,7829,6143,7272,7091,7086]

j = [];

for i in numbers5:
    
    if(i >= 6572 and i <= 7829):
        
        print(i);
        
        j.append(i);
        
print('\n');

print(len(j));
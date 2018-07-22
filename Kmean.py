a = [1,2,2,4,5,6,6,7,8,10,10,11,11,12,13,13,13]
k = 3  
c_k = [1,2,3]
distance = [0,0,0]

def step2_3(a,c_k):
    k0 = []
    k1 = []
    k2 = []
    for x in a :
        distance[0] = abs(x - c_k[0])
        distance[1] = abs(x - c_k[1])
        distance[2] = abs(x - c_k[2])
        min_value = min(distance)
        inx = distance.index(min_value)
        if inx == 0:
            k0.append(x)
        if inx == 1:
            k1.append(x)
        if inx == 2:
            k2.append(x)
    c_k[0] = sum(k0)/len(k0)
    c_k[1] = sum(k1)/len(k1)
    c_k[2] = sum(k2)/len(k2)
    
    print(k0,k1,k2)
    c_k_updated = c_k
    return c_k_updated
#----------------------------------------
centroid= []
centroid.append(c_k)
y= [centroid[0][0],centroid[0][1],centroid[0][2]]
x= step2_3(a,y)
centroid.append(x)
n=1
while centroid[n] != centroid[n-1] :
    y= [centroid[n][0],centroid[n][1],centroid[n][2]]
    x= step2_3(a,y)
    centroid.append(x)
    n = n+1




    






 

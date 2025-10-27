from sklearn.neighbors import KNeighborsClassifier
X=[
    [180,7],
    [200,7.5],
    [250,8],
    [300,8.5],
    [330,9],
    [360,9.5]
]
y=[0,0,0,1,1,1]
modeL=KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)
weight=float(input("enter the weight of the fruit in grams:"))
size=float(input("enter the size of fruit in cm :"))
prediction=model.predict([[weight,size]])[0]
if prediction ==0:
    print("This is likely apple")
else:
    print("This is likely orange")

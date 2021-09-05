M=csvread('C:\Users\lesli\mediapipe-python\prueba_1.csv');
M(:,[1 2])=[];
M(:,[1:3:1405])=[];
for n=1:336
    x=M(n,1:2:936);
    y=M(n,2:2:936);
    plot(x,y,'r:+');
    drawnow;
    pause(0.3)
end
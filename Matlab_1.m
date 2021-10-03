F=csvread('C:\Users\lesli\mediapipe-python\prueba_1.csv');
I=csvread('C:\Users\lesli\mediapipe-python\prueba_2.csv');
M=xlsread('C:\Users\lesli\mediapipe-python\prueba_3.csv');
F1=F(:,1);
I1=I(:,1);
M1=M(:,1);
F(:,[1 2])=[];
F(:,[1:3:end])=[];
I(:,[1 2])=[];
I2=I;
I(:,[1:3:end])=[];
M(:,[1 2])=[];
M(:,[1:4:end])=[];
M(:,[3:3:end])=[];
f=1;
i=1;
m=1;


f_may=F1(length(F1),1);
i_may=I1(length(I1),1);
m_may=M1(length(M1),1);

N_=m_may;

if f_may>N_
    
    N_=f_may;
end
if i_may>N_
    
    N_=i_may;
end

for n=0:N_
    if  n<f_may && F1(f,1)==n 
        x_f=F(f,1:2:end);
        y_f=-F(f,2:2:end);
        f=f+1;
        plot(x_f,y_f,'.');
        hold on;
        
    end
        
    if  n<i_may && I1(i,1)==n 
        x_i=I(i,1:2:end);
        y_i=-I(i,2:2:end);
        i=i+1;
        plot(x_i,y_i,'.');
        hold on;
        for t=0:32
            if I2(i,3*t+1)==11
                if I2(i,t+4+2*(t))==12
                plot([I2(i,3*t+2) I2(i,3*t+5)],[-I2(i,3*t+3) -I2(i,3*t+6)],'r');%11 12
                hold on; 
                end
                if I2(i,t+7+2*(t))==13
                plot([I2(i,t+1+2*(t)+1) I2(i,t+1+2*(t)+7)],[-I2(i,t+1+2*(t)+2) -I2(i,t+1+2*(t)+8)],'r');%11 13
                hold on;
                    if I2(i,3*t+13)==15
                    plot([I2(i,3*t+14) I2(i,3*t+8)],[-I2(i,3*t+15) -I2(i,3*t+9)],'r');%15 13
                    hold on;         
                    end
                   
                end
            end
        end
    end
    
    if  n<m_may && M1(m,1)==n 
        x_m=M(m,1:2:end);
        y_m=-M(m,2:2:end);
        plot(x_m,y_m,'.');
        hold on;
        if M1(m+1,1)==n
            x_m2=M(m+1,1:2:end);
            y_m2=-M(m+1,2:2:end);    
            m=m+2;
            plot(x_m2,y_m2,'.');
            hold on;
        else
            m=m+1;
        end
    end
        
        axis([0 1000 -700 30])
        drawnow;
        pause(0.02);
        hold off;
end
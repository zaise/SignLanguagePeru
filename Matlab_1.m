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
szI2=(size(I2));
I2(:,szI2(1,2))=[];
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
        cons=0;
        a=1;
        A=[];
        for t=0:32
            if I2(i,3*cons+1)==t
                A(a,1)=I2(i,3*cons+2);
                A(a,2)=I2(i,3*cons+3);
                cons=cons+1;
            end
            a=a+1;
        end
        if A(12,1)~=0 && A(13,1)~=0
                plot([A(12,1) A(13,1)],[-A(12,2) -A(13,2)],'r');%11 12
                hold on; 
        end
        
        if A(12,1)~=0 && A(14,1)~=0
                plot([A(12,1) A(14,1)],[-A(12,2) -A(14,2)],'r');%11 13
                hold on; 
        end
        if A(14,1)~=0 && A(16,1)~=0
                plot([A(14,1) A(16,1)],[-A(14,2) -A(16,2)],'r');%15 13
                hold on; 
        end
        if A(15,1)~=0 && A(17,1)~=0
                plot([A(15,1) A(17,1)],[-A(15,2) -A(17,2)],'r');%15 13
                hold on; 
        end
        if A(16,1)~=0 && A(18,1)~=0
                plot([A(16,1) A(18,1)],[-A(16,2) -A(18,2)],'r');%15 13
                hold on; 
        end
        if A(13,1)~=0 && A(15,1)~=0
                plot([A(13,1) A(15,1)],[-A(13,2) -A(15,2)],'r');%15 13
                hold on; 
        end
        if A(18,1)~=0 && A(20,1)~=0
                plot([A(18,1) A(20,1)],[-A(18,2) -A(20,2)],'r');%15 13
                hold on; 
        end
        if A(20,1)~=0 && A(22,1)~=0
                plot([A(20,1) A(22,1)],[-A(22,2) -A(20,2)],'r');%15 13
                hold on; 
        end
        if A(17,1)~=0 && A(19,1)~=0
                plot([A(17,1) A(19,1)],[-A(17,2) -A(19,2)],'r');%15 13
                hold on; 
        end 
        if A(19,1)~=0 && A(21,1)~=0
                plot([A(21,1) A(19,1)],[-A(21,2) -A(19,2)],'r');%15 13
                hold on; 
        end 
        if A(12,1)~=0 && A(24,1)~=0
                plot([A(12,1) A(24,1)],[-A(12,2) -A(24,2)],'r');%15 13
                hold on; 
        end 
        if A(13,1)~=0 && A(25,1)~=0
                plot([A(13,1) A(25,1)],[-A(13,2) -A(25,2)],'r');%15 13
                hold on; 
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

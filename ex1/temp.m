data = load ('ex1data1.txt');
x=data(:,1);
y=data(:,2);
m=length(y);%number of traning examples
plot(x,y,'bx','MarkerSize',10);
ylabel('profit in $10,000s');
xlabel('Population of City in 10,000s');
X=[ones(m,1),data(:,1)];
theta=zeros(2,1);  %initializes fitting parameters
iterations=1500;   
alpha =0.01;       %learning rate
size(X)
m = length(y); % number of training examples

J = 0;
h=X*h;
J=h-y;
J=J.*J
J=sum(J)/(2*m)


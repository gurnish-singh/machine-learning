function J = computeCost(X, y, theta)

m = length(y); % number of training examples

J = 0;



J = 0;
h=theta'*X';
J=h'-y;
J=J.*J;
J=sum(J)/(2*m);
end
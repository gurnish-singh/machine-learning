function [J, grad] = costFunction(theta, X, y)

m = length(y);
J = 0;
h = sigmoid(X*theta);
J=sum(-y.*log(h)-(1-y).*log(1-h))/m;

grad = zeros(size(theta));
for i=1:m 
grad =grad + (h(i)-y(i))*X(i,:)';
end
grad=grad/m;

end

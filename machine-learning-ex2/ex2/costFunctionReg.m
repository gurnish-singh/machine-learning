function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples
h = sigmoid(X*theta);
t=theta;
t(1)=0;
J = 0;
J=sum(-y.*log(h)-(1-y).*log(1-h))/m +lambda*(sum(t.^2))/(2*m);
grad = zeros(size(theta));
grad=(X'*(h-y))/m +(lambda/m)*t; % that's genius :-)
end

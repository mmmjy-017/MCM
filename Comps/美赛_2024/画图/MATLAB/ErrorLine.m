T_sim = RM1;
T_test = point_victor;
N = size(T_sim,1);

%相对误差error
error = abs(T_sim - T_test)./T_test;
 
%决定系数R^2
R2 = (N * sum(T_sim .* T_test) - sum(T_sim) * sum(T_test))^2 / ((N * sum((T_sim).^2) - (sum(T_sim))^2) * (N * sum((T_test).^2) - (sum(T_test))^2)); 
 
%结果对比
result = [T_test' T_sim' error']
%绘图
figure
plot(1:N,T_test,'b-o',1:N,T_sim,'r:*')
legend('Actual Price','Predicted Price')
xlabel('Test Set')
ylabel('Price')
string = {'Visualization of Results Comparison For Catamaran Sailboats';['R^2=' num2str(R2)]};
title(string)
j = 0;
for i=1:30
    err=error(1,i)
    if (err>0.3 && err~=Inf)
        j=j+1;
    end
end
rate = (30-j)/30
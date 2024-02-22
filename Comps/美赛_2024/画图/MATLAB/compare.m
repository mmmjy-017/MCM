%% 绘制预测值和真实值的对比
N = size(a,1);% 样本个数
yz = y0;% 真实值
yc = y1;% 预测值    
%计算R方
R2 = (N*sum(yc.*yz)-sum(yc)*sum(yz))^2/((N*sum((yc).^2)-(sum(yc))^2)*(N*sum((yz).^2)-(sum(yz))^2)); 
figure
plot(1:N,yz,'b:*',1:N,yc,'r-o')
legend('真实值','预测值','location','best')
xlabel('预测样本')
ylabel('值')
string = {'因变量预测结果对比';['R^2=' num2str(R2)]};
title(string)

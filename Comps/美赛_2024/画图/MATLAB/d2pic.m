%% 线图
 x = 0: 0.05 : 30; % 从0开始，步长0.05，到30结束
 y = sin(x)
 plot(x, y, 'Linewidth', 2)   
 xlabel("横坐标")
 ylabel("纵坐标")
 grid on
 axis([0 20 -1.5 1.5]) % x始 x终 y始 y终

%% 多组函数显示在一张图
y1 = sin(x)
y2 = cos(x)
plot(x, y1, x, y2)
axis([0 20 -1.5 1.5])

%% 条形图
t = -3:0.5:3;
p = exp(-t.*t); % e的-t的平方
bar(t, p)
barh(t, p)  % 转90°

%% 极坐标图
theta = 0:0.01: 2*pi;
radi = abs(sin(7*theta).*cos(10*theta)); % 点乘不是矩阵运算
polarplot(theta, radi)

%% 散点图
Height = randn(1000, 1); % 1000个数字符合正态分布
Weight = randn(1000, 1);
scatter(Height, Weight)
xlabel = ("Weight")
ylabel = ("Height")
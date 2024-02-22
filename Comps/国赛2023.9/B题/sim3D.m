method_fit = 'natural';

xxx = xxx*1852;
yyy = yyy*1852;
%插值生成网格化数据

[XX,YY,Z]=griddata(xxx,yyy,zzz,linspace(min(xxx),max(xxx))',linspace(min(yyy),max(yyy)),method_fit);
%[X,Y,C]=griddata(x,y,c,linspace(min(x),max(x))',linspace(min(y),max(y)),method_fit);
figure('color',[1 1 1]);
mesh(XX,YY,Z); % 三维曲面


zlabel('Z轴');
title('三维数值拟合曲线');
colormap("parula");
colorbar;
h = colorbar;%右侧颜色栏
set(get(h,'label'),'string','z值');%给右侧颜色栏命名
grid on;
%hold on;
%用来调整三维视角角度
view(157,11);

contour(XX,YY,Z);
xlabel('X轴');
ylabel('Y轴');

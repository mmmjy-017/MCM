%% 生成颜色柱
figure('color',[1 1 1]);
color1 = [0 176 240]./255; % 第一种颜色
color2 = [226 240 217]./255;% 第二种颜色
n=64;% 颜色数据点
R1 =(linspace(color1(1),color2(1),n))';
G1 =(linspace(color1(2),color2(2),n))';
B1 =(linspace(color1(3),color2(3),n))';
mycolor2 = [R1,G1,B1];
colormap(mycolor2);
c= colorbar;
save mycolor2
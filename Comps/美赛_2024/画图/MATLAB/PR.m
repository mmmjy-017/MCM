close all;
clear;
clc;
%% 数据
 
%% 画图ROC
% x=0:0.01:1;
% y=x;
% plot(x,y,'k--');
% hold on;
% theta=pi/2:0.01:pi; 
% X=1+1*cos(theta); 
% Y=0+1*sin(theta);  
% plot(X,Y); 
% xlim([0 1])
% %axis([0 1 0 1])
% text(0.4,0.8,' \leftarrow ROC曲线');%对曲线进行文字标注
% xlabel('False Positive Rate');
% ylabel('True Positive Rate');
% hold off;
%% 画PR曲线
x=0:0.01:1;
y=x;
plot(x,y,'k--');
hold on;
theta=0:0.01:pi/2; 
X=0+1*cos(theta); 
Y=0+1*sin(theta);  
plot(X,Y); 
xlim([0 1])
%axis([0 1 0 1])
text(0.55,0.85,' \leftarrow PR曲线');%对曲线进行文字标注
scatter(0.71,0.71,200,'k.');%第三是点的大小，后面是颜色和形状bgrcmykw
text(0.71,0.71,' \leftarrow 平衡点');%对曲线进行文字标注
hold on;
% 画某点到XY轴的垂线！！
x0=0.71;y0=0.71;  %曲线上的一点
hold on;        %在画完函数虚线之后保持曲线图
plot([0 x0],[y0 y0],'r--'); %画两个虚线
plot([x0 x0],[0 y0],'r--');
hold off;
xlabel('查全率');
ylabel('查准率');
box off;%去掉坐标轴上面和右边边框
hold off;
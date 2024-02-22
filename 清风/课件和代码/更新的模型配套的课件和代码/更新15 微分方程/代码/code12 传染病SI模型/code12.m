%% 最简单的SI模型
%% 直接求解析解求不出来
dsolve('Dx1=-0.1*x1*x2/1000','Dx2=0.1*x1*x2/1000','x1(0)=999,x2(0)=1','t')

%% 根据S+I=N的关系，消去一个变量后就可以求出来了
x1 = dsolve('Dx1=-0.1*x1*(1000-x1)/1000','x1(0)=999','t')  % S的数量
x2 = 1000-x1  % I的数量
figure(1)
fplot(x1,[1,200],'r')
hold on
fplot(x2,[1,200],'b')
legend('易感染者S','患者I')

%% 为了和后面更加复杂的模型的求解统一，我们这里就求数值解
clc;clear
global TOTAL_N   % 定义总人数为全局变量（可以在子函数中使用）
TOTAL_N = 1000;  % 总人数
i0 = 1; % 初始时刻患者（已感染者）的人数
[t,x]=ode45('fun1',[1:200],[TOTAL_N-i0 i0]); 
x = round(x);  % 可以对x进行四舍五入(人数为整数)
% % 注意：四舍五入后人口数加起来可能不等于总人数了，但这个误差可以忽略。
figure(1)
 % x的第一列是易感染者S的数量，x的第二列是患者I的数量
plot(t,x(:,1),'r-',t,x(:,2),'b-','Linewidth',1.5)  % 线的宽度设置为1.5
legend('易感染者S','患者I')

%% 考虑某种使得参数beta降低的因素（例如禁止大规模聚会、采取隔离措施等）
% 第60期后禁止大规模聚会，使得传染强度beta缩小为原来的10倍
clc;clear
global TOTAL_N   % 定义总人数为全局变量（可以在子函数中使用）
TOTAL_N = 1000;  % 总人数
i0 = 1; % 初始时刻患者（已感染者）的人数
[t,x]=ode45('fun2',[1:200],[TOTAL_N-i0 i0]); 
x = round(x);  % 对x进行四舍五入(人数为整数)
figure(2)
plot(t,x(:,1),'r-',t,x(:,2),'b-','Linewidth',1.5)  % x的第一列是易感染者S的数量，x的第二列是患者I的数量
legend('易感染者S','患者I')

% 考虑1000期
[t,x]=ode45('fun2',[1:1000],[TOTAL_N-i0 i0]); 
x = round(x);  % 对x进行四舍五入(人数为整数)
figure(3)
plot(t,x(:,1),'r-',t,x(:,2),'b-','Linewidth',1.5)  % x的第一列是易感染者S的数量，x的第二列是患者I的数量
legend('易感染者S','患者I')

% 两张图画到一起
[t,x1]=ode45('fun1',[1:500],[TOTAL_N-i0 i0]);   % 原来调用fun1，返回x1
[t,x2]=ode45('fun2',[1:500],[TOTAL_N-i0 i0]);   % 禁止大规模聚会后调用fun2，返回x2
figure(4)
plot(t,x1(:,1),'r-',t,x1(:,2),'b-','Linewidth',1.5)  
hold on  % 接着在上面那个图形上面画图
plot(t,x2(:,1),'r--',t,x2(:,2),'b--','Linewidth',1.5)   % 两个小横线--表示绘制的为虚线
axis([0 500 0 1000])  % 设置坐标轴范围，x轴为0-500 y轴为0-1000
legend('原来S','原来I','现在S','现在I')  % 在图中可以手动拖动图例的位置


%% 增加人口自然出生率和死亡率，但不考虑疾病的死亡率
clc;clear
TOTAL_N = 1000;  % 总人数
i0 = 1; % 初始时刻患者（已感染者）的人数
[t,x]=ode45('fun3',[1:200],[TOTAL_N-i0 i0 0]);  % 别忘了给ND初始值0
x = round(x);  % 对x进行四舍五入(人数为整数)
figure(5)
% x的第一列是易感染者S的数量，x的第二列是患者I的数量, x的第三列是自然死亡人数ND
plot(t,x(:,1),'r-',t,x(:,2),'b-',t,x(:,3),'k-','Linewidth',1.5)   
legend('易感染者S','患者I','自然死亡人数ND')

%% 不考虑人口自然出生率和死亡率，只考虑疾病的死亡率
clc;clear
TOTAL_N = 1000;  % 总人数
i0 = 1; % 初始时刻患者（已感染者）的人数
[t,x]=ode45('fun4',[1:500],[TOTAL_N-i0 i0 0]);  % 别忘了给ID初始值0
x = round(x);  % 对x进行四舍五入(人数为整数)
figure(6)
% x的第一列是易感染者S的数量，x的第二列是患者I的数量, x的第三列是患病死亡人数ID
plot(t,x(:,1),'r-',t,x(:,2),'b-',t,x(:,3),'k-','Linewidth',1.5)   
legend('易感染者S','患者I','患病死亡人数ID')

%% 同时考虑人口自然出生率和死亡率和疾病的死亡率
clc;clear
TOTAL_N = 1000;  % 总人数
i0 = 1; % 初始时刻患者（已感染者）的人数
[t,x]=ode45('fun5',[1:500],[TOTAL_N-i0 i0 0 0]);  % 别忘了给ID和ND的初始值都为0
x = round(x);  % 对x进行四舍五入(人数为整数)
figure(7)
% x的第一列是易感染者S的数量，x的第二列是患者I的数量
% x的第三列是患病死亡人数ID  ，x的第四列是自然死亡人数ND
plot(t,x(:,1),'r-',t,x(:,2),'b-',t,x(:,3),'k-',t,x(:,4),'g-','Linewidth',1.5)  
legend('易感染者S','患者I','患病死亡人数ID','自然死亡人数ND')



% % 注意：代码文件仅供参考，一定不要直接用于自己的数模论文中
% % 国赛对于论文的查重要求非常严格，代码雷同也算作抄袭
% % 视频中提到的附件可在售后群（购买后收到的那个无忧自动发货的短信中有加入方式）的群文件中下载。包括讲义、代码、我视频中推荐的资料等。
% % 关注我的微信公众号《数学建模学习交流》，后台发送“软件”两个字，可获得常见的建模软件下载方法；发送“数据”两个字，可获得建模数据的获取方法；发送“画图”两个字，可获得数学建模中常见的画图方法。另外，也可以看看公众号的历史文章，里面发布的都是对大家有帮助的技巧。
% % 购买更多优质精选的数学建模资料，可关注我的微信公众号《数学建模学习交流》，在后台发送“买”这个字即可进入店铺(我的微店地址：https://weidian.com/?userid=1372657210)进行购买。
% % 视频价格不贵，但价值很高。单人购买观看只需要58元，三人购买人均仅需46元，视频本身也是下载到本地观看的，所以请大家不要侵犯知识产权，对视频或者资料进行二次销售。
% % 如何修改代码避免查重的方法：https://www.bilibili.com/video/av59423231（必看）





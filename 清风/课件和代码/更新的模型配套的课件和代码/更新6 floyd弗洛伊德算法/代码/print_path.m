function [] = print_path(path,dist,i,j)
%% 该函数的作用是打印从i到j经过的最短路径
% 输入：
%        path是使用floyd算法求出来的路径矩阵
%        dist是使用floyd算法求出来的最短距离矩阵
%        i是起始节点的编号
%        j是终点节点的编号
% 输出：无

if i == j
    warning('起点和终点相同，请检查后重新输入')  % 在屏幕中提示警告信息
    return;  % 不运行下面的语句，直接退出函数
end
if path(i,j) == j   % 如果path(i,j) = j，则有两种可能：
% （1）如果dist(i,j) 为 Inf , 则说明从i到j没有路径可以到达
    if dist(i,j) == Inf
        disp(['从',num2str(i),'到',num2str(j),'没有路径可以到达'])
% （2）如果dist(i,j) 不为 Inf , 则说明从i到j可直接到达，且为最短路径
    else
        disp(['从',num2str(i),'到',num2str(j),'的最短路径为'])
        disp([num2str(i),' ---> ',num2str(j)])
        disp(['最短距离为',num2str(dist(i,j))])
    end
else  % 如果path(i,j) ~= j，则说明中间经过了其他节点：
    k = path(i,j);
    result = [num2str(i),' ---> '];  % 初始化要打印的这个字符串
    while k ~= j  % 只要k不等于j, 就一直循环下去
        result = [result , num2str(k) , ' ---> ' ];  % i先走到k这个节点处
        k = path(k,j);
    end
    result = [result , num2str(k)];
    disp(['从',num2str(i),'到',num2str(j),'的最短路径为'])
    disp(result)
    disp(['最短距离为',num2str(dist(i,j))])
end

end




% % 注意：代码文件仅供参考，一定不要直接用于自己的数模论文中
% % 国赛对于论文的查重要求非常严格，代码雷同也算作抄袭
% % 视频中提到的附件可在售后群（购买后收到的那个无忧自动发货的短信中有加入方式）的群文件中下载。包括讲义、代码、我视频中推荐的资料等。
% % 关注我的微信公众号《数学建模学习交流》，后台发送“软件”两个字，可获得常见的建模软件下载方法；发送“数据”两个字，可获得建模数据的获取方法；发送“画图”两个字，可获得数学建模中常见的画图方法。另外，也可以看看公众号的历史文章，里面发布的都是对大家有帮助的技巧。
% % 购买更多优质精选的数学建模资料，可关注我的微信公众号《数学建模学习交流》，在后台发送“买”这个字即可进入店铺(我的微店地址：https://weidian.com/?userid=1372657210)进行购买。
% % 视频价格不贵，但价值很高。单人购买观看只需要58元，三人购买人均仅需46元，视频本身也是下载到本地观看的，所以请大家不要侵犯知识产权，对视频或者资料进行二次销售。
% % 如何修改代码避免查重的方法：https://www.bilibili.com/video/av59423231（必看）
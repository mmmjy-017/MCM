%% 三维曲面图
[X, Y] = meshgrid(-2:0.1:2);
Z = X.*exp(-X.^2-Y.^2);
surf(X,Y,Z);
colormap hsv
%colormap summer
%colormap winter
colorbar

%% 子图
theta = 0:0.01: 2*pi;
radi = abs(sin(2*theta).*cos(2*theta));
Height = randn(1000, 1);
Weight = randn(1000, 1);

subplot(2,2,1); surf(X.*2); title('1st');
subplot(2,2,2); surf(Y.^3); title('2nd');

subplot(2,2,3); polarplot(theta,radi); title('3rd');
subplot(2,2,4); scatter(Height, Weight); title('4th');
% 替换为你的实际数据
predicted_labels = predict;
actual_labels = point_victor;

% 计算混淆矩阵
confusion_mat = confusionmat(actual_labels, predicted_labels);

% 提取混淆矩阵的各个元素
TP = confusion_mat(2, 2); % 真正例
FP = confusion_mat(1, 2); % 假正例
TN = confusion_mat(1, 1); % 真负例
FN = confusion_mat(2, 1); % 假负例

% 计算准确率、精确率和召回率
accuracy = (TP + TN) / (TP + FP + TN + FN);
precision = TP / (TP + FP);
recall = TP / (TP + FN);

% 打印结果
disp(['准确率：', num2str(accuracy)])
disp(['精确率：', num2str(precision)])
disp(['召回率：', num2str(recall)])

% 可视化混淆矩阵
figure;
confusionchart(confusion_mat, {'真实负例', '真实正例'}, 'RowSummary', 'row-normalized', 'ColumnSummary', 'column-normalized');
title('混淆矩阵');

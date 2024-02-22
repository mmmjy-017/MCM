import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

# 假设df是包含比赛数据的DataFrame
# 假设已经计算了实际比赛的势头得分并存储在'momentum_score'列

# 随机比赛模拟函数
def simulate_random_match(num_points, serve_win_prob=0.65):
    # 随机生成每个得分点的获胜方，发球方获胜概率较高
    wins = np.random.rand(num_points) < serve_win_prob
    momentum_scores = np.cumsum(wins)  # 累积胜点作为简化的势头得分
    return momentum_scores

# 实际比赛的势头得分
actual_momentum_scores = df['momentum_score']

# 模拟N次随机比赛
N = 1000
simulated_scores = [simulate_random_match(len(actual_momentum_scores)) for _ in range(N)]

# 统计检验
# 比较实际势头得分与模拟得分的分布差异
# 这里使用Kolmogorov-Smirnov test作为示例
ks_stat, p_value = stats.ks_2samp(actual_momentum_scores, np.concatenate(simulated_scores))

print(f"KS statistic: {ks_stat}, P-value: {p_value}")

# 可视化实际与模拟的势头得分分布
plt.hist(actual_momentum_scores, bins=30, alpha=0.5, label='Actual')
plt.hist(np.concatenate(simulated_scores), bins=30, alpha=0.5, label='Simulated', color='red')
plt.xlabel('Momentum Score')
plt.ylabel('Frequency')
plt.legend()
plt.title('Distribution of Momentum Scores: Actual vs. Simulated')
plt.show()
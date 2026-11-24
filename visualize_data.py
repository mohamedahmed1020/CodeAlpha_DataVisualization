import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load dataset and set visual theme
df = pd.read_csv('books_dataset.csv')
sns.set_theme(style='whitegrid', palette='muted')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

# ==========================================
# CHART 1: Book Price Distribution (Histogram + KDE)
# ==========================================
plt.figure(figsize=(10, 6))
sns.histplot(df['Price_GBP'], bins=15, kde=True, color='#2b5c8f', edgecolor='black')
mean_price = df['Price_GBP'].mean()
plt.axvline(mean_price, color='#d9534f', linestyle='--', linewidth=2, label=f'Mean Price: £{mean_price:.2f}')
plt.title('Distribution of Book Prices (£)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Price (£ GBP)', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('1_price_distribution.png', dpi=300)
plt.close()

# ==========================================
# CHART 2: Customer Star Rating Breakdown (Count Plot)
# ==========================================
plt.figure(figsize=(9, 6))
ax = sns.countplot(data=df, x='Rating', hue='Rating', palette='viridis', legend=False)
plt.title('Book Count by Star Rating (1 to 5 Stars)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Star Rating', fontsize=12)
plt.ylabel('Number of Books', fontsize=12)

# Add data labels on top of bars
for p in ax.patches:
    count = int(p.get_height())
    percentage = f'{100 * count / len(df):.1f}%'
    ax.annotate(f'{count}\n({percentage})',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.ylim(0, df['Rating'].value_counts().max() * 1.15)
plt.tight_layout()
plt.savefig('2_rating_distribution.png', dpi=300)
plt.close()

# ==========================================
# CHART 3: Price Spread Across Ratings (Boxplot)
# ==========================================
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Rating', y='Price_GBP', hue='Rating', palette='coolwarm', legend=False)
plt.title('Price Distribution Across Different Star Ratings', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Star Rating', fontsize=12)
plt.ylabel('Price (£ GBP)', fontsize=12)
plt.tight_layout()
plt.savefig('3_price_vs_rating_boxplot.png', dpi=300)
plt.close()

# ==========================================
# CHART 4: Top 10 Most Expensive Books
# ==========================================
top_10 = df.nlargest(10, 'Price_GBP').copy()
# Shorten very long titles for clean plotting
top_10['Short_Title'] = top_10['Title'].apply(lambda x: x[:35] + '...' if len(x) > 35 else x)

plt.figure(figsize=(11, 6))
sns.barplot(data=top_10, x='Price_GBP', y='Short_Title', hue='Rating', palette='flare', dodge=False)
plt.title('Top 10 Most Expensive Books (Colored by Rating)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Price (£ GBP)', fontsize=12)
plt.ylabel('Book Title', fontsize=12)
plt.legend(title='Star Rating', loc='lower right')
plt.tight_layout()
plt.savefig('4_top_10_expensive_books.png', dpi=300)
plt.close()

# ==========================================
# COMBINED EXECUTIVE DASHBOARD (2x2 Grid)
# ==========================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Books Catalog Analytics Dashboard - CodeAlpha Internship', fontsize=18, fontweight='bold', y=0.98)

# Subplot 1: Price Distribution
sns.histplot(df['Price_GBP'], bins=15, kde=True, color='#2b5c8f', ax=axes[0, 0])
axes[0, 0].axvline(mean_price, color='#d9534f', linestyle='--', linewidth=2, label=f'Mean: £{mean_price:.2f}')
axes[0, 0].set_title('1. Price Distribution (£)', fontsize=13, fontweight='bold')
axes[0, 0].set_xlabel('Price (£)')
axes[0, 0].legend()

# Subplot 2: Rating Counts
sns.countplot(data=df, x='Rating', hue='Rating', palette='viridis', legend=False, ax=axes[0, 1])
axes[0, 1].set_title('2. Star Rating Frequency', fontsize=13, fontweight='bold')
axes[0, 1].set_xlabel('Star Rating')

# Subplot 3: Boxplot Price vs Rating
sns.boxplot(data=df, x='Rating', y='Price_GBP', hue='Rating', palette='coolwarm', legend=False, ax=axes[1, 0])
axes[1, 0].set_title('3. Price Spread by Rating Tier', fontsize=13, fontweight='bold')
axes[1, 0].set_xlabel('Star Rating')
axes[1, 0].set_ylabel('Price (£)')

# Subplot 4: Top 5 Expensive Books
top_5 = top_10.head(5)
sns.barplot(data=top_5, x='Price_GBP', y='Short_Title', hue='Rating', palette='flare', dodge=False, ax=axes[1, 1])
axes[1, 1].set_title('4. Top 5 Highest-Priced Books', fontsize=13, fontweight='bold')
axes[1, 1].set_xlabel('Price (£)')
axes[1, 1].set_ylabel('')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('books_analytics_dashboard.png', dpi=300)
plt.close()

print('All visualizations and the combined dashboard have been saved successfully!')
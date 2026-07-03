import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_metrics_chart(user_n, user_p, user_k):
    # Load the agricultural data
    df = pd.read_csv('Crop_recommendation.csv')
    
    # Filter out data specifically for Mangoes
    mango_data = df[df['label'] == 'mango']
    
    # Calculate the average metrics that optimal mangoes need
    avg_n = mango_data['N'].mean()
    avg_p = mango_data['P'].mean()
    avg_k = mango_data['K'].mean()
    
    # Set style up
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 5))
    
    categories = ['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)']
    optimal_values = [avg_n, avg_p, avg_k]
    current_values = [user_n, user_p, user_k]
    
    # Create a clean side-by-side comparison bar chart
    x_axis = range(len(categories))
    
    ax.bar([x - 0.2 for x in x_axis], optimal_values, width=0.4, label='Optimal for Mango', color='#2e7d32')
    ax.bar([x + 0.2 for x in x_axis], current_values, width=0.4, label='Your Soil Metrics', color='#ffb300')
    
    ax.set_xticks(x_axis)
    ax.set_xticklabels(categories)
    ax.set_ylabel('Nutrient Value (mg/kg)')
    ax.set_title('Your Soil NPK vs. Optimal Mango Requirements')
    ax.legend()
    
    # Save the chart safely inside your website's static folder
    plt.tight_layout()
    plt.savefig('static/metrics_chart.png')
    plt.close()
    print("Success! Comparison chart saved to static/metrics_chart.png")

if __name__ == '__main__':
    # Test it with your current mango soil inputs (N=30, P=30, K=30)
    create_metrics_chart(30, 30, 30)
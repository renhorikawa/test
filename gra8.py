import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_patient_data(csv_file, y_max=None, xlabel='Session', ylabel='Variable'):
    df = pd.read_csv(csv_file)
    sns.set_palette('Set2')
    
    num_patients = df['patient'].nunique()
    plt.figure(figsize=(8, 3 * num_patients))  

    for i, (patient, data) in enumerate(df.groupby('patient')):
        plot_patient_data_subplot(i, num_patients, patient, data, y_max, xlabel, ylabel)

    plt.tight_layout()
    plt.show()

def plot_patient_data_subplot(i, num_patients, patient, data, y_max, xlabel, ylabel):
    plt.subplot(num_patients, 1, i + 1)
    sns.lineplot(data=data, x='session', y='variable', hue='terms', marker='o')
    
    term_a_max = data[data['terms'] == 'A']['session'].max()
    plt.axvline(x=term_a_max + 0.5, color='red', linestyle='--', label='Intervention Start')

    plt.title(patient, fontsize=13, fontweight='bold')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if y_max is not None:
        plt.ylim(0, y_max)
        
    plt.grid()
    plt.legend()

# 使用例
plot_patient_data('deta2.csv', y_max=13, xlabel='Weeks since start', ylabel='Measurement Value')



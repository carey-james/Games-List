import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# CONSTANTS
FEEDBACK_FILE = '../feedback.csv'
IMAGES_DIR = './imgs/'
SNS_STYLE = 'white'

def read_in_csv(file_path):
	df = pd.read_csv(file_path, sep='|', index_col=False, header=0)
	return df

def create_scatter(title, df, x, y, hue):
	sns.set_style(SNS_STYLE)
	ax = sns.scatterplot(data=df, x=x, y=y, hue=hue, style=hue)
	img_path = f'{IMAGES_DIR}{title}.png'
	plt.savefig(img_path)
	plt.close()
	return	img_path

def main():
	wd = create_scatter('Complexity', read_in_csv(FEEDBACK_FILE), 'mechanics_enjoyment', 'theme_enjoyment', hue='game')
	print(f'{wd} created.')

if __name__ == '__main__':
	main()
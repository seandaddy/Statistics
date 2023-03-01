import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.scatter(df['flipper_length_mm'], df['body_mass_g'])
plt.xlabel('Flipper Length(mm)')
plt.ylabel('Body Mass(g)')
plt.title('Correlation between Flipper & Body Weight')

plt.subplot(2,1,2)
plt.hist(df['body_mass_g'], bins=30)
plt.xlabel('Body Mass')
plt.ylabel('Count')
plt.title('Distribution of Penfuins Weight')

plt.subplots_adjust(left=0.1,
                    right=0.95,
                    bottom=0.1,
                    top=0.95,
                    wspace=0.5,
                    hspace=0.5)

plt.show()

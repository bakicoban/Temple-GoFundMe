
import pandas as pd

df = pd.read_csv("gofundme_scraped.csv", header=None)

col_three_list = df[df.columns[3]].tolist()

collected = []
total = []
for i in col_three_list:
    li = i.strip().split(" ")
    collected.append(''.join(c for c in li[0] if c.isdigit()))
    total.append(''.join(c for c in li[-2] if c.isdigit()))


from wordcloud import WordCloud
import matplotlib.pyplot as plt

col_one_list = df[df.columns[1]].tolist()
text = " ".join(col_one_list)
text = text.replace("Read more", "")
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

passed = ""
failed = ""
for i in range(1000):
    if collected >= total:
        passed += col_one_list[i] + " "
    else:
        failed += col_one_list[i] + " "

wordcloud = WordCloud().generate(failed)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
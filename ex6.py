import jieba
import wordcloud

f = open("wordcloud.txt","r",encoding="gbk")

t = f.read()
f.close()
ls = jieba.lcut(t)


txt = "".join(ls)
w = wordcloud.WordCloud(width = 1000,height = 700,background_color = "white",font_path="simsun.ttc")
w.generate(txt)
w.to_file("growordcloud.png")

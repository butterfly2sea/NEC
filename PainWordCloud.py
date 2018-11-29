from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np
import jieba
from utils.GetContent import get_music_comments
import time

# 分词
def trans_CN(text):
    word_list = jieba.cut(text)
    result = " ".join(word_list)
    return result

def pain_word_cloud(
        word_string,
        scale=3,
        stopword_set=None,
        mask=None,
        font_path="C:\Windows\Fonts\STXINGKA.TTF",
        randowm_state=42,
        max_font_size=40
):
    text = trans_CN(word_string)
    stopwords = set(STOPWORDS)
    stopwords.update(stopword_set)
    wordcloud = WordCloud(
        background_color='white', scale=scale, mask=mask, stopwords=stopwords, max_font_size=max_font_size,
        random_state=randowm_state, font_path=font_path
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()

def get_comments(song_id, hot=False):
    comments = get_music_comments(song_id, total='true')
    count = comments['total']
    if hot:
        pass
    else:
        result = ' '.join([i['content'] for i in comments['comments']])
        for i in range(count // 100):
            tmp = ' '.join(
                [i['content'] for i in get_music_comments(song_id, offset=(i + 1) * 100, total='true')['comments']])
            time.sleep(0.5)
            result += tmp
        return result


if __name__ == '__main__':
    words = get_comments(551816010)
    stopwords = {"大哭"}
    mask = np.array(Image.open('we.png'))
    pain_word_cloud(words, stopword_set=stopwords,font_path="C:\Windows\Fonts\hanyi.TTF")
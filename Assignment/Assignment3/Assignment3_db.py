from imdbpie import Imdb

imdb = Imdb()

for i in range(10):
    filename = 'review_{}.txt'.format(i)
    file = open(filename, 'w', encoding='utf8')
    file.write(imdb._get_reviews_data('tt1457767')[i]['text'])
    file.close()




# file_title = 'review_combined.txt'
# file = open(file_title, 'w', encoding='utf8')
# for i in range(21):
#     file.write(imdb._get_reviews_data('tt1457767')[i]['text'])
#     file.write('\n\n\n')
# file.close()
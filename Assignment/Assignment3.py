from imdbpie import Imdb

imdb = Imdb()

file = open('conjuring_review_1.txt', 'w')
file.write(imdb._get_reviews_data('tt1457767')[0]['text'])
file.close()

file = open('conjuring_review_2.txt', 'w')
file.write(imdb._get_reviews_data('tt1457767')[1]['text'])
file.close()

file = open('conjuring_review_3.txt', 'w')
file.write(imdb._get_reviews_data('tt1457767')[2]['text'])
file.close()

file = open('conjuring_review_4.txt', 'w')
file.write(imdb._get_reviews_data('tt1457767')[3]['text'])
file.close()

file = open('conjuring_review_5.txt', 'w')
file.write(imdb._get_reviews_data('tt1457767')[4]['text'])
file.close()
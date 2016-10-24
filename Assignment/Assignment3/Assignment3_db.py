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

file = open('conjuring_review_6.txt', 'w')
file.write(imdb._get_reviews_data('tt1457767')[5]['text'])
file.close()

file = open('conjuring_review_7.txt', 'w')
file.write(imdb._get_reviews_data('tt1457767')[6]['text'])
file.close()

file = open('conjuring_review_Combined.txt', 'w')
file.write(imdb._get_reviews_data('tt1457767')[0]['text'])
file.write('\n\n\n')
file.write(imdb._get_reviews_data('tt1457767')[1]['text'])
file.write('\n\n\n')
file.write(imdb._get_reviews_data('tt1457767')[2]['text'])
file.write('\n\n\n')
file.write(imdb._get_reviews_data('tt1457767')[3]['text'])
file.write('\n\n\n')
file.write(imdb._get_reviews_data('tt1457767')[4]['text'])
file.write('\n\n\n')
file.write(imdb._get_reviews_data('tt1457767')[5]['text'])
file.write('\n\n\n')
file.write(imdb._get_reviews_data('tt1457767')[6]['text'])
file.close()



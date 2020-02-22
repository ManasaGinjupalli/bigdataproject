i = open("books1.txt", "r")
o = open("01.txt", "w")

for line in i:
    datalist = line.strip().split("\t")
    BookID, title, authors, average_rating, isbn, isbn13, language_code,  num_pages, ratings_count, text_reviews_count = datalist
    o.write(authors + "\t" + average_rating  + "\n")

i.close()
o.close()




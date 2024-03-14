meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
            
word = input("Ketik kata yang tidak kamu mengerti (kapital): ")\

if word in meme_dict.keys():
    print("makna kata", word, "adalah", meme_dict[word])
else:
    print("makna kata tidak ditemukan")

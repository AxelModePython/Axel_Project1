import time
meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Memberikan reaksi terhadap sesuatu yang luarbiasa"
             }
while True:
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
        time.sleep(1)
    else:
        print("Word isn't found in the dictionary")
        time.sleep(1)

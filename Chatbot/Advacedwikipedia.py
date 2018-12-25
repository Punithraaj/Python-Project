import wikipedia
while True:
    Question = input("Question:\n")
    print(str(Question))
    print("Languages ",wikipedia.languages())
    print("Decimals: ",wikipedia.Decimal())
    print("URL ",str(wikipedia.API_URL))
    wikipedia.set_lang('en')
    print(str(wikipedia.summary(Question,sentences=2)))
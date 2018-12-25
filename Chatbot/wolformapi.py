import wolframalpha

Question = input("Q: ")
app_id = "YOUR APP ID"
client = wolframalpha.Client(app_id)

res = client.query(Question)
answer = next(res.results).text

print(answer)
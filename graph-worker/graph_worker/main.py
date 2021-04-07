import graph

test_data = [
    {"price": "122.41", "date": "2020-10-02"},
    {"price": "127.35", "date": "2020-10-03"},
    {"price": "121.11", "date": "2020-10-04"},
    {"price": "126.65", "date": "2020-10-05"},
    {"price": "123.42", "date": "2020-10-06"},
]

def main():
    img = graph.generate(data=test_data, title="Test Stock")
    print(img)

main()

from flask import Flask,render_template,request

# translate function
def translate(word):
    import requests
    API_KEY = '52309d6aa90c200fbe5f8b99465f2c93'
    API_ID = '14831ecd'

    headers = {
        "Accept": "application/json",
        "app_id": API_ID,
        "app_key": API_KEY
    }

    url = f"https://od-api.oxforddictionaries.com/api/v2/translations/en/hi/{word.lower()}?strictMatch=false&fields=translations"
    r = requests.get(url, headers=headers)
    hindi = r.json()["results"][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['translations'][0]['text']

    url2 = f"https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/{word.lower()}?fields=definitions&strictMatch=false"
    r2 = requests.get(url2, headers=headers)
    define = r2.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]

    return hindi,define


# flask framework
app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        text = request.form.get("word")
        translated=translate(text)
        return render_template('index.html', word=text, hindi=translated[0], definition=translated[1])
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
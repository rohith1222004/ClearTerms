from flask import Flask,render_template,request
from flask_cors import CORS
import openai

openai.api_key = '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'


app = Flask(__name__)
CORS(app)


@app.route('/data',methods = ['POST'])
def receive_data():
    data = request.get_json()
    name = data['data']
    completion = openai.Completion.create(
    model="davinci:ft-personal-2023-02-21-20-55-46",
    prompt=name,)
    print(completion)

    return completion




if __name__ == '__main__':
        app.run()

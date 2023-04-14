from flask import Flask,render_template,request
from flask_cors import CORS
import openai

# openai.api_key = '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'
# openai.api_key = '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'
# openai.api_key = ' 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'
openai.api_key = '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'



app = Flask(__name__)
CORS(app)

@app.route('/data',methods = ['POST'])
def receive_data():
    data = request.get_json()
    print(data)
    name = data['data']
    completion = openai.Completion.create(
    # model="davinci:ft-personal-2023-02-21-20-55-46",
    model ="davinci:ft-personal-2023-04-14-17-53-27",
    prompt=name,)
    print(completion)
    return completion

@app.route('/data/criticalTerms',methods = ['POST'])
def critical_terms_receive_data():
    data = request.get_json()
    print(data)
    name = data['data']
    completion = openai.Completion.create(
    # model="davinci:ft-personal-2023-02-21-20-55-46",
    model ="",
    prompt=name,)
    print(completion)
    return completion





if __name__ == '__main__':
        app.run(debug=True)



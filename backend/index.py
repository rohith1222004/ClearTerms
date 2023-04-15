from googletrans import Translator
from flask import Flask,render_template,request
from flask_cors import CORS
import openai

# openai.api_key = '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'
# openai.api_key = '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'
# openai.api_key = ' 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'
# openai.api_key = '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'
openai.api_key = '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'



app = Flask(__name__)
CORS(app)

translator = Translator()
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
# def critical_terms_receive_data():
#     data = request.get_json()
#     print(data)
#     name = data['data']
#     completion = openai.Completion.create(
#     # model="davinci:ft-personal-2023-02-21-20-55-46",
#     model ="davinci:ft-personal-2023-04-14-19-04-47",
#     prompt=name,)
#     print(completion)
#     original = completion.choices[0].text
#     print(original)
#     translated = translator.translate(original,dest='ta')
#     print(translated)
#     return {'original' : original,
#             'translated' : translated}
def critical_terms_receive_data():
    data = request.get_json()
    print(data)
    name = data['data']
    completion = openai.Completion.create(
        model="davinci:ft-personal-2023-04-14-19-04-47",
        prompt=name,
    )
    print(completion)
    original = completion.choices[0].text
    print(original)
    translated = translator.translate(original, dest='hi')
    print(translated.text)  # print the translated text
    return {'original': original, 'translated': translated.text}





if __name__ == '__main__':
        app.run(debug=True)



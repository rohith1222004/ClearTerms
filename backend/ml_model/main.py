from decouple import config
import openai

openai.api_key = config('OPEN_AI_API_KEY')


def listCriticalTerms(terms):
    pass

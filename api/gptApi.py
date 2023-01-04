from flask_restful import Resource, abort
from flask import request
from bson import json_util

import openai
openai.organization = "org-o99a4pdAsNg18j2N62fvItlB"
openai.api_key = "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"

import json

class GptImagesApi(Resource):

    def options(self):
        return 200
    
    def post(self):
        args = request.get_json()
        print(args)
        try:
            response = openai.Image.create(
                prompt= args["prompt"],
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
        except openai.error.OpenAIError as e:
            return e.error
        return image_url
    
from flask import Flask, request, jsonify
from flask_cors import CORS

import openai
openai.organization = "org-o99a4pdAsNg18j2N62fvItlB"
openai.api_key = "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"

app = Flask(__name__)

cors = CORS(app)


@app.route("/gptImages", methods = ["POST"])
def imageCreation():
    args = request.get_json()
    print(args)
    try:
        response = openai.Image.create(
        prompt= args["prompt"],
        n=1,
        size="256x256"
        )
        image_url = response['data'][0]['url']
    except openai.error.OpenAIError as e:
        return e.error
    return {"imageUrl": image_url}

if __name__ == "__main__":
    app.run(debug = False, port=3000)
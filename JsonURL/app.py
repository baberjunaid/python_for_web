from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    from urllib.request import urlopen

    # import json
    import json
    # store the URL in url as
    # parameter for urlopen
    url = "https://cms.mlcs.xyz/api/view/program_sessions/all/"

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
    cs_session = []
    for a in data_json:
        cs_session.append(a['Session_Title'])
    print (cs_session)
    return render_template("index.html", cs_session=cs_session)

@app.route("/session",  methods=['POST'])
def intro():
    a = request.form.get("program")
    return "You selected "  + str(a)


if __name__ == "__main__":
    app.run(debug=True)

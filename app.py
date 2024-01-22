from flask import Flask, render_template, request, send_from_directory, render_template, jsonify
import os
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app = Flask(__name__)


@app.route("/")
def index():
    uploads = os.path.join(app.root_path, app.config["UPLOAD_FOLDER"])
    files = [f for f in os.listdir(uploads) if os.path.isfile(os.path.join(uploads, f))]

    return render_template("index.html")

@app.route("/sorry")
def sorry():
    return render_template("jewgle.html")



#@app.route("/upload", methods=["POST"])
#def upload():
#    file = request.files["file"]
#    filename = file.filename
#    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
#    return "File uploaded successfully."


#@app.route("/download/<filename>")
#def download(filename):
#    uploads = os.path.join(app.root_path, app.config["UPLOAD_FOLDER"])
#    return send_from_directory(directory=uploads, path=filename)


@app.route("/chat", methods=["POST", "GET"])
def chatora():
    from llama_cpp import Llama
    chat = request.form.get("chat")
    from_user = request.form.get("from_user")
    llm = Llama(model_path="/home/dumball/codellama-7b-instruct.Q2_K.gguf")
    output = llm(f"user: {chat} Assistant: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
    return jsonify(output=output['choices'][0]['text'])



@app.route('/name')
def method_name():
    name = "allah"
    return render_template('niga.html',name=name)



@app.route('/upload'):
def upload():
    

@app.route('/play'):



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


#@app.route("/rename/<img>", methods=["POST"])
#def rename(img):
#    import predict_step from renamefiles
#    predict_step



@app.route('/watch')
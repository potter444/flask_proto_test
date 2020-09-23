from flask import Flask,render_template,request,url_for,redirect
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    else:
        ip = request.form.get("login_ip")
        account = request.form.get("account")
        print(ip, account)
        return redirect(url_for("proto_test"))


@app.route("/proto/", methods=["GET","POST"])
def proto_test():
    if request.method == "GET":
        return render_template("proto.html")
    else:
        pass



if __name__ == "__main__":
    app.run()
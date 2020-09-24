from flask import Flask,render_template,request,url_for,redirect,session
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        ip = request.form.get("login_ip")
        account = request.form.get("account")
        print(ip, account)
        session["account"] = account
        session["ip"] = ip
        session.permanent = True
        return redirect(url_for("proto_test"))


@app.route("/proto/")
def proto_test():

    return render_template("proto.html", account=session.get("account"))


if __name__ == "__main__":
    app.run()
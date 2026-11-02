from flask import Flask, render_template, request, redirect, url_for, flash

from database import initialize_database, get_all_records
from deduplication import add_record

app = Flask(__name__)
app.secret_key = "codealpha-development-key"

initialize_database()


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")

        status, message = add_record(name, email)

        if status == "SUCCESS":
            flash(message, "success")
        elif status == "DUPLICATE":
            flash(message, "warning")
        else:
            flash(message, "error")

        return redirect(url_for("index"))

    records = get_all_records()

    return render_template(
        "index.html",
        records=records,
        total_records=len(records)
    )


if __name__ == "__main__":
    app.run(debug=True)

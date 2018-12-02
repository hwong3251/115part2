# {"AddedDate":"2016-09-24T21:37:43Z",
# "BreachDate":"2007-07-12",
# "DataClasses":["Dates of birth","Email addresses","Genders","IP addresses","Names","Passwords","Physical addresses","Security questions and answers","Usernames","Website activity"],
# "Description":"In July 2007, the multiplayer game portal known as <a href=\"https://web.archive.org/web/20070710161412/http://gpotato.com/\" target=\"_blank\" rel=\"noopener\">gPotato</a> (link to archive of the site at that time) suffered a data breach and over 2 million user accounts were exposed. The site later merged into the <a href=\"http://www.webzen.com/\" target=\"_blank\" rel=\"noopener\">Webzen portal</a> where the original accounts still exist today. The exposed data included usernames, email and IP addresses, MD5 hashes and personal attributes such as gender, birth date, physical address and security questions and answers stored in plain text.",
# "Domain":"gpotato.com",
# "IsFabricated":false,
# "IsRetired":false,
# "IsSensitive":false,
# "IsSpamList":false,
# "IsVerified":true,
# "LogoPath":"https://haveibeenpwned.com/Content/Images/PwnedLogos/gPotato.png",
# "ModifiedDate":"2016-09-24T21:37:43Z",
# "Name":"gPotato",
# "PwnCount":2136520,
# "Title":"gPotato"}

from flask import Flask, render_template, jsonify, redirect
import test

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/have-i-been-pwned')
def have_i_been_pwned():
    return redirect("https://haveibeenpwned.com/", code=302)


@app.route('/json', methods=['GET'])
def json():
    return jsonify(test.ten_recent_breach_site("https://haveibeenpwned.com/api/v2/breaches"))


@app.route('/h-json', methods=['GET'])
def h_json():
    return jsonify(test.get_map_data("https://haveibeenpwned.com/api/v2/breaches"))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)

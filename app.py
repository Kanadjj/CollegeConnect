
from flask import Flask, render_template, jsonify, request, session, redirect

app = Flask(__name__)

app.secret_key = "collegeconnect-demo-secret"


queries_data = []
requests_data = []


notifications = [
    {
        "title": "Mid-Semester Examination Schedule",
        "message": "The examination schedule has been published.",
        "date": "10 September 2026",
        "type": "Academic"
    },
    {
        "title": "Hackathon Registration",
        "message": "Registration for the college hackathon is open.",
        "date": "12 September 2026",
        "type": "Event"
    },
    {
        "title": "Library Timing Updated",
        "message": "The library will remain open until 8:00 PM on weekdays.",
        "date": "15 September 2026",
        "type": "Administration"
    }
]


announcements = [
    {
        "title": "Mid-Semester Examination Schedule",
        "category": "Academic",
        "date": "10 September 2026",
        "description": "The mid-semester examination schedule has been published."
    },
    {
        "title": "Hackathon Registration",
        "category": "Events",
        "date": "12 September 2026",
        "description": "Students interested in participating in the college hackathon can register before the deadline."
    },
    {
        "title": "Library Timing Updated",
        "category": "Administration",
        "date": "15 September 2026",
        "description": "The library will remain open until 8:00 PM on weekdays."
    }
]


events = [
    {
        "day": "15",
        "month": "SEP",
        "title": "Mid-Semester Examination",
        "type": "EXAM",
        "description": "Mid-semester examinations begin."
    },
    {
        "day": "18",
        "month": "SEP",
        "title": "College Hackathon",
        "type": "EVENT",
        "description": "Internal college hackathon for participating students."
    },
    {
        "day": "22",
        "month": "SEP",
        "title": "PCE Assignment Submission",
        "type": "DEADLINE",
        "description": "Last date for submitting the PCE assignment."
    }
]


@app.route("/")
def home():

    if not session.get("student_id"):
        return redirect("/login")

    return render_template("index.html")


@app.route("/api/announcements")
def get_announcements():

    if not session.get("student_id"):
        return redirect("/login")

    return jsonify(announcements)


@app.route("/queries")
def queries():

    if not session.get("student_id"):
        return redirect("/login")

    return render_template("queries.html")


@app.route("/api/queries", methods=["POST"])
def submit_query():

    if not session.get("student_id"):
        return redirect("/login")

    data = request.get_json()

    query_id = "CC-" + str(len(queries_data) + 1).zfill(4)

    new_query = {
        "query_id": query_id,
        "department": data["department"],
        "subject": data["subject"],
        "message": data["message"],
        "status": "Pending"
    }

    queries_data.append(new_query)

    return jsonify({
        "success": True,
        "query_id": query_id,
        "status": "Pending"
    })


@app.route("/calendar")
def calendar():

    if not session.get("student_id"):
        return redirect("/login")

    return render_template("calendar.html")


@app.route("/api/events")
def get_events():

    if not session.get("student_id"):
        return redirect("/login")

    return jsonify(events)


@app.route("/requests")
def requests():

    if not session.get("student_id"):
        return redirect("/login")

    return render_template("requests.html")


@app.route("/api/requests", methods=["POST"])
def submit_request():

    if not session.get("student_id"):
        return redirect("/login")

    data = request.get_json()

    request_id = "REQ-" + str(len(requests_data) + 1).zfill(4)

    new_request = {
        "request_id": request_id,
        "type": data["type"],
        "department": data["department"],
        "description": data["description"],
        "status": "Pending"
    }

    requests_data.append(new_request)

    return jsonify({
        "success": True,
        "request_id": request_id,
        "status": "Pending"
    })


@app.route("/dashboard")
def dashboard():

    student_id = session.get("student_id")

    if not student_id:
        return redirect("/login")

    student = {
        "student_id": student_id,
        "name": "Kanad Joshi",
        "course": "Computer Science",
        "year": "Second Year",
        "division": "A"
    }

    return render_template(
        "dashboard.html",
        student=student,
        queries=queries_data,
        requests=requests_data
    )


@app.route("/api/notifications")
def get_notifications():

    if not session.get("student_id"):
        return redirect("/login")

    return jsonify(notifications)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        student_id = request.form["student_id"]
        password = request.form["password"]

        if student_id == "CS2026001" and password == "student123":

            session["student_id"] = student_id

            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Invalid Student ID or password."
        )

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)

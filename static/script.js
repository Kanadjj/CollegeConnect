document.addEventListener("DOMContentLoaded", function () {
    loadAnnouncements();
    loadEvents();
    loadNotifications();
});


function loadAnnouncements() {

    fetch("/api/announcements")
        .then(response => response.json())
        .then(data => {

            const announcementList =
                document.getElementById("announcement-list");

            announcementList.innerHTML = "";

            data.forEach(announcement => {

                const card = document.createElement("div");

                card.className = "announcement-card";

                card.innerHTML = `
                    <div class="announcement-top">
                        <span class="category">
                            ${announcement.category}
                        </span>

                        <span class="date">
                            ${announcement.date}
                        </span>
                    </div>

                    <h3>${announcement.title}</h3>

                    <p>${announcement.description}</p>
                `;

                announcementList.appendChild(card);
            });
        })
        .catch(error => {
            console.error("Error loading announcements:", error);
        });
}
const queryForm = document.getElementById("query-form");

if (queryForm) {

    queryForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const department =
            document.getElementById("department").value;

        const subject =
            document.getElementById("subject").value;

        const message =
            document.getElementById("message").value;


        fetch("/api/queries", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                department: department,
                subject: subject,
                message: message
            })

        })

        .then(response => response.json())

        .then(data => {

            const result =
                document.getElementById("query-result");

            result.style.display = "block";

            result.innerHTML = `
                <h3>Query Submitted Successfully!</h3>

                <p>
                    Your tracking ID is:
                    <span class="query-id">
                        ${data.query_id}
                    </span>
                </p>

                <p>
                    Status:
                    <strong>${data.status}</strong>
                </p>

                <p>
                    You can use this ID to track your query.
                </p>
            `;

            queryForm.reset();

        })

        .catch(error => {

            console.error("Error:", error);

            alert("Unable to submit query.");

        });

    });
}
function loadEvents() {

    fetch("/api/events")
        .then(response => response.json())
        .then(data => {

            const eventsList =
                document.getElementById("events-list");

            if (!eventsList) {
                return;
            }

            eventsList.innerHTML = "";

            data.forEach(event => {

                const card = document.createElement("div");

                card.className = "event-card";

                card.innerHTML = `
                    <div class="event-date">
                        <strong>${event.day}</strong>
                        <span>${event.month}</span>
                    </div>

                    <div class="event-info">

                        <span class="event-type">
                            ${event.type}
                        </span>

                        <h3>${event.title}</h3>

                        <p>${event.description}</p>

                    </div>
                `;

                eventsList.appendChild(card);
            });

        })
        .catch(error => {
            console.error("Error loading events:", error);
        });
}


const requestForm = document.getElementById("request-form");

if (requestForm) {

    requestForm.addEventListener("submit", function(event) {

        event.preventDefault();

        const type =
            document.getElementById("request-type").value;

        const department =
            document.getElementById("request-department").value;

        const description =
            document.getElementById("request-description").value;


        fetch("/api/requests", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                type: type,
                department: department,
                description: description
            })

        })

        .then(response => response.json())

        .then(data => {

            const result =
                document.getElementById("request-result");

            result.style.display = "block";

            result.innerHTML = `
                <h3>Request Submitted Successfully!</h3>

                <p>
                    Your tracking ID:
                    <span class="query-id">
                        ${data.request_id}
                    </span>
                </p>

                <p>
                    Status:
                    <strong>${data.status}</strong>
                </p>

                <p>
                    The concerned department can process
                    your request using this tracking ID.
                </p>
            `;

            requestForm.reset();

        })

        .catch(error => {

            console.error("Error:", error);

            alert("Unable to submit request.");

        });

    });
}

function loadNotifications() {

    fetch("/api/notifications")
        .then(response => response.json())
        .then(data => {

            const notificationList =
                document.getElementById("notification-list");

            if (!notificationList) {
                return;
            }

            notificationList.innerHTML = "";

            data.forEach(notification => {

                const item = document.createElement("div");

                item.className = "notification-item";

                item.innerHTML = `
                    <div>
                        <strong>${notification.title}</strong>
                        <p>${notification.message}</p>
                    </div>

                    <span>${notification.date}</span>
                `;

                notificationList.appendChild(item);
            });
        })
        .catch(error => {
            console.error("Error loading notifications:", error);
        });
}


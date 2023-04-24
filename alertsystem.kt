// Define an Incident class to store incident details
data class Incident(val id: Int, val title: String, val description: String)

// Define a function to send alerts
fun sendAlert(incident: Incident) {
    // Code to send alert (e.g. email, SMS, push notification)
    println("ALERT: Incident ${incident.id} - ${incident.title}")
}

// Define a list of incidents
val incidents = listOf(
    Incident(1, "Server down", "The server is not responding."),
    Incident(2, "Network outage", "The network is experiencing disruptions."),
    Incident(3, "Database error", "There is a problem with the database."),
)

// Loop through the incidents and send alerts for any that meet the criteria
for (incident in incidents) {
    if (incident.title.contains("down") || incident.title.contains("error")) {
        sendAlert(incident)
    }
}

import requests

# Azure Notification Hub Configuration
NOTIFICATION_HUB_NAME = "<Your_Notification_Hub_Name>"
CONNECTION_STRING = "<Your_Full_Connection_String>"

# Notification Hub Endpoint
API_VERSION = "2015-01"
URL = f"https://{NOTIFICATION_HUB_NAME}.servicebus.windows.net/{NOTIFICATION_HUB_NAME}/messages/?api-version={API_VERSION}"

# Notification Content
def create_notification_payload(title, message):
    """Create the notification payload."""
    return {
        "title": title,
        "body": message,
    }

def send_notification_to_driver(driver_id, title, message):
    """
    Send a push notification to the driver.
    
    Args:
        driver_id (str): Driver ID or tag used to identify the driver.
        title (str): Notification title.
        message (str): Notification message.
    """
    headers = {
        "Authorization": generate_sas_token(CONNECTION_STRING, NOTIFICATION_HUB_NAME),
        "Content-Type": "application/json",
        "ServiceBusNotification-Tags": f"driver:{driver_id}",
    }
    
    payload = create_notification_payload(title, message)

    response = requests.post(URL, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Notification sent successfully to driver {driver_id}")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")
        print(response.text)

def generate_sas_token(connection_string, hub_name):
    """
    Generate a Shared Access Signature (SAS) token for Azure Notification Hub.
    """
    import urllib.parse
    import hmac
    import hashlib
    import base64
    import time

    # Parse the connection string
    parts = connection_string.split(";")
    endpoint = parts[0].replace("Endpoint=", "")
    shared_access_key_name = parts[1].replace("SharedAccessKeyName=", "")
    shared_access_key = parts[2].replace("SharedAccessKey=", "")

    # Construct the token
    uri = urllib.parse.quote_plus(f"{endpoint}{hub_name}")
    expiry = str(int(time.time() + 3600))  # 1 hour expiration
    string_to_sign = f"{uri}\n{expiry}"
    signature = base64.b64encode(
        hmac.new(
            shared_access_key.encode("utf-8"),
            string_to_sign.encode("utf-8"),
            hashlib.sha256,
        ).digest()
    ).decode("utf-8")

    return f"SharedAccessSignature sr={uri}&sig={signature}&se={expiry}&skn={shared_access_key_name}"


# Example Usage
if __name__ == "__main__":
    # Example driver ID, notification title, and message
    driver_id = "driver123"
    notification_title = "Maintenance Alert"
    notification_message = "Your vehicle requires immediate maintenance. Please check the dashboard for details."

    # Send notification
    send_notification_to_driver(driver_id, notification_title, notification_message)

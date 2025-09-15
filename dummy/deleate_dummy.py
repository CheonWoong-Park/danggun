import requests

# Specify the ID of the board you want to delete
board_id = '4506d2bd-e6a7-4c26-b541-29664643050b'  # Replace with the actual board ID
url = f'http://13.124.30.115:8000/board/delete/{board_id}/'

# Send the DELETE request
response = requests.get(url)

# Check the response status
if response.status_code == 200:
    print("Board deleted successfully.")
else:
    print(f"Error: {response.status_code}, Response Text: {response.text}")

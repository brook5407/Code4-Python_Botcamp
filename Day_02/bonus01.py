from datetime import datetime
import pytz

if __name__ == "__main__":
	local_timezone = pytz.timezone('Asia/Kuala_Lumpur')
	local_time = datetime.now(local_timezone)
	print(local_time.time())

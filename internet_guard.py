import subprocess
import time
import os
import logging

ADAPTER = "Eathernet"
ADAPTER = "WI-FI"

INTERVAL = 5 * 60

OFF_DURATION = 60


logging.basicCongig(
        filename="internet_guard.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
)

def set_internet(enable: bool):
    action = "enable" if enable else "disable"
    
    command = (
        f"{action}-NetAdapter "
        f"-Name '{ADAPTER}' -Confirm:$false"
    )

    subprocess.run(["powershell", "-Command", command]
     check=True
     capture_output=True
     text=True
     )

def main():
    logging.info("Starting Internet Guard...")

    try:
        while True:
            time.sleep(INTERVAL)

            try:
                logging.info("Disabling internet...")
                set_internet(False)
                time.sleep(OFF_DURATION)

            finnally:
                set_internet(True)
                logging.info("Enabling internet...")

    except KeyboardInterrupt:
        logging.info("stoping")

    finally:
        try:
            set_internet(True)
        except Exception as e:
            logging.execption(f"Failed to enable internet: {e}")

if __name__ == "__main__":
    main()
                
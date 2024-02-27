import sys
import logging

def main():
    setup_logging()  # Added for system testing
    limits = parse_limits()
    sensor_data = []

    if len(limits) > 0 and check_limits(limits):
        sensor_data = read_sensors()
        for row in sensor_data:
            print(row)
    else:
        logging.error("Incorrect command line arguments.")  # Modified for system testing

def parse_limits():
    limits = []

    try:
        limits = [int(sys.argv[1]), int(sys.argv[2])]
    except Exception:
        pass
    
    return limits

def check_limits(limits):
    if limits[0] < limits[1]:
        return True
    else:
        return False

def read_sensors():
    return [
        [21.2, 18.2, 18.2, 22.2],
        [-5.0, -4.2, -3.9, -4.5],
        [1.2, 0.0, 0.5, -0.8, -1.0],
        [25.0, -4.2, -13.9, 4.5]
    ]

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')  # Added for system testing

if __name__ == "__main__":
    main()

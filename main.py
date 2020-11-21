from src.data_collector import DataCollector
from datetime import datetime

if __name__ == "__main__":
    # Create the DataCollector with default parameters
    my_data_collector = DataCollector()

    # Start the Data Collection
    print(f"[i] Start DataColector{datetime.now()}")
    my_data_collector.start()
    print(f"[i] Stop DataColector{datetime.now()}")

from src.data_collector import DataCollector
from datetime import datetime

if __name__ == "__main__":
    # Create the DataCollector
    my_data_collector = DataCollector()
    # Start the Data Collection
    print(datetime.now())
    print('[i] Start DataColector')
    my_data_collector.start()
    print('[i] Stop DataColector')
    print(datetime.now())

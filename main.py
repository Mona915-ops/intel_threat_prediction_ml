# main.py

from models import train_model

if __name__ == '__main__':
    print("🚀 Starting model training...")
    train_model(data_folder_path='.')

from pathlib import Path 
import pandas as pd

DATA_DIR = Path("data/raw/acl18")

def main():
    print("Dataset exists:", DATA_DIR.exists())

    price_dir = DATA_DIR / "price"
    tweet_dir = DATA_DIR / "tweet"

    print("Price directory:", price_dir.exists())
    print("Tweet directory:", tweet_dir.exists())

if __name__ == "__main__":
    main()



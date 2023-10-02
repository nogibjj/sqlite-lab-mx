"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

def main():
  if args.action =="extract":
    # Extract
      print("Extracting data...")
      extract()
  elif args.action =="transform_data":
      # Transform and load
      print("Transforming data...")
      load()
  
  elif args.action == "query":
      # Query
      print("Querying data...")
      query()
  else:
    print("unknown action")


if __name__ == "__mian__":
  main()

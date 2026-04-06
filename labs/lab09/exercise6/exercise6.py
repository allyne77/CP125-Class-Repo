import pandas as pd


def critical_inventory(filename):
    df = pd.read_csv (filename)

    total_product = len(df)
    critical_count = df[(df['StockLevel'] < df["ReorderThreshold"]) & (df['DaysSinceRestock']) >30]
    critical_product = set(df['ProductName'])

    return {
        "total_products": total_product,
        "critical_count": len(critical_count),
        "critical_products": set(critical_product)
    }

 

result = critical_inventory("labs/lab09/data/inventory.csv")
print(result)





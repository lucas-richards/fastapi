import polars as pl

df = (
    pl.read_csv("data/iris.csv")
    .filter(pl.col("sepal.length") > 5)
    # .group_by("variety")
    # .agg(pl.all().sum())
)

# df = q.collect()


print(df)
print(df.group_by("variety").agg(pl.all().sum()))
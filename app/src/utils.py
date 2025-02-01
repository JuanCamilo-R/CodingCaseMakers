import pandas as pd

def read_prompt_file(path: str):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    return content

def replace_placeholders(content: str, **kwargs):
    for key, value in kwargs.items():
        placeholder = "{{" + key + "}}"
        strval = str(value)
        content = content.replace(placeholder, strval)
    return content

def format_products(data: pd.DataFrame):
    formatted_products = []
    for _, row in data.iterrows():
        product_attributes = [
            f"Name: {row.get("name", "")}",
            f"Category: {row.get("category", "")}",
            f"Brand: {row.get("brand", "")}",
            f"Description: {row.get("description", "")}",
            f"Price: {row.get("price", "")}",
            f"Stock: {row.get("stock", "")}"
        ]
        formatted_products.append("\n".join(product_attributes))
    return "\n--------------------------\n".join(formatted_products)
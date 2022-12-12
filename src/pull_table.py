import pandas as pd
import time


def main():
    total_node_info = []
    url = r"https://www.browsenodes.com/amazon.com/browseNodeLookup/16310211.html"
    tables = pd.read_html(
        url,
    )
    table = tables[0]
    table["Parent"] = "Food"
    node_info = list(zip(table["Parent"], table["Name"], table["Id"]))
    total_node_info.extend(node_info)
    total_node_info = extract_dataframe(list(node_info), total_node_info)

    df = pd.DataFrame(total_node_info, columns=["parent", "name", "id"])
    df.to_csv("amazon_food_nodes.csv", index=False)


def extract_dataframe(node_info, total_node_info):

    for node_tuple in node_info:
        table = get_table_of_subnodes(node_tuple[2])

        if table["Id"][0] != table["Name"][0]:  # Test leaf lode
            table["Parent"] = node_tuple[1]
            new_node_info = list(zip(table["Parent"], table["Name"], table["Id"]))
            total_node_info.extend(new_node_info)
            total_node_info = extract_dataframe(list(new_node_info), total_node_info)

        else:
            continue
    return total_node_info


def get_table_of_subnodes(node):
    url = f"https://www.browsenodes.com/amazon.com/browseNodeLookup/{node}.html"
    time.sleep(0.1)
    tables = pd.read_html(
        url,
    )
    table = tables[0]
    return table


if __name__ == "__main__":
    main()

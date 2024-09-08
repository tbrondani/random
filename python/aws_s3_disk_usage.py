## Credits to : Daniel Abreu / Lucas Perin

import boto3

#baseline to work with
bucket = "insert_bucket"
prefix = "insert"


def calculate_size(size, _size_table):
    count = 0
    while size // 1024 > 0:
        size = size / 1024
        count += 1
    return f"{round(size, 2)} {_size_table[count]}"
size_table = {0: "Bs", 1: "KBs", 2: "MBs", 3: "GBs", 4: "TBs", 5: "PBs", 6: "EBs"}

s3_client = boto3.client("s3")
paginator = s3_client.get_paginator("list_object_versions")
operation_parameters = {"Bucket": bucket, "Prefix": prefix} if prefix else {"Bucket": bucket}
prefix_metrics = {}
delete_marker_count = 0
print("$ Calculating, please wait... this may take a while")
with open("resultados.txt", "w") as f:  # Abre o arquivo para escrita
    f.write("$ Calculating, please wait... this may take a while\n\n")
    for response in paginator.paginate(**operation_parameters):
        if "DeleteMarkers" in response:
            delete_marker_count += len(response["DeleteMarkers"])
        for version in response.get("Versions", []):
            key = version["Key"]
            object_size = version["Size"]
            object_prefix = key.split("/")[0] if "/" in key else ""
            metrics = prefix_metrics.setdefault(object_prefix, {
                "delete_marker_count": 0,
                "current_object_count": 0,
                "current_object_size": 0,
                "versioned_object_count": 0,
                "versioned_object_size": 0
            })
            metrics["versioned_object_count"] += 1
            metrics["versioned_object_size"] += object_size
            if version["IsLatest"]:
                metrics["current_object_count"] += 1
                metrics["current_object_size"] += object_size
    f.write("-" * 10 + "\n")
    for prefix, metrics in prefix_metrics.items():
        f.write(f"Metrics for Prefix: {prefix}\n")
        f.write("$ Total Delete Markers: {}\n".format(delete_marker_count))
        f.write("$ Number of Current objects: {}\n".format(metrics["current_object_count"]))
        f.write("$ Current Objects size: {}\n".format(calculate_size(metrics["current_object_size"], size_table)))
        f.write("$ Number of Non-current objects: {}\n".format(metrics["versioned_object_count"]))
        f.write("$ Non-current Objects size: {}\n".format(calculate_size(metrics["versioned_object_size"], size_table)))
        f.write("$ Total size Current + Non-current: {}\n".format(calculate_size(metrics["current_object_size"] + metrics["versioned_object_size"], size_table)))
        f.write("-" * 5 + "\n\n")
    f.write("-" * 10 + "\n")
    f.write("$ Process completed successfully\n\n")


# -*- coding: utf-8 -*-

import boto3
from s3splitmerge.merge import merge_parquet_by_prefix
from s3splitmerge.lbd.hdl_create_parquet import lbd_func_create_parquet
from s3splitmerge.lbd.hdl_split_csv import lbd_func_split_csv
from s3splitmerge.lbd.hdl_split_parquet import lbd_func_split_parquet
from chalice import Chalice

boto_ses = boto3.session.Session()
s3_client = boto_ses.client("s3")

app = Chalice(app_name="s3splitmerge")


@app.lambda_function(name=lbd_func_create_parquet.name)
def handler_create_parquet(event, context):
    return lbd_func_create_parquet.handler(event, context)


@app.lambda_function(name=lbd_func_split_csv.name)
def handler_split_csv(event, context):
    return lbd_func_split_csv.handler(event, context)


@app.lambda_function(name=lbd_func_split_parquet.name)
def handler_split_parquet(event, context):
    return lbd_func_split_parquet.handler(event, context)


@app.lambda_function(name="handler_merge_parquet")
def handler_merge_parquet(event, context):
    """
    {
        "source_bucket": "aws-data-lab-sanhe-aws-etl-solutions",
        "source_key": "s3splitmerge/tests/many-file/parquet-1GB/",
        "target_bucket": "aws-data-lab-sanhe-aws-etl-solutions",
        "target_key": "s3splitmerge/tests/out/many-file/parquet-1GB/{i}.parquet",
        "target_size": 250 * 1024 * 1024
    }


    {
        "source_bucket": "aws-data-lab-sanhe-aws-etl-solutions",
        "source_key": "s3splitmerge/tests/many-file/parquet-1MB/",
        "target_bucket": "aws-data-lab-sanhe-aws-etl-solutions",
        "target_key": "s3splitmerge/tests/out/many-file/parquet-1MB/{i}.parquet",
        "target_size": 500 * 1024
    }
    """
    me = MergeEvent(**event)
    return merge_parquet_by_prefix(
        boto3_session=boto_ses,
        source_bucket=me.source_bucket,
        source_key_prefix=me.source_key,
        target_bucket=me.target_bucket,
        target_key=me.target_key,
        target_size=me.target_size,
    )

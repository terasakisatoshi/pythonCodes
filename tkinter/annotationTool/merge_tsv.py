import argparse
from collections import defaultdict
import csv
from glob import glob
import os
import random

import pandas as pd

IMAGE_EXTENSION = ".JPG"


def get_answer(tsv_path):
    img_path = os.path.splitext(tsv_path)[0] + IMAGE_EXTENSION
    df = pd.read_csv(tsv_path, delimiter='\t')
    return df


def exists_img(tsv_path):
    img_path = os.path.splitext(tsv_path)[0] + IMAGE_EXTENSION
    return os.path.exists(img_path)


def collect_data(dataset, divide_ratio):
    for root, dirs, files in os.walk(dataset):
        is_used_for_train = random.random() < divide_ratio
        tsv_files = glob(os.path.join(root, "*.tsv"))
        tsv_files = list(filter(exists_img, tsv_files))
        for tsv_file in tsv_files:
            img_path = os.path.splitext(tsv_file)[0] + IMAGE_EXTENSION
            df = pd.read_csv(tsv_file, delimiter='\t')
            df["ImagePath"] = os.path.abspath(img_path)
            df["UseFor"] = is_used_for_train
            df = df.rename(columns={"ID": "TargetNo"})
            yield df


def make_tsv(args):
    tot_df = None
    for df in collect_data(args.dataset, args.divide_ratio):
        if tot_df is None:
            tot_df = df
        else:
            tot_df = pd.concat([tot_df, df])
    # permutate order of cols
    cols = ["ImagePath", "UseFor"] + \
        [col for col in tot_df if not col in ["ImagePath", "UseFor"]]
    tot_df = tot_df[cols]
    tot_df.to_csv(args.output, sep="\t", index=False)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dataset", help="dataset directory includes pairs of TSV and JPG")
    parser.add_argument(
        "--divide-ratio", type=float, default=0.7, help="divide ratio which is used dividing dataset into train and valid")
    parser.add_argument(
        "--seed", type=int, default=12345, help="random seed")
    parser.add_argument("-o", "--output", default="output.tsv")
    return parser.parse_args()


def main():
    args = parse_arguments()
    random.seed(args.seed)
    make_tsv(args)


if __name__ == '__main__':
    main()

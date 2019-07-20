import argparse

def parser_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('-d','--data_dir',type=str,help="data")
    parser.add_argument('-i','--integer',type=int,help="len(argv)")
    return parser.parse_args()

def main():
    args=parser_args()
    print(args.integer)
    print(args.data_dir)

if __name__ == '__main__':
    main()
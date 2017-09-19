import argparse as argp

parser = argp.ArgumentParser(description='Get some bookz')
parser.add_argument('book_name', metavar='Book', type=string, nargs='+',
                    help='da book to get')

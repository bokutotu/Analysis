import argparse

import numpy as np


def main(args):
    trj = np.load(args.trj_name)
    with open(args.save_name, "w+") as f:
        f.write("HEADER \n \n")
        for time in range(trj.shape[0]):
            for atom in range(trj.shape[1]):
                coord = trj[time, atom]
                coord = list(coord)
                str_coord = " {:.5e} {:.5e} {:.5e}\n".format(
                    coord[0], coord[1], coord[2])
                f.write(str_coord)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="numpy のトラジェクトリをAmber cordに変換します")
    parser.add_argument("--save_name", type=str,
                        required=True, help="保存するファイルの名前")
    parser.add_argument("--trj_name", type=str,
                        required=True, help="変換するnpyファイルの名前")

    args = parser.parse_args()
    main(args)

# coding: UTF-8
import argparse
import os

from experiment import Experiment


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # data
    parser.add_argument('--imsize', type=int, default=64)
    parser.add_argument('--n_workers', type=int, default=2)
    # model
    parser.add_argument('--nz', type=int, default=100)
    parser.add_argument('--nc', type=int, default=3)
    parser.add_argument('--ngf', type=int, default=64)
    parser.add_argument('--ndf', type=int, default=64)
    # training
    parser.add_argument('--device', type=str, default='cuda:0')
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--lr', type=float, default=0.0002)
    # log
    parser.add_argument('--log_freq', type=int, default=100)
    parser.add_argument('--output_dir', type=str, default='./results')

    args, unknown_args = parser.parse_known_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    Experiment(args).run()

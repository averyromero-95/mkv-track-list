"""MKV Track List — List video, audio, and subtitle tracks in an MKV with language and codec."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='mkv_track_list',
        description='List video, audio, and subtitle tracks in an MKV with language and codec.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('MKV Track List')
    print('What is actually inside the file.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python
#
# Copyright 2021 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
""" Merges dEQP sharded test results in the ANGLE testing infrastucture."""

import os
import pathlib
import sys


PY_UTILS = str(pathlib.Path(__file__).resolve().parents[1] / 'src' / 'tests' / 'py_utils')
if PY_UTILS not in sys.path:
    os.stat(PY_UTILS) and sys.path.insert(0, PY_UTILS)
import angle_path_util

angle_path_util.AddDepsDirToPath('testing/merge_scripts')
import merge_api
import standard_isolated_script_merge


def main(raw_args):

    parser = merge_api.ArgumentParser()
    args = parser.parse_args(raw_args)

    # TODO(jmadill): Merge QPA files into one. http://anglebug.com/5236

    return standard_isolated_script_merge.StandardIsolatedScriptMerge(
        args.output_json, args.summary_json, args.jsons_to_merge)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

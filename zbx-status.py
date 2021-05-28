from os.path import exists, dirname
from os import makedirs, remove

from metrics import STATUSES
from mbrgk import DG
import argparse
import re
import json

BEGIN = re.compile(r'^Instantaneous measure |^Totals ')


def get_zbx_measures(host, port, filename):
    measures_to_zbx = ['Instantaneous measure L1 Phase Voltage - Mains (Bus)',
                       'Instantaneous measure L2 Phase Voltage - Mains (Bus)',
                       'Instantaneous measure L3 Phase Voltage - Mains (Bus)',
                       'Instantaneous measure L1 Phase Voltage - Generator',
                       'Instantaneous measure L2 Phase Voltage - Generator',
                       'Instantaneous measure L3 Phase Voltage - Generator',
                       'Instantaneous measure L1 Current',
                       'Instantaneous measure L2 Current',
                       'Instantaneous measure L3 Current',
                       'Instantaneous measure Neutral Current',
                       'Instantaneous measure Eqv. Phase Voltage - Mains (Bus)',
                       'Instantaneous measure Eqv. Phase-To-Phase Voltage Mains (Bus)',
                       'Instantaneous measure Frequency - Mains(Bus)',
                       'Instantaneous measure Eqv. Phase Voltage - Generator',
                       'Instantaneous measure Eqv. Phase-To-Phase Voltage - Generator',
                       'Instantaneous measure Frequency - Generator',
                       'Instantaneous measure Eqv Power Factor - Mains (Bus)',
                       'Instantaneous measure Power Factor - Generator',
                       'Instantaneous measure Engine speed',
                       'Totals Engine working time',
                       'Totals Engine partial running time',
                       'Totals Good cranks',
                       'Totals Total cranks',
                       'Totals Rate good crancks',
                       'Totals Temperature',
                       'Totals Pressure',
                       'Totals Fuel',
                       'Totals Battery voltage',
                       'Totals D+ input voltage',
                       'Status Device global status(bit 0-bit15)'
                       ]
    dg = DG(host=host, port=port)
    data = dg.get_measures_by_list(measures_to_zbx)
    with open(filename, 'w') as fl:
        for measure_name, measure in data.items():
            if measure_name == 'Status Device global status(bit 0-bit15)':
                for k, v in STATUSES.items():
                    if k in measure[0]:
                        print(f"{k}=1", file=fl)
                    else:
                        print(f"{k}=0", file=fl)
            else:
                short_name = re.sub(BEGIN, '', measure_name, 1)
                if isinstance(measure, tuple):
                    print(f"{short_name}={measure[0]}", file=fl)
                else:
                    print(f"{short_name}={measure}", file=fl)


def create_dir(full_dir_path):
    if not exists(full_dir_path):
        makedirs(full_dir_path)


def remove_file(full_file_name):
    if exists(full_file_name):
        remove(full_file_name)


def run():
    parser = argparse.ArgumentParser(prog='dg-status',
                                     description='Get generating set controller status.')
    parser.add_argument('-t', '--host',  # -h occupied by help :(
                        required=True,
                        help="Generating set controller hostname or IP.")
    parser.add_argument('-p', '--port',
                        required=True,
                        help="Generating set controller port number.")
    parser.add_argument('-f', '--file',
                        required=True,
                        help="File name to store generating set controller measures.")
    args = parser.parse_args()

    get_zbx_measures(host=args.host, port=args.port, filename=args.file)


def batch():
    parser = argparse.ArgumentParser(prog='dg-status',
                                     description='Get generating set controller status.')
    parser.add_argument('-j', '--json',
                        required=True,
                        help="Zabbix LLD json file to discover generating sets controllers.")
    args = parser.parse_args()

    with open(args.json) as fl:
        try:
            dg_lld = json.load(fl)
        except json.decoder.JSONDecodeError as e:
            print(f"LLD json file decode error: {e}")
            exit(1)
    try:
        data = dg_lld['data']
    except KeyError as e:
        print(f"Invalid LLD json format. Absent root key: {e}")
        exit(2)
    expected_keys = {'{#DGHOST}', '{#DGPORT}', '{#DGMEASUREFILE}'}
    for itm in data:
        keys = set(itm.keys())
        if keys.intersection(expected_keys) != expected_keys:
            print(f"Not enough parameters in LLD json: {expected_keys.difference(keys)}")
            exit(3)
        metrics_file = itm['{#DGMEASUREFILE}']
        #remove_file(metrics_file)
        create_dir(dirname(metrics_file))
        get_zbx_measures(host=itm['{#DGHOST}'], port=itm['{#DGPORT}'], filename=itm['{#DGMEASUREFILE}'])


if __name__ == "__main__":
    # run()
    batch()

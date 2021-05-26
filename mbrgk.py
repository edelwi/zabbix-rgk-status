from collections import OrderedDict
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

from metrics import RGK_MEASURES, STATUSES, Measure, UNIT

# TODO: Выделить в отдельный проект и реализовать функции управления.

class DG:
    def __init__(self, host, port, model='default'):
        self._host = host
        self._port = port
        # TODO: add measures supported by models.
        self._model = model
        self._server = None

    def connect(self):
        if not self._server:
            self._server = ModbusClient(self._host, port=self._port)
            self._server.connect()

    def disconnect(self):
        if self._server:
            self._server.close()
            self._server = None

    def close(self):
        self.disconnect()

    def __del__(self):
        self.disconnect()

    @staticmethod
    def get_status_list(word):
        out = []
        for k,v in STATUSES.items():
            if word & v:
                out.append(k)
        return out

    @staticmethod
    def unpack(measure: Measure, registers):
        decoder = BinaryPayloadDecoder.fromRegisters(registers,
                                                     byteorder=Endian.Big,
                                                     wordorder=Endian.Big)
        if measure.format == 'Unsigned long' or measure.format == 'long':
            return decoder.decode_32bit_uint()
        elif measure.format == 'Signed long':
            return decoder.decode_32bit_int()
        elif measure.format == 'Status bit map':
            val_ = decoder.decode_16bit_uint()
            return DG.get_status_list(val_)
        elif measure.format == 'Unsigned int':
            return decoder.decode_16bit_uint()
        elif measure.format == 'Status bit map (hi)':
            return registers
        else:
            return registers

    def dump_all_metrics(self, file_name='default'):
        if file_name == 'default':
            from datetime import datetime
            dt = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            _file_name = f'DGRGK_{dt}.txt'
        else:
            _file_name = file_name

        self.connect()

        with open(_file_name, 'w') as fl:
            for measure_name, measure_nt in RGK_MEASURES.items():
                try:
                    response = self._server.read_input_registers(measure_nt.address-1, measure_nt.words, unit=UNIT)
                except TypeError as e:
                    print(measure_name, measure_nt.address)
                if response.isError():
                    print(f"{measure_name} - error (or call is not supported)!", file=fl)
                else:
                    if measure_nt.format:
                        try:
                            if measure_nt.multiplier:
                                print(f"{measure_name}="
                                      f"{DG.unpack(measure_nt, response.registers) * measure_nt.multiplier} "
                                      f"{measure_nt.unit}", file=fl)
                            else:
                                print(f"{measure_name}={DG.unpack(measure_nt, response.registers)} "
                                      f"{measure_nt.unit}", file=fl)
                        except TypeError as e:
                            # print(f"Error: {e}", file=fl)
                            # print(f"{measure_name =} {response.registers =} {measure_nt.multiplier =} "
                            #       f"{measure_nt.unit =}", file=fl)
                            pass
                    else:
                        #print(f"{measure_name}", file=fl)
                        pass

    def get_measure_by_name(self, measure_name: str):
        self.connect()
        measure = RGK_MEASURES[measure_name]
        response = self._server.read_input_registers(
            measure.address-1,
            measure.words,
            unit=UNIT
        )
        if response.isError():
            return None
        else:
            if measure.format:
                try:
                    if measure.multiplier:
                        result = (DG.unpack(measure, response.registers) * measure.multiplier,
                                  measure.unit)
                    else:
                        result = (DG.unpack(measure, response.registers), measure.unit)
                except TypeError as e:
                    return None
            else:
                result = (response.registers, None)
        return result

    def get_measures_by_list(self, measures_name: list):
        if not isinstance(measures_name, list):
            return None
        result = OrderedDict()
        for measure in measures_name:
            result[measure] = self.get_measure_by_name(measure_name=measure)
        return result

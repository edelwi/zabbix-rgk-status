from collections import namedtuple, OrderedDict

Measure = namedtuple('Measure', 'address, words, unit, multiplier, format')

# TODO: Реализовать контроль доступности измерений моделям систем.

RGK_MEASURES = OrderedDict(
    [
        ('Average measure L1 Phase Voltage - Mains (Bus)',
         Measure(address=0x0002, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L2 Phase Voltage - Mains (Bus)',
        Measure(address=0x0004, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L3 Phase Voltage - Mains (Bus)',
        Measure(address=0x0006, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L1 Phase Voltage - Generator',
        Measure(address=0x0008, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L2 Phase Voltage - Generator',
        Measure(address=0x000A, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L3 Phase Voltage - Generator',
        Measure(address=0x000C, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L1 Current',
        Measure(address=0x000E, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure L2 Current',
        Measure(address=0x0010, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure L3 Current',
        Measure(address=0x0012, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure Neutral Current',
        Measure(address=0x0014, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure L1-L2 Voltage - Mains (Bus)',
        Measure(address=0x0016, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L2-L3 Voltage - Mains (Bus)',
        Measure(address=0x0018, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L3-L1 Voltage - Mains (Bus)',
        Measure(address=0x001A, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L1-L2 Voltage - Generator',
        Measure(address=0x001C, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L2-L3 Voltage - Generator',
        Measure(address=0x001E, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L3-L1 Voltage - Generator',
        Measure(address=0x0020, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure L1 Active Power - Mains (Bus)',
        Measure(address=0x0022, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Average measure L2 Active Power - Mains (Bus)',
        Measure(address=0x0024, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Average measure L3 Active Power - Mains (Bus)',
        Measure(address=0x0026, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Average measure L1 Active Power - Generator',
        Measure(address=0x0028, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Average measure L2 Active Power - Generator',
        Measure(address=0x002A, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Average measure L3 Active Power - Generator',
        Measure(address=0x002C, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Average measure L1 Reactive Power - Mains (Bus)',
        Measure(address=0x002E, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Average measure L2 Reactive Power - Mains (Bus)',
        Measure(address=0x0030, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Average measure L3 Reactive Power - Mains (Bus)',
        Measure(address=0x0032, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Average measure L1 Reactive Power - Generator',
        Measure(address=0x0034, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Average measure L2 Reactive Power - Generator',
        Measure(address=0x0036, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Average measure L3 Reactive Power - Generator',
        Measure(address=0x0038, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Average measure L1 Apparent Power - Mains (Bus)',
        Measure(address=0x003A, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Average measure L2 Apparent Power - Mains (Bus)',
        Measure(address=0x003C, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Average measure L3 Apparent Power - Mains (Bus)',
        Measure(address=0x003E, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Average measure L1 Apparent Power - Generator',
        Measure(address=0x0040, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Average measure L2 Apparent Power - Generator',
        Measure(address=0x0042, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Average measure L3 Apparent Power - Generator',
        Measure(address=0x0044, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Average measure L1 Power Factor - Mains (Bus)',
        Measure(address=0x0046, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure L2 Power Factor - Mains (Bus)',
        Measure(address=0x0048, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure L3 Power Factor - Mains (Bus)',
        Measure(address=0x004A, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure L1 Power Factor - Generator',
        Measure(address=0x004C, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure L2 Power Factor - Generator',
        Measure(address=0x004E, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure L3 Power Factor - Generator',
        Measure(address=0x0050, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure Eqv. Phase Voltage - Mains (Bus)',
        Measure(address=0x0052, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure Eqv. Phase-To-Phase Voltage Mains (Bus)',
        Measure(address=0x0054, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure Frequency - Mains(Bus)',
        Measure(address=0x0056, words=2, unit='Hz', multiplier=0.001, format='Unsigned long')), (
        'Average measure Eqv. Phase Voltage - Generator',
        Measure(address=0x0058, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure Eqv. Phase-To-Phase Voltage - Generator',
        Measure(address=0x005A, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Average measure Frequency - Generator',
        Measure(address=0x005C, words=2, unit='Hz', multiplier=0.001, format='Unsigned long')), (
        'Average measure Eqv Power Factor - Mains (Bus)',
        Measure(address=0x005E, words=2, unit='', multiplier=0.0001, format='Signed long')),
        ('Average measure Free', Measure(address=0x0068, words=2, unit='', multiplier=1, format='')), (
        'Average measure Power Factor - Generator',
        Measure(address=0x0064, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure Eqv. Active Power - Mains (Bus)',
        Measure(address=0x006A, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Average measure Eqv. Reactive Power - Mains (Bus)',
        Measure(address=0x006C, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Average measure Eqv. Apparent Power - Mains (Bus)',
        Measure(address=0x006E, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Average measure Eqv. Active Power - Generator',
        Measure(address=0x0070, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Average measure Eqv. Reactive Power - Generator',
        Measure(address=0x0072, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Average measure Eqv. Apparent Power - Generator',
        Measure(address=0x0074, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Average measure % Active Power - Mains (Bus)',
        Measure(address=0x0076, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Average measure % Reactive Power - Mains (Bus)',
        Measure(address=0x0078, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Average measure % Apparent Power - Mains (Bus)',
        Measure(address=0x007A, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure % Active Power Generator',
        Measure(address=0x007C, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Average measure % Reactive Power - Generator',
        Measure(address=0x007E, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Average measure % Apparent Power - Generator',
        Measure(address=0x0080, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure Phase-Phase Voltage Asymmetriy - Mains',
        Measure(address=0x0082, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure Phase-Neural Voltage Asymmetriy- Mains (Bus)',
        Measure(address=0x0084, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure Current Asymmetry - Mains (Bus)',
        Measure(address=0x0086, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure Phase-Phase Voltage Asymmetriy - Generator',
        Measure(address=0x0088, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure Phase-Neural Voltage Asymmetriy - Generator',
        Measure(address=0x008A, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure Current Asymmetry - Generator',
        Measure(address=0x008C, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure Engine speed',
        Measure(address=0x008E, words=2, unit='Rpm', multiplier=0.1, format='Unsigned long')), (
        'Average measure L1-2 Voltage Thd - Generator',
        Measure(address=0x0090, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure L2-3 Voltage Thd - Generator',
        Measure(address=0x0092, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure L3-1 Voltage Thd - Generator',
        Measure(address=0x0094, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure L1 Voltage Thd - Generator',
        Measure(address=0x0096, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure L2 Voltage Thd - Generator',
        Measure(address=0x0098, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure L3 Voltage Thd - Generator',
        Measure(address=0x009A, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure L1 Current Thd - Generator',
        Measure(address=0x009C, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure L2 Current Thd - Generator',
        Measure(address=0x009E, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure L3 Current Thd - Generator',
        Measure(address=0x00A0, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure N Current Thd - Generator',
        Measure(address=0x00A2, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Average measure L1 CosPhi - Generator',
        Measure(address=0x00A4, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure L2 CosPhi - Generator',
        Measure(address=0x00A6, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure L3 CosPhi - Generator',
        Measure(address=0x00A8, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure L1 Current - view -',
        Measure(address=0x00AA, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure L2 Current - view -',
        Measure(address=0x00AC, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure L3 Current - view -',
        Measure(address=0x00AE, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure Neutral Current - view -',
        Measure(address=0x00B0, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure Engine speed W or Pick-UP',
        Measure(address=0x00B2, words=2, unit='Rpm', multiplier=0.1, format='Unsigned long')), (
        'Average measure Delta frequency',
        Measure(address=0x00B4, words=2, unit='Hz', multiplier=0.001, format='Signed long')), (
        'Average measure Active Power - Load',
        Measure(address=0x00B6, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Average measure Reactive Power - Load',
        Measure(address=0x00B8, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Average measure Apparent Power - Load',
        Measure(address=0x00BA, words=2, unit='VA', multiplier=0.01, format='Signed long')), (
        'Average measure Power factor - load',
        Measure(address=0x00BC, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Average measure L5 Current',
        Measure(address=0x00BE, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure L5 Current - view -',
        Measure(address=0x00C0, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Average measure L5 CosPhi - Mains/Bus',
        Measure(address=0x00C2, words=2, unit='', multiplier=0.01, format='Signed long')), (
        'Average measure Nominal power of devices connected to bus',
        Measure(address=0x00C4, words=2, unit='', multiplier=0.01, format='Unsigned long')), (
        'Average measure Load power',
        Measure(address=0x00C6, words=2, unit='', multiplier=0.01, format='Unsigned long')), (
        'Average measure Power reserve',
        Measure(address=0x00C8, words=2, unit='', multiplier=0.01, format='Unsigned long')), (
        'Average measure Time remaining before switchover (GEN1-GEN2 )',
        Measure(address=0x1104, words=2, unit='min', multiplier=1, format='Unsigned long')), (
        'Average measure Time remaining before switchover (GEN2-GEN1 )',
        Measure(address=0x1106, words=2, unit='min', multiplier=1, format='Unsigned long')), (
        'Instantaneous measure L1 Phase Voltage - Mains (Bus)',
        Measure(address=0x200, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L2 Phase Voltage - Mains (Bus)',
        Measure(address=0x202, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L3 Phase Voltage - Mains (Bus)',
        Measure(address=0x204, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L1 Phase Voltage - Generator',
        Measure(address=0x206, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L2 Phase Voltage - Generator',
        Measure(address=0x208, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L3 Phase Voltage - Generator',
        Measure(address=0x20a, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L1 Current',
        Measure(address=0x20c, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Instantaneous measure L2 Current',
        Measure(address=0x20e, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Instantaneous measure L3 Current',
        Measure(address=0x210, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Instantaneous measure Neutral Current',
        Measure(address=0x212, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Instantaneous measure L1-L2 Voltage - Mains (Bus)',
        Measure(address=0x214, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L2-L3 Voltage - Mains (Bus)',
        Measure(address=0x216, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L3-L1 Voltage - Mains (Bus)',
        Measure(address=0x218, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L1-L2 Voltage - Generator',
        Measure(address=0x21a, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L2-L3 Voltage - Generator',
        Measure(address=0x21c, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L3-L1 Voltage - Generator',
        Measure(address=0x21e, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L1 Active Power - Mains (Bus)',
        Measure(address=0x220, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L2 Active Power - Mains (Bus)',
        Measure(address=0x222, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L3 Active Power - Mains (Bus)',
        Measure(address=0x224, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L1 Active Power - Generator',
        Measure(address=0x226, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L2 Active Power - Generator',
        Measure(address=0x228, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L3 Active Power - Generator',
        Measure(address=0x22a, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L1 Reactive Power - Mains (Bus)',
        Measure(address=0x22c, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L2 Reactive Power - Mains (Bus)',
        Measure(address=0x22e, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L3 Reactive Power - Mains (Bus)',
        Measure(address=0x230, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L1 Reactive Power - Generator',
        Measure(address=0x232, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L2 Reactive Power - Generator',
        Measure(address=0x234, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L3 Reactive Power - Generator',
        Measure(address=0x236, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure L1 Apparent Power - Mains (Bus)',
        Measure(address=0x238, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L2 Apparent Power - Mains (Bus)',
        Measure(address=0x23a, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L3 Apparent Power - Mains (Bus)',
        Measure(address=0x23c, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L1 Apparent Power - Generator',
        Measure(address=0x23e, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L2 Apparent Power - Generator',
        Measure(address=0x240, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L3 Apparent Power - Generator',
        Measure(address=0x242, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L1 Power Factor - Mains (Bus)',
        Measure(address=0x244, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure L2 Power Factor - Mains (Bus)',
        Measure(address=0x246, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure L3 Power Factor - Mains (Bus)',
        Measure(address=0x248, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure L1 Power Factor - Generator',
        Measure(address=0x24a, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure L2 Power Factor - Generator',
        Measure(address=0x24c, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure L3 Power Factor - Generator',
        Measure(address=0x24e, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure Eqv. Phase Voltage - Mains (Bus)',
        Measure(address=0x250, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Eqv. Phase-To-Phase Voltage Mains (Bus)',
        Measure(address=0x252, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Frequency - Mains(Bus)',
        Measure(address=0x254, words=2, unit='Hz', multiplier=0.001, format='Unsigned long')), (
        'Instantaneous measure Eqv. Phase Voltage - Generator',
        Measure(address=0x256, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Eqv. Phase-To-Phase Voltage - Generator',
        Measure(address=0x258, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Frequency - Generator',
        Measure(address=0x25a, words=2, unit='Hz', multiplier=0.001, format='Unsigned long')), (
        'Instantaneous measure Eqv Power Factor - Mains (Bus)',
        Measure(address=0x25c, words=2, unit='', multiplier=0.0001, format='Signed long')),
        ('Instantaneous measure Free', Measure(address=0x266, words=2, unit='', multiplier=1, format='')), (
        'Instantaneous measure Power Factor - Generator',
        Measure(address=0x262, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure Eqv. Active Power - Mains (Bus)',
        Measure(address=0x268, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure Eqv. Reactive Power - Mains (Bus)',
        Measure(address=0x26a, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure Eqv. Apparent Power - Mains (Bus)',
        Measure(address=0x26c, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Eqv. Active Power - Generator',
        Measure(address=0x26e, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure Eqv. Reactive Power - Generator',
        Measure(address=0x270, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure Eqv. Apparent Power - Generator',
        Measure(address=0x272, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure % Active Power - Mains (Bus)',
        Measure(address=0x274, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure % Reactive Power - Mains (Bus)',
        Measure(address=0x276, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure % Apparent Power - Mains (Bus)',
        Measure(address=0x278, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure % Active Power Generator',
        Measure(address=0x27a, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure % Reactive Power - Generator',
        Measure(address=0x27c, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Instantaneous measure % Apparent Power - Generator',
        Measure(address=0x27e, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Phase-Phase Voltage Asymmetriy - Mains',
        Measure(address=0x280, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Phase-Neural Voltage Asymmetriy- Mains (Bus)',
        Measure(address=0x282, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Current Asymmetry - Mains (Bus)',
        Measure(address=0x284, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Phase-Phase Voltage Asymmetriy - Generator',
        Measure(address=0x286, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Phase-Neural Voltage Asymmetriy - Generator',
        Measure(address=0x288, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Current Asymmetry - Generator',
        Measure(address=0x28a, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure Engine speed',
        Measure(address=0x28c, words=2, unit='Rpm', multiplier=0.1, format='Unsigned long')), (
        'Instantaneous measure L1-2 Voltage Thd - Generator',
        Measure(address=0x28e, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L2-3 Voltage Thd - Generator',
        Measure(address=0x290, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L3-1 Voltage Thd - Generator',
        Measure(address=0x292, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L1 Voltage Thd - Generator',
        Measure(address=0x294, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L2 Voltage Thd - Generator',
        Measure(address=0x296, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L3 Voltage Thd - Generator',
        Measure(address=0x298, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L1 Current Thd - Generator',
        Measure(address=0x29a, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L2 Current Thd - Generator',
        Measure(address=0x29c, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L3 Current Thd - Generator',
        Measure(address=0x29e, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure N Current Thd - Generator',
        Measure(address=0x2a0, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Instantaneous measure L1 CosPhi - Generator',
        Measure(address=0x2a2, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure L2 CosPhi - Generator',
        Measure(address=0x2a4, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure L3 CosPhi - Generator',
        Measure(address=0x2a6, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Instantaneous measure L1 Current - view -',
        Measure(address=0x2a8, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Instantaneous measure L2 Current - view -',
        Measure(address=0x2aa, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Instantaneous measure L3 Current - view -',
        Measure(address=0x2ac, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Instantaneous measure Neutral Current - view -',
        Measure(address=0x2ae, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Instantaneous measure Engine speed W or Pick-UP',
        Measure(address=0x2b0, words=2, unit='Rpm', multiplier=0.1, format='Unsigned long')), (
        'Maximum measure L1 Phase Voltage - Mains (Bus)',
        Measure(address=0x400, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L2 Phase Voltage - Mains (Bus)',
        Measure(address=0x402, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L3 Phase Voltage - Mains (Bus)',
        Measure(address=0x404, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L1 Phase Voltage - Generator',
        Measure(address=0x406, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L2 Phase Voltage - Generator',
        Measure(address=0x408, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L3 Phase Voltage - Generator',
        Measure(address=0x40a, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L1 Current',
        Measure(address=0x40c, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Maximum measure L2 Current',
        Measure(address=0x40e, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Maximum measure L3 Current',
        Measure(address=0x410, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Maximum measure Neutral Current',
        Measure(address=0x412, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Maximum measure L1-L2 Voltage - Mains (Bus)',
        Measure(address=0x414, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L2-L3 Voltage - Mains (Bus)',
        Measure(address=0x416, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L3-L1 Voltage - Mains (Bus)',
        Measure(address=0x418, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L1-L2 Voltage - Generator',
        Measure(address=0x41a, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L2-L3 Voltage - Generator',
        Measure(address=0x41c, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L3-L1 Voltage - Generator',
        Measure(address=0x41e, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L1 Active Power - Mains (Bus)',
        Measure(address=0x420, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Maximum measure L2 Active Power - Mains (Bus)',
        Measure(address=0x422, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Maximum measure L3 Active Power - Mains (Bus)',
        Measure(address=0x424, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Maximum measure L1 Active Power - Generator',
        Measure(address=0x426, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Maximum measure L2 Active Power - Generator',
        Measure(address=0x428, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Maximum measure L3 Active Power - Generator',
        Measure(address=0x42a, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Maximum measure L1 Reactive Power - Mains (Bus)',
        Measure(address=0x42c, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Maximum measure L2 Reactive Power - Mains (Bus)',
        Measure(address=0x42e, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Maximum measure L3 Reactive Power - Mains (Bus)',
        Measure(address=0x430, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Maximum measure L1 Reactive Power - Generator',
        Measure(address=0x432, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Maximum measure L2 Reactive Power - Generator',
        Measure(address=0x434, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Maximum measure L3 Reactive Power - Generator',
        Measure(address=0x436, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Maximum measure L1 Apparent Power - Mains (Bus)',
        Measure(address=0x438, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L2 Apparent Power - Mains (Bus)',
        Measure(address=0x43a, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L3 Apparent Power - Mains (Bus)',
        Measure(address=0x43c, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L1 Apparent Power - Generator',
        Measure(address=0x43e, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L2 Apparent Power - Generator',
        Measure(address=0x440, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L3 Apparent Power - Generator',
        Measure(address=0x442, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L1 Power Factor - Mains (Bus)',
        Measure(address=0x444, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure L2 Power Factor - Mains (Bus)',
        Measure(address=0x446, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure L3 Power Factor - Mains (Bus)',
        Measure(address=0x448, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure L1 Power Factor - Generator',
        Measure(address=0x44a, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure L2 Power Factor - Generator',
        Measure(address=0x44c, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure L3 Power Factor - Generator',
        Measure(address=0x44e, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure Eqv. Phase Voltage - Mains (Bus)',
        Measure(address=0x450, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Eqv. Phase-To-Phase Voltage Mains (Bus)',
        Measure(address=0x452, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Frequency - Mains(Bus)',
        Measure(address=0x454, words=2, unit='Hz', multiplier=0.001, format='Unsigned long')), (
        'Maximum measure Eqv. Phase Voltage - Generator',
        Measure(address=0x456, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Eqv. Phase-To-Phase Voltage - Generator',
        Measure(address=0x458, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Frequency - Generator',
        Measure(address=0x45a, words=2, unit='Hz', multiplier=0.001, format='Unsigned long')), (
        'Maximum measure Eqv Power Factor - Mains (Bus)',
        Measure(address=0x45c, words=2, unit='', multiplier=0.0001, format='Signed long')),
        ('Maximum measure Free', Measure(address=0x466, words=2, unit='', multiplier=1, format='')), (
        'Maximum measure Power Factor - Generator',
        Measure(address=0x462, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure Eqv. Active Power - Mains (Bus)',
        Measure(address=0x468, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Maximum measure Eqv. Reactive Power - Mains (Bus)',
        Measure(address=0x46a, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Maximum measure Eqv. Apparent Power - Mains (Bus)',
        Measure(address=0x46c, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Eqv. Active Power - Generator',
        Measure(address=0x46e, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Maximum measure Eqv. Reactive Power - Generator',
        Measure(address=0x470, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Maximum measure Eqv. Apparent Power - Generator',
        Measure(address=0x472, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure % Active Power - Mains (Bus)',
        Measure(address=0x474, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Maximum measure % Reactive Power - Mains (Bus)',
        Measure(address=0x476, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Maximum measure % Apparent Power - Mains (Bus)',
        Measure(address=0x478, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure % Active Power Generator',
        Measure(address=0x47a, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Maximum measure % Reactive Power - Generator',
        Measure(address=0x47c, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Maximum measure % Apparent Power - Generator',
        Measure(address=0x47e, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Phase-Phase Voltage Asymmetriy - Mains',
        Measure(address=0x480, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Phase-Neural Voltage Asymmetriy- Mains (Bus)',
        Measure(address=0x482, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Current Asymmetry - Mains (Bus)',
        Measure(address=0x484, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Phase-Phase Voltage Asymmetriy - Generator',
        Measure(address=0x486, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Phase-Neural Voltage Asymmetriy - Generator',
        Measure(address=0x488, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Current Asymmetry - Generator',
        Measure(address=0x48a, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure Engine speed',
        Measure(address=0x48c, words=2, unit='Rpm', multiplier=0.1, format='Unsigned long')), (
        'Maximum measure L1-2 Voltage Thd - Generator',
        Measure(address=0x48e, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L2-3 Voltage Thd - Generator',
        Measure(address=0x490, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L3-1 Voltage Thd - Generator',
        Measure(address=0x492, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L1 Voltage Thd - Generator',
        Measure(address=0x494, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L2 Voltage Thd - Generator',
        Measure(address=0x496, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L3 Voltage Thd - Generator',
        Measure(address=0x498, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L1 Current Thd - Generator',
        Measure(address=0x49a, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L2 Current Thd - Generator',
        Measure(address=0x49c, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L3 Current Thd - Generator',
        Measure(address=0x49e, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure N Current Thd - Generator',
        Measure(address=0x4a0, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Maximum measure L1 CosPhi - Generator',
        Measure(address=0x4a2, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure L2 CosPhi - Generator',
        Measure(address=0x4a4, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure L3 CosPhi - Generator',
        Measure(address=0x4a6, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Maximum measure L1 Current - view -',
        Measure(address=0x4a8, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Maximum measure L2 Current - view -',
        Measure(address=0x4aa, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Maximum measure L3 Current - view -',
        Measure(address=0x4ac, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Maximum measure Neutral Current - view -',
        Measure(address=0x4ae, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Maximum measure Engine speed W or Pick-UP',
        Measure(address=0x4b0, words=2, unit='Rpm', multiplier=0.1, format='Unsigned long')), (
        'Minimum measure L1 Phase Voltage - Mains (Bus)',
        Measure(address=0x600, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L2 Phase Voltage - Mains (Bus)',
        Measure(address=0x602, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L3 Phase Voltage - Mains (Bus)',
        Measure(address=0x604, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L1 Phase Voltage - Generator',
        Measure(address=0x606, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L2 Phase Voltage - Generator',
        Measure(address=0x608, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L3 Phase Voltage - Generator',
        Measure(address=0x60a, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L1 Current',
        Measure(address=0x60c, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Minimum measure L2 Current',
        Measure(address=0x60e, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Minimum measure L3 Current',
        Measure(address=0x610, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Minimum measure Neutral Current',
        Measure(address=0x612, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Minimum measure L1-L2 Voltage - Mains (Bus)',
        Measure(address=0x614, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L2-L3 Voltage - Mains (Bus)',
        Measure(address=0x616, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L3-L1 Voltage - Mains (Bus)',
        Measure(address=0x618, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L1-L2 Voltage - Generator',
        Measure(address=0x61a, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L2-L3 Voltage - Generator',
        Measure(address=0x61c, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L3-L1 Voltage - Generator',
        Measure(address=0x61e, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L1 Active Power - Mains (Bus)',
        Measure(address=0x620, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Minimum measure L2 Active Power - Mains (Bus)',
        Measure(address=0x622, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Minimum measure L3 Active Power - Mains (Bus)',
        Measure(address=0x624, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Minimum measure L1 Active Power - Generator',
        Measure(address=0x626, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Minimum measure L2 Active Power - Generator',
        Measure(address=0x628, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Minimum measure L3 Active Power - Generator',
        Measure(address=0x62a, words=2, unit='V', multiplier=0.01, format='Signed long')), (
        'Minimum measure L1 Reactive Power - Mains (Bus)',
        Measure(address=0x62c, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Minimum measure L2 Reactive Power - Mains (Bus)',
        Measure(address=0x62e, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Minimum measure L3 Reactive Power - Mains (Bus)',
        Measure(address=0x630, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Minimum measure L1 Reactive Power - Generator',
        Measure(address=0x632, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Minimum measure L2 Reactive Power - Generator',
        Measure(address=0x634, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Minimum measure L3 Reactive Power - Generator',
        Measure(address=0x636, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Minimum measure L1 Apparent Power - Mains (Bus)',
        Measure(address=0x638, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L2 Apparent Power - Mains (Bus)',
        Measure(address=0x63a, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L3 Apparent Power - Mains (Bus)',
        Measure(address=0x63c, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L1 Apparent Power - Generator',
        Measure(address=0x63e, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L2 Apparent Power - Generator',
        Measure(address=0x640, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L3 Apparent Power - Generator',
        Measure(address=0x642, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L1 Power Factor - Mains (Bus)',
        Measure(address=0x644, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure L2 Power Factor - Mains (Bus)',
        Measure(address=0x646, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure L3 Power Factor - Mains (Bus)',
        Measure(address=0x648, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure L1 Power Factor - Generator',
        Measure(address=0x64a, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure L2 Power Factor - Generator',
        Measure(address=0x64c, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure L3 Power Factor - Generator',
        Measure(address=0x64e, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure Eqv. Phase Voltage - Mains (Bus)',
        Measure(address=0x650, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Eqv. Phase-To-Phase Voltage Mains (Bus)',
        Measure(address=0x652, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Frequency - Mains(Bus)',
        Measure(address=0x654, words=2, unit='Hz', multiplier=0.001, format='Unsigned long')), (
        'Minimum measure Eqv. Phase Voltage - Generator',
        Measure(address=0x656, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Eqv. Phase-To-Phase Voltage - Generator',
        Measure(address=0x658, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Frequency - Generator',
        Measure(address=0x65a, words=2, unit='Hz', multiplier=0.001, format='Unsigned long')), (
        'Minimum measure Eqv Power Factor - Mains (Bus)',
        Measure(address=0x65c, words=2, unit='', multiplier=0.0001, format='Signed long')),
        ('Minimum measure Free', Measure(address=0x666, words=2, unit='', multiplier=1, format='')), (
        'Minimum measure Power Factor - Generator',
        Measure(address=0x662, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure Eqv. Active Power - Mains (Bus)',
        Measure(address=0x668, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Minimum measure Eqv. Reactive Power - Mains (Bus)',
        Measure(address=0x66a, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Minimum measure Eqv. Apparent Power - Mains (Bus)',
        Measure(address=0x66c, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Eqv. Active Power - Generator',
        Measure(address=0x66e, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Minimum measure Eqv. Reactive Power - Generator',
        Measure(address=0x670, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Minimum measure Eqv. Apparent Power - Generator',
        Measure(address=0x672, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure % Active Power - Mains (Bus)',
        Measure(address=0x674, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Minimum measure % Reactive Power - Mains (Bus)',
        Measure(address=0x676, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Minimum measure % Apparent Power - Mains (Bus)',
        Measure(address=0x678, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure % Active Power Generator',
        Measure(address=0x67a, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Minimum measure % Reactive Power - Generator',
        Measure(address=0x67c, words=2, unit='%', multiplier=0.01, format='Signed long')), (
        'Minimum measure % Apparent Power - Generator',
        Measure(address=0x67e, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Phase-Phase Voltage Asymmetriy - Mains',
        Measure(address=0x680, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Phase-Neural Voltage Asymmetriy- Mains (Bus)',
        Measure(address=0x682, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Current Asymmetry - Mains (Bus)',
        Measure(address=0x684, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Phase-Phase Voltage Asymmetriy - Generator',
        Measure(address=0x686, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Phase-Neural Voltage Asymmetriy - Generator',
        Measure(address=0x688, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Current Asymmetry - Generator',
        Measure(address=0x68a, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure Engine speed',
        Measure(address=0x68c, words=2, unit='Rpm', multiplier=0.1, format='Unsigned long')), (
        'Minimum measure L1-2 Voltage Thd - Generator',
        Measure(address=0x68e, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L2-3 Voltage Thd - Generator',
        Measure(address=0x690, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L3-1 Voltage Thd - Generator',
        Measure(address=0x692, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L1 Voltage Thd - Generator',
        Measure(address=0x694, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L2 Voltage Thd - Generator',
        Measure(address=0x696, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L3 Voltage Thd - Generator',
        Measure(address=0x698, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L1 Current Thd - Generator',
        Measure(address=0x69a, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L2 Current Thd - Generator',
        Measure(address=0x69c, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L3 Current Thd - Generator',
        Measure(address=0x69e, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure N Current Thd - Generator',
        Measure(address=0x6a0, words=2, unit='%', multiplier=0.01, format='Unsigned long')), (
        'Minimum measure L1 CosPhi - Generator',
        Measure(address=0x6a2, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure L2 CosPhi - Generator',
        Measure(address=0x6a4, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure L3 CosPhi - Generator',
        Measure(address=0x6a6, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Minimum measure L1 Current - view -',
        Measure(address=0x6a8, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Minimum measure L2 Current - view -',
        Measure(address=0x6aa, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Minimum measure L3 Current - view -',
        Measure(address=0x6ac, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Minimum measure Neutral Current - view -',
        Measure(address=0x6ae, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Minimum measure Engine speed W or Pick-UP',
        Measure(address=0x6b0, words=2, unit='Rpm', multiplier=0.1, format='Unsigned long')), (
        'Measure demand L1 Current - Mains(Bus)',
        Measure(address=0x0800, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure demand L2 Current - Mains(Bus)',
        Measure(address=0x0802, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure demand L3 - Rete(Bus) L3 Current - Mains(Bus)',
        Measure(address=0x0804, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure demand Neutral Current-mains',
        Measure(address=0x0806, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure demand L1 Active Power - Mains(Bus)',
        Measure(address=0x0808, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure demand L2 Active Power - Mains(Bus)',
        Measure(address=0x080A, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure demand L3 Active Power - Mains(Bus)',
        Measure(address=0x080C, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure demand L1 Active Power - Generator',
        Measure(address=0x080E, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure demand L2 Active Power - Generator',
        Measure(address=0x0810, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure demand L3 Active Power - Generator',
        Measure(address=0x0812, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure demand L1 Reactive Power - Mains(Bus)',
        Measure(address=0x0814, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure demand L2 Reactive Power - Mains(Bus)',
        Measure(address=0x0816, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure demand L3 Reactive Power - Mains(Bus)',
        Measure(address=0x0818, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure demand L1 Reactive Power - Generator',
        Measure(address=0x081A, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure demand L2 Reactive Power - Generator',
        Measure(address=0x081C, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure demand L3 Reactive Power - Generator',
        Measure(address=0x081E, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure demand L1 Apparent Power - Mains(Bus)',
        Measure(address=0x0820, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure demand L2 Apparent Power - Mains(Bus)',
        Measure(address=0x0822, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure demand L3 Apparent Power - Mains(Bus)',
        Measure(address=0x0824, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure demand L1 Apparent Power - Generator',
        Measure(address=0x0826, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure demand L2 Apparent Power - Generator',
        Measure(address=0x0828, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure demand L3 Apparent Power - Generator',
        Measure(address=0x082A, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure demand Eqv. Active Power - Mains',
        Measure(address=0x082C, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure demand Eqv. Reactive Power - Mains (Bus)',
        Measure(address=0x082E, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure demand Eqv. Apparent Power - Mains (Bus)',
        Measure(address=0x0830, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure demand Eqv Power Factor - Mains (Bus)',
        Measure(address=0x0832, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Measure demand Eqv. Active Power - Generator',
        Measure(address=0x0834, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure demand Eqv. Reactive Power - Generator',
        Measure(address=0x0836, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure demand Eqv. Apparent Power - Generator',
        Measure(address=0x0838, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure demand Eqv Power Factor - Generator',
        Measure(address=0x083A, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Measure demand L1 Current - Generator',
        Measure(address=0x083C, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure demand L2 Current - Generator',
        Measure(address=0x083E, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure demand L3 Current - Generator',
        Measure(address=0x0840, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure demand Neutral Current - Generator',
        Measure(address=0x0842, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure max demand L1 Current - Mains(Bus)',
        Measure(address=0xa00, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure max demand L2 Current - Mains(Bus)',
        Measure(address=0xa02, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure max demand L3 - Rete(Bus) L3 Current - Mains(Bus)',
        Measure(address=0xa04, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure max demand Neutral Current-mains',
        Measure(address=0xa06, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure max demand L1 Active Power - Mains(Bus)',
        Measure(address=0xa08, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure max demand L2 Active Power - Mains(Bus)',
        Measure(address=0xa0a, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure max demand L3 Active Power - Mains(Bus)',
        Measure(address=0xa0c, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure max demand L1 Active Power - Generator',
        Measure(address=0xa0e, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure max demand L2 Active Power - Generator',
        Measure(address=0xa10, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure max demand L3 Active Power - Generator',
        Measure(address=0xa12, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure max demand L1 Reactive Power - Mains(Bus)',
        Measure(address=0xa14, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure max demand L2 Reactive Power - Mains(Bus)',
        Measure(address=0xa16, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure max demand L3 Reactive Power - Mains(Bus)',
        Measure(address=0xa18, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure max demand L1 Reactive Power - Generator',
        Measure(address=0xa1a, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure max demand L2 Reactive Power - Generator',
        Measure(address=0xa1c, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure max demand L3 Reactive Power - Generator',
        Measure(address=0xa1e, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure max demand L1 Apparent Power - Mains(Bus)',
        Measure(address=0xa20, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure max demand L2 Apparent Power - Mains(Bus)',
        Measure(address=0xa22, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure max demand L3 Apparent Power - Mains(Bus)',
        Measure(address=0xa24, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure max demand L1 Apparent Power - Generator',
        Measure(address=0xa26, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure max demand L2 Apparent Power - Generator',
        Measure(address=0xa28, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure max demand L3 Apparent Power - Generator',
        Measure(address=0xa2a, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure max demand Eqv. Active Power - Mains',
        Measure(address=0xa2c, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure max demand Eqv. Reactive Power - Mains (Bus)',
        Measure(address=0xa2e, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure max demand Eqv. Apparent Power - Mains (Bus)',
        Measure(address=0xa30, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure max demand Eqv Power Factor - Mains (Bus)',
        Measure(address=0xa32, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Measure max demand Eqv. Active Power - Generator',
        Measure(address=0xa34, words=2, unit='W', multiplier=0.01, format='Signed long')), (
        'Measure max demand Eqv. Reactive Power - Generator',
        Measure(address=0xa36, words=2, unit='Var', multiplier=0.01, format='Signed long')), (
        'Measure max demand Eqv. Apparent Power - Generator',
        Measure(address=0xa38, words=2, unit='VA', multiplier=0.01, format='Unsigned long')), (
        'Measure max demand Eqv Power Factor - Generator',
        Measure(address=0xa3a, words=2, unit='', multiplier=0.0001, format='Signed long')), (
        'Measure max demand L1 Current - Generator',
        Measure(address=0xa3c, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure max demand L2 Current - Generator',
        Measure(address=0xa3e, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure max demand L3 Current - Generator',
        Measure(address=0xa40, words=2, unit='A', multiplier=0.0001, format='Unsigned long')), (
        'Measure max demand Neutral Current - Generator',
        Measure(address=0xa42, words=2, unit='A', multiplier=0.0001, format='Unsigned long')),
        ('Analog Counter CNT 1', Measure(address=0x1D00, words=2, unit='UM1', multiplier=None, format='long')),
        ('Analog Counter CNT 2', Measure(address=0x1D02, words=2, unit='UM2', multiplier=None, format='long')),
        ('Analog Counter CNT 3', Measure(address=0x1D04, words=2, unit='UM3', multiplier=None, format='long')),
        ('Analog Counter CNT 4', Measure(address=0x1D06, words=2, unit='UM4', multiplier=None, format='long')),
        ('Analog Counter CNT 5', Measure(address=0x1D08, words=2, unit='UM5', multiplier=None, format='long')),
        ('Analog Counter CNT 6', Measure(address=0x1D0A, words=2, unit='UM6', multiplier=None, format='long')),
        ('Analog Counter CNT 7', Measure(address=0x1D0C, words=2, unit='UM7', multiplier=None, format='long')),
        ('Analog Counter CNT 8', Measure(address=0x1D0E, words=2, unit='UM8', multiplier=None, format='long')),
        ('Analog Analog input 1', Measure(address=0x0F50, words=2, unit='UM1', multiplier=None, format='long')),
        ('Analog Analog input 2', Measure(address=0x0F52, words=2, unit='UM2', multiplier=None, format='long')),
        ('Analog Analog input 3', Measure(address=0x0F54, words=2, unit='UM3', multiplier=None, format='long')),
        ('Analog Analog input 4', Measure(address=0x0F56, words=2, unit='UM4', multiplier=None, format='long')),
        ('Analog Analog input 5', Measure(address=0x0F58, words=2, unit='UM5', multiplier=None, format='long')),
        ('Analog Analog input 6', Measure(address=0x0F5A, words=2, unit='UM6', multiplier=None, format='long')),
        ('Analog Analog input 7', Measure(address=0x0F5C, words=2, unit='UM7', multiplier=None, format='long')),
        ('Analog Analog input 8', Measure(address=0x0F5E, words=2, unit='UM8', multiplier=None, format='long')),
        ('Analog Analog output 1', Measure(address=0x0F60, words=2, unit='UM1', multiplier=None, format='long')),
        ('Analog Analog output 2', Measure(address=0x0F62, words=2, unit='UM2', multiplier=None, format='long')),
        ('Analog Analog output 3', Measure(address=0x0F64, words=2, unit='UM3', multiplier=None, format='long')),
        ('Analog Analog output 4', Measure(address=0x0F66, words=2, unit='UM4', multiplier=None, format='long')),
        ('Analog Analog output 5', Measure(address=0x0F68, words=2, unit='UM5', multiplier=None, format='long')),
        ('Analog Analog output 6', Measure(address=0x0F6A, words=2, unit='UM6', multiplier=None, format='long')),
        ('Analog Analog output 7', Measure(address=0x0F6C, words=2, unit='UM7', multiplier=None, format='long')),
        ('Analog Analog output 8', Measure(address=0x0F6E, words=2, unit='UM8', multiplier=None, format='long')),
        ('Totals Engine working hours',
         Measure(address=0x0F80, words=2, unit='h', multiplier=1, format='Unsigned long')), (
        'Totals Engine working time',
        Measure(address=0x0F82, words=2, unit='s', multiplier=1, format='Unsigned long')), (
        'Totals Engine partial running hours',
        Measure(address=0x0F84, words=2, unit='h', multiplier=1, format='Unsigned long')), (
        'Totals Engine partial running time',
        Measure(address=0x0F86, words=2, unit='s', multiplier=1, format='Unsigned long')), (
        'Totals Maintenance time 1',
        Measure(address=0x0F88, words=2, unit='h', multiplier=1, format='Unsigned long')), (
        'Totals Maintenance time 2',
        Measure(address=0x0F8A, words=2, unit='h', multiplier=1, format='Unsigned long')), (
        'Totals Maintenance time 3',
        Measure(address=0x0F8C, words=2, unit='h', multiplier=1, format='Unsigned long')),
        ('Totals Rent time', Measure(address=0x0F8E, words=2, unit='h', multiplier=1, format='Unsigned long')),
        (
            'Totals Good cranks', Measure(address=0x0F90, words=2, unit='n', multiplier=1, format='Unsigned long')),
        ('Totals Total cranks',
         Measure(address=0x0F92, words=2, unit='n', multiplier=1, format='Unsigned long')), (
        'Totals Rate good crancks',
        Measure(address=0x0F94, words=2, unit='%', multiplier=0.1, format='Unsigned long')), (
        'Totals Generator contactor closing counter',
        Measure(address=0x0F96, words=2, unit='n', multiplier=1, format='Unsigned long')), (
        'Totals Modbus Function 17 clone',
        Measure(address=0x0F98, words=2, unit='', multiplier=1, format='Unsigned long')), (
        'Totals Temperature', Measure(address=0x0FA0, words=2, unit='°C or °F', multiplier=1,
                                      format='Unsigned long')),
        ('Totals Pressure', Measure(address=0x0FA2, words=2, unit='Bar', multiplier=0.1, format='Unsigned long')),
        ('Totals Fuel', Measure(address=0x0FA4, words=2, unit='%', multiplier=1, format='Unsigned long')), (
        'Totals Auxyliary sensor',
        Measure(address=0x0FA6, words=2, unit='', multiplier=1, format='Unsigned long')), (
        'Totals Battery voltage',
        Measure(address=0x0FA8, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Totals D+ input voltage',
        Measure(address=0x0FAA, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Totals AC input voltage',
        Measure(address=0x0FAC, words=2, unit='V', multiplier=0.01, format='Unsigned long')), (
        'Totals Instantaneous fuel consumption',
        Measure(address=0x0FAE, words=2, unit='l/h or gal/h', multiplier=0.1, format='Unsigned long')), (
        'Totals Total imp. Active Energy - Mains (Bus)',
        Measure(address=0x1A20, words=2, unit='kWh', multiplier=0.1, format='Unsigned long')), (
        'Totals Total exported Active Energy - Mains (Bus)',
        Measure(address=0x1A22, words=2, unit='kWh', multiplier=0.1, format='Unsigned long')), (
        'Totals Total imp. Reactive Energy - Mains (Bus)',
        Measure(address=0x1A24, words=2, unit='kvarh', multiplier=0.1, format='Unsigned long')), (
        'Totals Total exp. Reactive Energy - Mains (Bus)',
        Measure(address=0x1A26, words=2, unit='kvarh', multiplier=0.1, format='Unsigned long')), (
        'Totals Total Apparent Energy - Mains (Bus)',
        Measure(address=0x1A28, words=2, unit='kVAh', multiplier=0.1, format='Unsigned long')), (
        'Totals Total imp. Active Energy - Generator',
        Measure(address=0x1A2A, words=2, unit='kWh', multiplier=0.1, format='Unsigned long')), (
        'Totals Total exported Active Energy - Generator',
        Measure(address=0x1A2C, words=2, unit='kWh', multiplier=0.1, format='Unsigned long')), (
        'Totals Total imp. Reactive Energy - Generator',
        Measure(address=0x1A2E, words=2, unit='kvarh', multiplier=0.1, format='Unsigned long')), (
        'Totals Total exp. Reactive Energy - Generator',
        Measure(address=0x1A30, words=2, unit='kvarh', multiplier=0.1, format='Unsigned long')), (
        'Totals Total Apparent Energy - Generator',
        Measure(address=0x1A32, words=2, unit='kVAh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial imp. Active Energy - Mains (Bus)',
        Measure(address=0x1B20, words=2, unit='kWh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial exported Active Energy - Mains (Bus)',
        Measure(address=0x1B22, words=2, unit='kWh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial imp. Reactive Energy - Mains (Bus)',
        Measure(address=0x1B24, words=2, unit='kvarh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial exp. Reactive Energy - Mains (Bus)',
        Measure(address=0x1B26, words=2, unit='kvarh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial Apparent Energy - Mains (Bus)',
        Measure(address=0x1B28, words=2, unit='kVAh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial imp. Active Energy - Generator',
        Measure(address=0x1B2A, words=2, unit='kWh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial exported Active Energy - Generator',
        Measure(address=0x1B2C, words=2, unit='kWh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial imp. Reactive Energy - Generator',
        Measure(address=0x1B2E, words=2, unit='kvarh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial exp. Reactive Energy - Generator',
        Measure(address=0x1B30, words=2, unit='kvarh', multiplier=0.1, format='Unsigned long')), (
        'Totals Partial Apparent Energy - Generator',
        Measure(address=0x1B32, words=2, unit='kVAh', multiplier=0.1, format='Unsigned long')), (
        'Inputs OR of all Inputs from 1 to 16',
        Measure(address=0x2100, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Inputs INP 1', Measure(address=0x2101, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 2', Measure(address=0x2102, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 3', Measure(address=0x2103, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 4', Measure(address=0x2104, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 5', Measure(address=0x2105, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 6', Measure(address=0x2106, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 7', Measure(address=0x2107, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 8', Measure(address=0x2108, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 9', Measure(address=0x2109, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 10', Measure(address=0x210a, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 11', Measure(address=0x210b, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 12', Measure(address=0x210c, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 13', Measure(address=0x210d, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 14', Measure(address=0x210e, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 15', Measure(address=0x210f, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 16', Measure(address=0x2110, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs OR of all Inputs from 17 to 32',
         Measure(address=0x2120, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Inputs INP 17', Measure(address=0x2121, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 18', Measure(address=0x2122, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 19', Measure(address=0x2123, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 20', Measure(address=0x2124, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 21', Measure(address=0x2125, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 22', Measure(address=0x2126, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 23', Measure(address=0x2127, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 24', Measure(address=0x2128, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 25', Measure(address=0x2129, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 26', Measure(address=0x212a, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 27', Measure(address=0x212b, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 28', Measure(address=0x212c, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 29', Measure(address=0x212d, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 30', Measure(address=0x212e, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 31', Measure(address=0x212f, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Inputs INP 32', Measure(address=0x2130, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OR of all Outputs from 1 to 16',
         Measure(address=0x2140, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 1', Measure(address=0x2141, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 2', Measure(address=0x2142, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 3', Measure(address=0x2143, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 4', Measure(address=0x2144, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 5', Measure(address=0x2145, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 6', Measure(address=0x2146, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 7', Measure(address=0x2147, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 8', Measure(address=0x2148, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 9', Measure(address=0x2149, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 10', Measure(address=0x214a, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 11', Measure(address=0x214b, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 12', Measure(address=0x214c, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 13', Measure(address=0x214d, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 14', Measure(address=0x214e, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 15', Measure(address=0x214f, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 16', Measure(address=0x2150, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OR of all Outputs from 17 to 32',
         Measure(address=0x2160, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 17', Measure(address=0x2161, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 18', Measure(address=0x2162, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 19', Measure(address=0x2163, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 20', Measure(address=0x2164, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 21', Measure(address=0x2165, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 22', Measure(address=0x2166, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 23', Measure(address=0x2167, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 24', Measure(address=0x2168, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 25', Measure(address=0x2169, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 26', Measure(address=0x216a, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 27', Measure(address=0x216b, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 28', Measure(address=0x216c, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 29', Measure(address=0x216d, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 30', Measure(address=0x216e, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 31', Measure(address=0x216f, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Outputs OUT 32', Measure(address=0x2170, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes OR of all remote variables',
         Measure(address=0x2180, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Remotes REM 1', Measure(address=0x2181, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 2', Measure(address=0x2182, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 3', Measure(address=0x2183, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 4', Measure(address=0x2184, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 5', Measure(address=0x2185, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 6', Measure(address=0x2186, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 7', Measure(address=0x2187, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 8', Measure(address=0x2188, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 9', Measure(address=0x2189, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 10', Measure(address=0x218a, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 11', Measure(address=0x218b, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 12', Measure(address=0x218c, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 13', Measure(address=0x218d, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 14', Measure(address=0x218e, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 15', Measure(address=0x218f, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Remotes REM 16', Measure(address=0x2190, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits OR of all limits',
         Measure(address=0x21c0, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Limits LIM 1', Measure(address=0x21c1, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 2', Measure(address=0x21c2, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 3', Measure(address=0x21c3, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 4', Measure(address=0x21c4, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 5', Measure(address=0x21c5, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 6', Measure(address=0x21c6, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 7', Measure(address=0x21c7, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 8', Measure(address=0x21c8, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 9', Measure(address=0x21c9, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 10', Measure(address=0x21ca, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 11', Measure(address=0x21cb, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 12', Measure(address=0x21cc, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 13', Measure(address=0x21cd, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 14', Measure(address=0x21ce, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 15', Measure(address=0x21cf, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Limits LIM 16', Measure(address=0x21d0, words=1, unit='bool', multiplier=None, format='Unsigned int')),
        ('Alarms Alarms A01-A16',
         Measure(address=0x2200, words=1, unit='', multiplier=None, format='Unsigned int')), (
        'Alarms Alarms A17-A32',
        Measure(address=0x2201, words=1, unit='', multiplier=None, format='Unsigned int')), (
        'Alarms Alarms A33-A48',
        Measure(address=0x2202, words=1, unit='', multiplier=None, format='Unsigned int')), (
        'Alarms Alarms A49-A60-UA1-UA2-UA3-UA4',
        Measure(address=0x2203, words=1, unit='', multiplier=None, format='Unsigned int')), (
        'Alarms Alarms UA5-UA6-UA7',
        Measure(address=0x2204, words=1, unit='', multiplier=None, format='Unsigned int')), (
        'Status Device global status(bit 0-bit15)',
        Measure(address=0x2210, words=1, unit='', multiplier=None, format='Status bit map')), (
        'Status Device global status(bit 16-bit31)',
        Measure(address=0x2211, words=1, unit='', multiplier=None, format='Status bit map (hi)')),
        ('Geo data GPS time', Measure(address=0x1200, words=2, unit='', multiplier=None, format='Unsigned long')),
        ('Geo data GPS status',
         Measure(address=0x1202, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data GPS latitude integer part',
        Measure(address=0x1204, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data GPS latitude decimal part',
        Measure(address=0x1206, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data GPS latitude N or S',
        Measure(address=0x1208, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data GPS longitude integer part',
        Measure(address=0x120A, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data GPS longitude decimal part',
        Measure(address=0x120C, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data GPS longitude E or W',
        Measure(address=0x120E, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data Gps speed integer part',
        Measure(address=0x1210, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data Gps speed decimal part',
        Measure(address=0x1212, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data Gps track angle in degrees True integer part',
        Measure(address=0x1214, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data Gps track angle in degrees True decimal part',
        Measure(address=0x1216, words=2, unit='', multiplier=None, format='Unsigned long')),
        ('Geo data GPS date', Measure(address=0x1218, words=2, unit='', multiplier=None, format='Unsigned long')),
        ('Geo data Gps magnetic variation integer part',
         Measure(address=0x121A, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data Gps magnetic variation decimal part',
        Measure(address=0x121C, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data Gps mode indication E or W',
        Measure(address=0x121E, words=2, unit='', multiplier=None, format='Unsigned long')), (
        'Geo data Gps coordinate',
        Measure(address=0x2340, words=32, unit='', multiplier=None, format='NMEA 0183')),
        ('Date Year', Measure(address=0x28f0, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Date Month', Measure(address=0x28f1, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Date Day', Measure(address=0x28f2, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Date Hours', Measure(address=0x28f3, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Date Minutes', Measure(address=0x28f4, words=1, unit='', multiplier=None, format='Unsigned int')),
        ('Date Seconds', Measure(address=0x28f5, words=1, unit='', multiplier=None, format='Unsigned int')),
    ]
)

STATUSES = OrderedDict(
    {
    'OFF mode': 0b0000000000000001,
    'MAN mode': 0b0000000000000010,
    'AUT mode': 0b0000000000000100,
    'TEST mode': 0b0000000000001000,
    'Mains voltage OK': 0b0000000000010000,
    'Gen. voltage OK': 0b0000000000100000,
    'Engine running': 0b0000000001000000,
    'Generator ready': 0b0000000010000000,
    'Global alarm': 0b0000000100000000,
    'Mechanical fault': 0b0000001000000000,
    'Electrical fault': 0b0000010000000000,
    'Alarms enabled': 0b0000100000000000,
    'Automatic test running': 0b0001000000000000,
    'Automatic test enabled': 0b0010000000000000,
    'Mains contactor closed': 0b0100000000000000,
    'Generator contactor closed': 0b1000000000000000,
    }
)

UNIT = 0x1
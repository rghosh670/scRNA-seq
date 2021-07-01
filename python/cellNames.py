import random

NUM_CELLS = 37148

def __switch(argument):
    switcher = {
        'ADA_ADE_grandparent': 'ADE',
        'ADL_parent': 'ADL',
        'AIN_parent': 'AIN',
        'AMso_parent': 'AMso',
        'ASE_parent': 'ASE',
        'ASI_parent': 'ASI',
        'ASK_parent': 'ASK',
        'AVH_parent': 'AVH',
        'DVC_parent': 'DVC',
        'IL1_parent': 'IL1',
        'M1_parent': 'M1_parent',
        'M4_parent': 'M4_parent',
        'NSM_parent': 'NSM_parent',
        'Neuroblast_ADE_ADA': 'ADE',
        'Neuroblast_ADF_AWB': ('ADF', 'AWB'),
        'Neuroblast_AFD_RMD': ('AFD', 'RMD'),
        'Neuroblast_AIZ_FLP': ('AIZ', 'FLP'),
        'Neuroblast_AIZ_FLP_RMG': ('AIZ', 'FLP'),
        'Neuroblast_ALA_RMED': ('ALA', 'RMED'),
        'Neuroblast_ALM_BDU': 'ALM_BDU',
        'Neuroblast_ASE_ASJ_AUA': ('ASE', 'ASJ', 'AUA'),
        'Neuroblast_ASG_AWA': ('ASG', 'AWA'),
        'Neuroblast_ASH_RIB': ('ASH', 'RIB'),
        'Neuroblast_ASJ_AUA': ('ASJ', 'AUA'),
        'Neuroblast_AVG_RIR': 'AVG',
        'Neuroblast_AWC_SAAVx': 'AWC',
        'Neuroblast_BAG_SMDVx': 'BAG',
        'Neuroblast_HSN_PHB': 'PHB_and_possibly_PHA',
        'Neuroblast_I6_M5': 'Neuroblast_I6_M5',
        'Neuroblast_IL1_IL2': ('IL1', 'IL2'),
        'Neuroblast_M2_M3': 'Neuroblast_M2_M3',
        'Neuroblast_PVC_LUA': 'Neuroblast_PVC_LUA',
        'Neuroblast_URX_CEPDx': 'URX',
        'OLL_parent': 'OLL',
        'OLQ_grandparent': 'OLQ',
        'OLQ_parent': 'OLQ',
        'PLM_ALN_grandparent': ('PLM', 'ALN'),
        'PLM_ALN_great_grandparent': ('PLM', 'ALN'),
        'PVQ_parent': 'PVQ_and_possibly_PVC',
        'Parent_of_AMsh_URB': ('AMsh', 'URB_and_possibly_URA'),
        'Parent_of_MI_pm1DR': 'Parent_of_MI_pm1DR',
        'Parent_of_PVP_and_rect_V': 'PVP',
        'Parents_of_PHsh_hyp8_hyp9': 'Parents_of_PHsh_hyp8_hyp9',
        'Parents_of_Y_DA6_DA7_DA9': 'Parents_of_Y_DA6_DA7_DA9',
        'RIA_parent': 'RIA',
        'RIC_parent': 'RIC',
        'RID_parent': 'RID',
        'RIM_parent': 'RIM',
        'RME_LR_parent': 'RME',
        'URA_parent': 'URB_and_possibly_URA'
    }

    return (switcher.get(argument, argument))

def getCellName(index, includeTuples = True):
    if 'names' not in globals():
        f = open('data/geneAndTimeData/namesOfNeuronalCells.txt', 'r')
        global names
        names = f.read().splitlines()
        f.close()

    return(__switch(names[index]) if includeTuples or type(__switch(names[index])) != tuple else __switch(names[index])[0])

def getCellColor(index):
    if 'colorDict' not in globals():
        global colorDict
        colorDict = {}

    cellName = getCellName(index)
    return colorDict.setdefault(cellName, [random.random(), random.random(), random.random()])
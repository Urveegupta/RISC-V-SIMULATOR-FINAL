PC = {}
PC_temp = {}
PC_temp2 = {}
clock = 0
instructions = dict()
registers = dict()
registers_bool = dict()
memory = dict()
# for data forwarding
data_frwd = 0
stall = True
forward = False

stats = []

f = 0
to_stall = False



# variable = dict()
message = ['' for _ in range(5)]
#queues for buffers 
fetch_buffer= []
decode_buffer= []
execute_buffer= []
memory_buffer= []
BTB = [] # branch target buffer
branch_predicted=[]
data_hazard=[]
#counters
fetch_counter= 0
decode_counter= -4
execute_counter= -8
memory_counter= -12
register_counter= -16
#######
forwarding=False
status_to_pc=dict()
pc_to_status=dict()
number_of_cycles=0
number_of_instrs=0
number_of_load_store=0
number_of_alu=0
number_of_control=0
number_of_stalls=0
number_of_data_hazards=0
number_of_control_hazards=0
number_of_stalls_dh=0
number_of_stalls_ch=0
branch_mis=0
data_stalls=0
data_hazard_path=[]
control_stalls=0
buffers = []
num_of_stall_temp =0
###########

####################### PHASE 3 ###########################
data_cache = dict()
instr_cache = dict()
cache_size = None
block_size = None
numSA = 10
num_of_sets = None
num_of_blocks = None
hits = 0
misses = 0
accesses = 0
I_hits = 0
I_misses = 0
I_accesses = 0
print_cache= dict()

###########
# cache_size = 360
# block_size = 12
# numSA = 4 
###########

def getSet(numSA):
    w = dict()
    l = [0, None, None]
    for i in range(numSA):
        w[i] = [0, None, None, []]
    return w


def intialise_data_cache():
    global data_cache
    global num_of_sets
    global num_of_blocks
    num_of_blocks = int(cache_size/block_size)
    num_of_sets = int(num_of_blocks/numSA)
    for i in range(num_of_sets):
        data_cache[i] = getSet(numSA)
    return

def intialise_instr_cache():
    global instr_cache
    global num_of_sets
    global num_of_blocks
    num_of_blocks = int(cache_size/block_size)
    num_of_sets = int(num_of_blocks/numSA)
    for i in range(num_of_sets):
        instr_cache[i] = getSet(numSA)
    return

def readInstrCache(address): # type(address) = int
    
    global data_cache
    global I_hits
    global I_misses
    global I_accesses
    global print_cache

    I_accesses += 1

    startAddress = address - (address % block_size)
    numBlock = int (startAddress / num_of_blocks)
    numSet = numBlock % num_of_sets

    isHit = False
    index = -1
    reqMem = None

    for i in range(numSA):
        if (instr_cache[numSet][i][0] == 1):
            if (instr_cache[numSet][i][2] == startAddress):
                isHit = True
                index = i
                break
    
    if (isHit):
        I_hits += 1 
        print_cache["f_access"]= "Hit"
        reqMem = instr_cache[numSet][index][3][address-startAddress]
    
    else:
        I_misses += 1
        print_cache["f_access"]="Miss\t"
        isAvailable = False
        index = -1
        for i in range(numSA):
            if (instr_cache[numSet][i][0] == 0):
                isAvailable = True
                index = i
                print_cache["f_access"] += "No block evicted"
                break
        if (isAvailable == False):
            for i in range(numSA):
                if (instr_cache[numSet][i][1] == 0):
                    instr_cache[numSet][i] = getSet(numSA)
                    index = i
                    break
            print_cache["f_access"] += "Block evicted from way "+str(index)
        instr_cache[numSet][index][0] = 1
        instr_cache[numSet][index][1] = numSA-1
        instr_cache[numSet][index][2] = startAddress
        instr_cache[numSet][index][3] = [memory.get(startAddress + i, '00000000') for i in range(block_size)]
        reqMem = instr_cache[numSet][index][3][address-startAddress]
        
    for i in range(numSA):
        if (instr_cache[numSet][i][0] == 1):
            instr_cache[numSet][i][1] = max(instr_cache[numSet][i][1]-1, 0)
    instr_cache[numSet][index][1] = numSA-1

    
    print_cache["fetch"]= numSet
    return reqMem


def readDataCache(address): # type(address) = int
    
    global data_cache
    global hits
    global misses
    global accesses
    global print_cache

    accesses += 1

    startAddress = address - (address % block_size)
    numBlock = int (startAddress / num_of_blocks)
    numSet = numBlock % num_of_sets

    isHit = False
    index = -1
    reqMem = None

    for i in range(numSA):
        if (data_cache[numSet][i][0] == 1):
            if (data_cache[numSet][i][2] == startAddress):
                isHit = True
                index = i
                break
    
    if (isHit):
        hits += 1 
        print_cache["l_access"]= "Hit"
        reqMem = data_cache[numSet][index][3][address-startAddress]
    
    else:
        misses += 1
        print_cache["l_access"]="Miss\t"
        isAvailable = False
        index = -1
        for i in range(numSA):
            if (data_cache[numSet][i][0] == 0):
                isAvailable = True
                index = i
                print_cache["l_access"] += "No block evicted"
                break
        if (isAvailable == False):
            for i in range(numSA):
                if (data_cache[numSet][i][1] == 0):
                    data_cache[numSet][i] = getSet(numSA)
                    index = i
                    break
            print_cache["l_access"] += "Block evicted from way "+str(index)
        data_cache[numSet][index][0] = 1
        data_cache[numSet][index][1] = numSA-1
        data_cache[numSet][index][2] = startAddress
        data_cache[numSet][index][3] = [memory.get(startAddress + i, '00000000') for i in range(block_size)]
        reqMem = data_cache[numSet][index][3][address-startAddress]
        
    for i in range(numSA):
        if (data_cache[numSet][i][0] == 1):
            data_cache[numSet][i][1] = max(data_cache[numSet][i][1]-1, 0)
    data_cache[numSet][index][1] = numSA-1

    print_cache["load"]= numSet
    return reqMem

def writeDataCache(address, data):

    global data_cache
    global hits
    global misses
    global accesses
    global memory
    global print_cache

    accesses += 1

    startAddress = address - (address % block_size)
    numBlock = int (startAddress / num_of_blocks)
    numSet = numBlock % num_of_sets

    isHit = False
    index = -1
    reqMem = None

    for i in range(numSA):
        if (data_cache[numSet][i][0] == 1):
            if (data_cache[numSet][i][2] == startAddress):
                isHit = True
                index = i
                break
    
    if (isHit):
        hits += 1 
        print_cache["s_access"]= "Hit"
        # reqMem = data_cache[numSet][index][3][address-startAddress]
        data_cache[numSet][index][3][address-startAddress] = data
    
    else:
        misses += 1
        print_cache["s_access"]="Miss\t"
        isAvailable = False
        index = -1
        for i in range(numSA):
            if (data_cache[numSet][i][0] == 0):
                isAvailable = True
                index = i
                print_cache["s_access"] += "No block evicted"
                break
        if (isAvailable == False):
            for i in range(numSA):
                if (data_cache[numSet][i][1] == 0):
                    data_cache[numSet][i] = getSet(numSA)
                    index = i
                    break
            print_cache["s_access"] += "Block evicted from way "+str(index)
        data_cache[numSet][index][0] = 1
        data_cache[numSet][index][1] = numSA-1
        data_cache[numSet][index][2] = startAddress
        data_cache[numSet][index][3] = [memory.get(startAddress + i, '00000000') for i in range(block_size)]
        reqMem = data_cache[numSet][index][3][address-startAddress]
        data_cache[numSet][index][3][address-startAddress] = data
        
    for i in range(numSA):
        if (data_cache[numSet][i][0] == 1):
            data_cache[numSet][i][1] = max(data_cache[numSet][i][1]-1, 0)
    data_cache[numSet][index][1] = numSA-1

    memory[address] = data
    print_cache["store"]= numSet
    return None


def intialise_cache():
    global block_size
    intialise_data_cache()
    intialise_instr_cache()
    block_size = int(block_size/4)

# intialise_cache()
####################################################################

def reset_print_cache():
    global print_cache
    print_cache = {"fetch":None, "load":None, "store":None, "f_access":None,"l_access":None,"s_access":None}



def reset_all():

    global PC
    global registers
    global memory
    # global variable
    global fetch_buffer
    global decode_buffer
    global execute_buffer
    global memory_buffer
    global registers_bool
    global BTB
    global print_cache

    global status_to_pc
    global pc_to_status
    status_to_pc=dict()
    pc_to_status=dict()
    status_to_pc["Fetch"]=-1
    status_to_pc["Decode"]=-1
    status_to_pc["Execute"]=-1
    status_to_pc["Register_Update"]=-1
    status_to_pc["Memory_Write"]=-1
    ###########
    BTB = {}

    print_cache= {"fetch":None, "load":None, "store":None, "f_access":None,"l_access":None,"s_access":None}

    # PC = 0x0
    PC = {}
    PC_temp = {}

    decode_buffer= []
    execute_buffer= []
    fetch_buffer= []
    memory_buffer= []

    registers = {i: '0x00000000' for i in range(32)}
    registers_bool = {i: 0 for i in range(32)}
    
    registers[2] = '0x7FFFFFF0'  # stack pointer
    registers[3] = '0x10000000'  # global pointer

    data_size = 1000
    # to be addressed starting from 0x10000000
    memory = {(0x10000000+(4*i)): '00000000' for i in range(data_size)}

    stack_size = 1000
    # to be addressed starting from 0x7FFFFFFC

    for i in range(0x7FFFFFFC, 0x7FFFFFFC-4000, -4):
        memory[i] = '00000000'

    heap_size = 1000
    # to be addressed starting from 0x10007FE8

    for i in range(0x10007FE8, 0x10007FE8+4000, 4):
        memory[i] = '00000000'

    variable = {'opcode': '', 'funct3': '', 'funct7': '', 'rd': '',
                'rs1': '', 'rs2': '', 'instr_type': '', 'operation': ''}

    return


def readfile(filename):  # assuming input.mc has instructions > data > stack > heap

    global instructions
    global registers
    global memory

    file = open(filename, 'r')

    input_list = dict()

    for line in file:
        a, b = line.split()
        if (b == 'text_end'):
            instructions[int(a, 16)] = b
            break
        instructions[int(a, 16)] = b

    for line in file:
        a, b = line.split()
        if (b == 'data_end'):
            break
        if (b[:2] == '0x'):
            b = b[2:]
        memory[int(a, 16)] = b

    for line in file:
        a, b = line.split()
        if (b == 'stack_end'):
            break
        if (b[:2] == '0x'):
            b = b[2:]
        memory[int(a, 16)] = b

    for line in file:
        a, b = line.split()
        if (b == 'heap_end'):
            break
        if (b[:2] == '0x'):
            b = b[2:]
        memory[int(a, 16)] = b
    
    for i in instructions:
        memory[i] = instructions[i]


    #############################
    global pc_to_status
    for i in instructions:
        pc_to_status[i]="-1"

    #############################
    return


def extractR(instr):  # instruction is of type string, for ex, 0x00011101
    variable = {'opcode': '', 'funct3': '', 'funct7': '', 'rd': '',
                'rs1': '', 'rs2': '', 'instr_type': '', 'operation': ''}
    bin_instr = bin(int(instr, 16))[2:].zfill(32)
    variable['opcode'] = bin_instr[25:32]
    variable['rd'] = bin_instr[20:25]
    variable['funct3'] = bin_instr[17:20]
    variable['rs1'] = bin_instr[12:17]
    variable['rs2'] = bin_instr[7:12]
    variable['funct7'] = bin_instr[0:7]
    return variable # [opcode, rd, funct3, rs1, rs2, funct7]


def extractS(instr):  # instruction is of type string, for ex, 0x00011101
    # global variable
    variable = {'opcode': '', 'funct3': '', 'funct7': '', 'rd': '',
                'rs1': '', 'rs2': '', 'instr_type': '', 'operation': ''}
    bin_instr = bin(int(instr, 16))[2:].zfill(32)
    variable['opcode'] = bin_instr[25:32]
    imm1 = bin_instr[20:25]
    variable['funct3'] = bin_instr[17:20]
    variable['rs1'] = bin_instr[12:17]
    variable['rs2'] = bin_instr[7:12]
    imm2 = bin_instr[0:7]
    variable['imm'] = imm2+imm1
    return variable # [opcode, funct3, rs1, rs2, imm]


def extractI(instr):  # instruction is of type string, for ex, 0x00011101
    # global variable
    variable = {'opcode': '', 'funct3': '', 'funct7': '', 'rd': '',
                'rs1': '', 'rs2': '', 'instr_type': '', 'operation': ''}
    bin_instr = bin(int(instr, 16))[2:].zfill(32)
    variable['opcode'] = bin_instr[25:32]
    variable['rd'] = bin_instr[20:25]
    variable['funct3'] = bin_instr[17:20]
    variable['rs1'] = bin_instr[12:17]
    variable['imm'] = bin_instr[0:12]

    return variable # [opcode, rd, funct3, rs1, imm]


def extractSB(instr):  # instruction is of type string, for ex, 0x00011101
    # global variable
    variable = {'opcode': '', 'funct3': '', 'funct7': '', 'rd': '',
                'rs1': '', 'rs2': '', 'instr_type': '', 'operation': ''}
    bin_instr = bin(int(instr, 16))[2:].zfill(32)
    variable['opcode'] = bin_instr[25:32]
    variable['funct3'] = bin_instr[17:20]
    variable['rs1'] = bin_instr[12:17]
    variable['rs2'] = bin_instr[7:12]

    variable['imm'] = bin_instr[0] + bin_instr[7] + \
        bin_instr[1:7] + bin_instr[20:24] + '0'

    return variable # [opcode, funct3, rs1, rs2, imm]


def extractU(instr):  # instruction is of type string, for ex, 0x00011101
    # global variable
    variable = {'opcode': '', 'funct3': '', 'funct7': '', 'rd': '',
                'rs1': '', 'rs2': '', 'instr_type': '', 'operation': ''}
    bin_instr = bin(int(instr, 16))[2:].zfill(32)
    variable['opcode'] = bin_instr[25:32]
    variable['rd'] = bin_instr[20:25]
    variable['imm'] = bin_instr[0:20]+'0'*12

    return variable # [opcode, rd, imm]


def extractUJ(instr):  # instruction is of type string, for ex, 0x00011101
    # global variable
    variable = {'opcode': '', 'funct3': '', 'funct7': '', 'rd': '',
                'rs1': '', 'rs2': '', 'instr_type': '', 'operation': ''}
    bin_instr = bin(int(instr, 16))[2:].zfill(32)
    variable['opcode'] = bin_instr[25:32]
    variable['rd'] = bin_instr[20:25]

    variable['imm'] = bin_instr[0]+bin_instr[12:20] + \
        bin_instr[11]+bin_instr[1:11]+'0'

    return variable # [opcode, rd, imm]


def decodeR(variable):  # funct3, funct7):

    funct3 = variable['funct3']
    funct7 = variable['funct7']

    operation = 'error'
    if (funct3 == '000'):
        if (funct7 == '0000000'):
            operation = 'add'
        elif (funct7 == '0100000'):
            operation = 'sub'
        elif (funct7 == '0000001'):
            operation = 'mul'
    elif (funct3 == '001' and funct7 == '0000000'):
        operation = 'sll'
    elif (funct3 == '010' and funct7 == '0000000'):
        operation = 'slt'
    elif (funct3 == '100' and funct7 == '0000000'):
        operation = 'xor'
    elif (funct3 == '100' and funct7 == '0000001'):
        operation = 'div'
    elif (funct3 == '101'):
        if (funct7 == '0000000'):
            operation = 'srl'
        elif (funct7 == '0100000'):
            operation = 'sra'
    elif (funct3 == '110' and funct7 == '0000000'):
        operation = 'or'
    elif (funct3 == '110' and funct7 == '0000001'):
        operation = 'rem'
    elif (funct3 == '111' and funct7 == '0000000'):
        operation = 'and'
    return operation


def decodeS(variable):  # funct3):
    global branch_predicted
    branch_predicted=[]
    branch_predicted.append("predicted not taken")
    funct3 = variable['funct3']
    operation = 'error'
    if (funct3 == '000'):
        operation = 'sb'
    elif (funct3 == '001'):
        operation = 'sh'
    elif (funct3 == '010'):
        operation = 'sw'
    return operation


def decodeI(variable):  # opcode, funct3):
    global branch_predicted
    branch_predicted=[]
    opcode = variable['opcode']
    funct3 = variable['funct3']
    operation = 'error'
    if (opcode == "0000011"):
        if (funct3 == '000'):
            operation = 'lb'
        elif (funct3 == '001'):
            operation = 'lh'
        elif (funct3 == '010'):
            operation = 'lw'
    elif (opcode == "0010011"):
        if (funct3 == '111'):
            operation = 'andi'
        elif (funct3 == '110'):
            operation = 'ori'
        elif (funct3 == '000'):
            operation = 'addi'
    elif (opcode == "1100111"):
        if (funct3 == '000'):
            operation = 'jalr'
            branch_predicted=[]
            branch_predicted.append("predicted not taken")
    return operation


def decodeSB(variable):  # funct3):
    global branch_predicted
    branch_predicted = []
    branch_predicted.append("predicted not taken")
    funct3 = variable['funct3']
    operation = 'error'
    if(funct3 == "000"):
        operation = "beq"
    elif(funct3 == "001"):
        operation = "bne"
    elif(funct3 == "100"):
        operation = "blt"
    elif(funct3 == "101"):
        operation = "bge"
    return operation


def decodeU(variable):  # opcode):
    opcode = variable['opcode']
    operation = 'error'
    if(opcode == "0010111"):
        operation = "auipc"
    elif(opcode == "0110111"):
        operation = "lui"
    return operation


# fetch

def fetch(P):  # PC is of type string 0x0
    global message
    global PC_temp
    global fetch_buffer

    PC_temp[fetch_counter] = P + 4
    message[0] = "FETCH:           \nPC_temp -> " + hex(P+4) + "    \nFetched instruction - " + instructions[P]
    
    fetch_buffer.append(readInstrCache(P)) ##now adding it to queue instead of returning
    ##return instructions[PC]  # string or int


# decode


def get_reg_val(reg):
    return get_signed(registers[get_signed(reg)])


def decode(instr):
    global message
    global decode_buffer
    bin_instr = "{0:032b}".format(int(instr, 16))

    opcode = bin_instr[25:32]

    operation = 'error'
    instr_type = 'error'

    reg_list = []

    to_stall = False

    if(opcode == "0110011"):
        instr_type = 'R'
        variable = extractR(instr)
        operation = decodeR(variable)
        reg_list = [get_reg_val(variable['rs1']), get_reg_val(variable['rs2'])]

    elif(opcode == "0100011"):
        instr_type = 'S'
        variable = extractS(instr)
        operation = decodeS(variable)
        reg_list = [get_reg_val(variable['rs1'])]


    elif(opcode == "0000011" or opcode == "0010011" or opcode == "1100111"):
        instr_type = 'I'
        variable = extractI(instr)
        operation = decodeI(variable)
        reg_list = [get_reg_val(variable['rs1'])]

    elif(opcode == "1100011"):
        instr_type = 'SB'
        variable = extractSB(instr)
        operation = decodeSB(variable)
        reg_list = [get_reg_val(variable['rs1']), get_reg_val(variable['rs2'])]

    elif(opcode == "0010111" or opcode == "0110111"):
        instr_type = 'U'
        variable = extractU(instr)
        operation = decodeU(variable)  # code_list[0])
        reg_list = []

    elif(opcode == "1101111"):
        instr_type = 'UJ'
        variable = extractUJ(instr)  # code_list = extractUJ(instr)
        global branch_predicted
        branch_predicted=[]
        branch_predicted.append("predicted not taken")
        operation = 'jal'
        reg_list = []

    


    global number_of_data_hazards
    global num_of_stall_temp
    if stall:
        if (variable["rs1"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs1"],2)]>0):
            to_stall = True
            num_of_stall_temp +=1
            return True, variable["rs1"]
        if (variable["rs2"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs2"],2)]>0):
            to_stall = True, variable["rs2"]
            num_of_stall_temp +=1
            return True, variable["rs2"]

    variable['instr_type'] = instr_type
    variable['operation'] = operation

    #check for data hazard in rs1 and rs2
    if(data_frwd ==1):
        # if(variable["rs1"]!=variable["rs2"]):
        #     # E to E
        #     if(variable["rs1"]!="" and  registers_bool[int("0b"+variable["rs1"],2)] ==2):
        #         variable["rs1"]= execute_buffer[0][1]["rd"]
        #     if(variable["rs2"]!="" and  registers_bool[int("0b"+variable["rs2"],2)] ==2):
        #         variable["rs2"]= execute_buffer[0][1]["rd"]
        #     # M to E
        #     if(variable["rs1"]!="" and registers_bool[int("0b"+variable["rs1"],2)] ==1):
        #          variable["rs1"]= memory_buffer[0][2]["rd"]
        #     if(variable["rs2"]!="" and registers_bool[int("0b"+variable["rs2"],2)] ==1):
        #          variable["rs2"]= memory_buffer[0][2]["rd"]
    
        #     # M to M ------------------
        # else:
        #     # E to E
        #     if(variable["rs1"]!="" and  registers_bool[int("0b"+variable["rs1"],2)] ==2):
        #         variable["rs1"]= execute_buffer[0][1]["rd"]
        #         variable["rs2"]= execute_buffer[0][1]["rd"]
        #     # M to E
        #     if(variable["rs1"]!="" and registers_bool[int("0b"+variable["rs1"],2)] ==1):
        #          variable["rs1"]= memory_buffer[0][2]["rd"]
        #          variable["rs2"]= memory_buffer[0][2]["rd"]
    
        #     # M to M ------------------
        ############################ CHANGED ######################################    
        ##yaha agr purani instr execute me se just nikli hai to register 
        #me execute se aae hui value dalegi na ki already stored value
        global data_hazard_path
        if(instr_type=="R" or instr_type=="SB"):
            if(variable["rs1"]!=variable["rs2"]):
                # E to E
                if(variable["rs1"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs1"],2)] ==2):
                    reg_list[0]= execute_buffer[-1][0]
                    number_of_data_hazards+=1 
                    data_hazard_path.append("data hazard solved using E to E forwarding.")  
                if(variable["rs2"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs2"],2)] ==2):
                    reg_list[1]= execute_buffer[-1][0]
                    number_of_data_hazards+=1
                    data_hazard_path.append("data hazard solved using E to E forwarding.")
                # M to E
                if(variable["rs1"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs1"],2)] ==1):
                    reg_list[0]= memory_buffer[-1][1]
                    number_of_data_hazards+=1
                    data_hazard_path.append("data hazard solved using M to E forwarding.") 
                if(variable["rs2"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs2"],2)] ==1):
                     reg_list[1]= memory_buffer[-1][1]
                     number_of_data_hazards+=1
                     data_hazard_path.append("data hazard solved using M to E forwarding.")
        
                # M to M ------------------
            else:
                # E to E
                if(variable["rs1"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs1"],2)] ==2):
                    reg_list[0]= execute_buffer[-1][0]
                    reg_list[1]= execute_buffer[-1][0]
                    number_of_data_hazards+=1
                    data_hazard_path.append("data hazard solved using E to E forwarding.")
                # M to E
                if(variable["rs1"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs1"],2)] ==1):
                    reg_list[0]= memory_buffer[-1][1]
                    reg_list[1]= memory_buffer[-1][1]
                    number_of_data_hazards+=1
                    data_hazard_path.append("data hazard solved using M to E forwarding.")
            
            #reg_list = [get_reg_val(variable['rs1']), get_reg_val(variable['rs2'])]
            
            
       
        elif(instr_type=="I" or instr_type=="S"):
            
            if(variable["rs1"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs1"],2)] ==2):
                    reg_list[0]= execute_buffer[-1][0]
                   
            # M to E
            if(variable["rs1"] not in ["", "00000"] and registers_bool[int("0b"+variable["rs1"],2)] ==1):
                 reg_list[0]= memory_buffer[-1][0]
            
        
            
        ##############################################################################
    
    # jump and branch in decode

    global PC
    global PC_temp
    global PC_temp2
    ###################
    global number_of_cycles
    global number_of_control
    global number_of_stalls
    global branch_mis
    
    ###################
    if (operation == "jalr"):
        PC_temp[decode_counter] = reg_list[0] + get_signed(variable["imm"])
        PC_temp2[decode_counter] = PC[decode_counter]+4
        #############################
        number_of_cycles+=1
        number_of_control+=1
        number_of_stalls+=1
        branch_mis+=1
        ######################
    elif (operation == "jal"):
        PC_temp[decode_counter] = PC[decode_counter] + get_signed(variable["imm"])
        PC_temp2[decode_counter] = PC[decode_counter]+4
        #############################
        number_of_cycles+=1
        number_of_control+=1
        number_of_stalls+=1
        branch_mis+=1
        ######################
    elif (instr_type == "SB"):
        op1 = reg_list[0]
        op2 = reg_list[1]
        if type(op1)==str:
            op1 = int(op1, 16)
        if type(op2)==str:
            op2 = int(op2, 16)
        imm = get_signed(variable['imm'])
        PC_temp2[decode_counter] = -1
        #########3
        number_of_control+=1
        branch_mis+=1
        ################3
        if(operation == "beq"):
            if(op1 == op2):
                PC_temp[decode_counter] = imm+PC[decode_counter]
                PC_temp2[decode_counter] = imm+PC[decode_counter]-4
                #############################
                number_of_cycles+=1
                number_of_stalls+=1
                ######################
        if(operation == "bne"):
            if(op1 != op2):
                PC_temp[decode_counter] = imm+PC[decode_counter]
                PC_temp2[decode_counter] = imm+PC[decode_counter]-4
                ############3
                number_of_stalls+=1
                number_of_cycles+=1
                ############################
        if(operation == "blt"):
            if(op1 < op2):
                PC_temp[decode_counter] = imm+PC[decode_counter]
                PC_temp2[decode_counter] = imm+PC[decode_counter]-4
                #############################
                number_of_cycles+=1
                number_of_stalls+=1
                ######################

        if(operation == "bge"):
            if(op1 >= op2):
                PC_temp[decode_counter] = imm+PC[decode_counter]
                PC_temp2[decode_counter] = imm+PC[decode_counter]-4
                #############################
                number_of_cycles+=1
                number_of_stalls+=1
                ######################

        if (PC_temp[decode_counter] == -1):
            PC_temp2[decode_counter] = PC[decode_counter]

    PC[decode_counter] = PC_temp[decode_counter]

    if(variable["rd"]!="" ):
        registers_bool[int("0b"+variable["rd"],2)]=3
    message[1] = "\nDECODE:          \nIntruction Type - " + instr_type + "    \nOperation - " + operation + "    \nRegister values are read."
    
    decode_buffer.append([reg_list, variable])
    

    global number_of_stalls_ch
    global number_of_stalls_dh
    if stall==True:
        if variable["operation"] in ["beq","bne","bge","blt","jal","jalr"]:
            if num_of_stall_temp>0:
                number_of_stalls_ch += num_of_stall_temp
            num_of_stall_temp =0
        else:
            #number_of_stalls_dh += num_of_stall_temp
            num_of_stall_temp =0

    return False, -1
##??????????????????????????????????????????????????????????????????

def get_signed(value):
    val = value
    if(val==""):
        return 0
    if (len(val) == 5):  # registers
        return int('0b'+val, 2)
    if (value[:2] == '0b'):
        val = value[2:].zfill(32)
    if (value[:2] == '0x'):
        val = bin(int(value, 16))[2:].zfill(32)
    if (val[0] == '0'):
        return int('0b'+val, 2)
    else:
        inv = ''
        for bit in val:
            inv += str(1 ^ int(bit))
        return -1*(int('0b'+inv, 2)+1)


def shiftRightLogical(n, m):  # shift n right by m bits
    if (n >= 0):
        return n >> m
    s = ''
    b = bin(-n)[2:].zfill(32)
    ns = ''
    for bit in b:
        ns += str(1 ^ int(bit))
    ns = bin(int(ns, 2)+1)[-32:]
    shifted = '0'*m + ns[:32-m]
    return int('0b'+shifted, 2)

# execute


def executeR(reg_list, variable):

    operation = variable['operation']

    op1 = reg_list[0]
    op2 = reg_list[1]
    if (type(op1)==str):
        op1 = int(op1, 16)
    if (type(op2)==str):
        op2 = int(op2, 16)

    val = 0

    if (operation == 'add'):
        val = op1 + op2

    elif (operation == 'and'):
        val = op1 & op2

    elif (operation == 'or'):
        val = op1 | op2

    elif (operation == 'sll'):
        val = op1 << op2

    elif (operation == 'slt'):
        if(op1 < op2):
            val = 1
        else:
            val = 0

    elif (operation == 'sra'):  # arithmetic shift right
        val = op1 >> op2

    elif (operation == 'srl'):  # logical shift right
        # val= op1 >> op2
        val = shiftRightLogical(op1, op2)

    elif (operation == 'sub'):
        val = op1 - op2

    elif (operation == 'xor'):
        val = op1 ^ op2

    elif (operation == 'mul'):
        val = op1 * op2

    elif (operation == 'div'):
        val = op1 // op2

    elif (operation == 'rem'):
        val = op1 % op2

    return val


def executeU(reg_list, variable):  # rd imm

    # --U type dont use signed

    operation = variable['operation']

    imm = int('0b'+variable['imm'], 2)

    if(operation == 'auipc'):
        # val = PC + imm
        val = PC[execute_counter] + imm

    elif(operation == 'lui'):

        val = imm

    return val


def executeSB(reg_list, variable):  # rs1, rs2, imm
    global PC_temp

    operation = variable['operation']

    imm = get_signed(variable['imm'])

    op1 = reg_list[0]
    op2 = reg_list[1]
    
    return PC_temp2[execute_counter]

    if(operation == "beq"):
        if(op1 == op2):
            PC_temp[execute_counter] = imm+PC[execute_counter]
            return imm+PC[execute_counter]-4

    if(operation == "bne"):
        if(op1 != op2):
            PC_temp[execute_counter] = imm+PC[execute_counter]
            return imm+PC[execute_counter]-4

    if(operation == "blt"):
        if(op1 < op2):
            PC_temp[execute_counter] = imm+PC[execute_counter]
            return imm+PC[execute_counter]-4

    if(operation == "bge"):
        if(op1 >= op2):
            PC_temp[execute_counter] = imm+PC[execute_counter]
            return imm+PC[execute_counter]-4

    # PC_temp[execute_counter] = PC[execute_counter]
    return PC[execute_counter]  # -----


def executeUJ(reg_list, variable):  # rd imm
    global PC_temp
    # [rd, imm] = [get_signed(i) for i in reg_list]
    imm = get_signed(variable['imm'])
    # PC_temp[execute_counter] = PC[execute_counter]+imm
    return PC_temp2[execute_counter] #PC[execute_counter]+4


def executeI(reg_list, variable):  # rd rs1 imm
    global PC_temp
    operation = variable['operation']
    
    op1 = reg_list[0]
    op2 = get_signed(variable['imm'])        
        
    ans = 0
    
    if (operation == 'addi'):
        ans = op1 + op2
    elif (operation == 'andi'):
        ans = op1 & op2
    elif (operation == 'ori'):
        ans = op1 | op2
    elif (operation in ['lb', 'lh', 'lw']):
        ans = op1 + op2  # calculating address
    elif (operation == 'jalr'):
        # ans = PC[execute_counter] + 4
        ans = PC_temp2[execute_counter]
        # PC_temp[execute_counter] = op1 + op2
    return ans


def executeS(reg_list, variable):  # rs1 rs2 imm

    ans = reg_list[0] + get_signed(variable['imm'])
    return ans


def execute(parameters):
    [reg_list, variable] = parameters
    # global PC
    # global PC_temp
    # global PC_temp2
    global message
    global execute_buffer
    # PC_temp2 = -1
    instr_type = variable['instr_type']
    var = 0
    if (instr_type == 'R'):
        var = executeR(reg_list, variable)  # returns value to be stored in rd
    elif (instr_type == 'S'):
        # returns effective address imm(rs1) whose value is to be stored in rs2
        var = executeS(reg_list, variable)
    elif (instr_type == 'I'):
        # returns value to be stored in rd or effective address imm(rs1)
        var = executeI(reg_list, variable)
    elif (instr_type == 'SB'):
        var = executeSB(reg_list, variable)  # return PC temp
    elif (instr_type == 'U'):
        var = executeU(reg_list, variable)  # returns required value
    elif (instr_type == 'UJ'):
        # returns PC temp and return address of jump instruction %list%
        var = executeUJ(reg_list, variable)
    
    if(variable["rd"] not in ["", "00000"] and registers_bool[int("0b"+variable["rd"],2)]==3):
        registers_bool[int("0b"+variable["rd"],2)] -= 1
    
    # PC[execute_counter] = PC_temp[execute_counter]
    # if (PC_temp2 != -1):
    #     PC = PC_temp2
    message[2] = "\nEXECUTE:         \nPC -> " + hex(PC[execute_counter]) + "    \nReturned value - " + str(var)
    execute_buffer.append([var, variable])
    #return var


# memory access

def sign_extend_hex(s):  # '12031312' returns '210481200'
    sign = '0'
    num = int('0x'+s[0], 16)
    if (num > 7):
        sign = 'F'
    ne = 8-len(s)
    return (sign*ne)+s


def memoryAccess(parameters):
    [var, variable] = parameters
    # global PC
    global memory
    global message
    global memory_buffer
    global number_of_data_hazards
    if(variable["rd"] not in ["", "00000"] and registers_bool[int("0b"+variable["rd"],2)]==2):
        registers_bool[int("0b"+variable["rd"],2)] -= 1

    operation = variable['operation']
    instr_type = variable['instr_type']
    memread = ""
    
    if (instr_type == 'S'):
        message[3] = '\nMEMORY ACCESS:   \nMemory at ' + hex(var) + ' is updated.'

        registerValue = registers[get_signed(variable['rs2'])]

        # M to M
        if data_frwd:
            if(len(memory_buffer)>0):
                if (memory_buffer[0][2]["operation"] in ["lw", "lh", "lb"]): # prev instr
                    if (variable["rs2"] == memory_buffer[0][2]["rd"]):
                        registerValue = memory_buffer[0][1]
                        number_of_data_hazards+=1
                        data_hazard_path.append("data hazard solved using M to E forwarding.")
        toStore = None
        if (operation == 'sb'):
            toStore = memory.get(var, '00000000')[:6] + registerValue[-2:]
        elif (operation == 'sh'):
            toStore = memory.get(var, '00000000')[:4] + registerValue[-4:]
        elif (operation == 'sw'):
            toStore = registerValue[-8:]
        writeDataCache(var, toStore)
    
    elif (instr_type == 'I'):
        message[3] = '\nMEMORY ACCESS:   \nData at ' + hex(var) + ' is accessed.'
        memCache = sign_extend_hex(readDataCache(var))
        if (operation == 'lb'):
            memread = '0x' + memCache[-2:]
        elif (operation == 'lh'):
            memread = '0x' + memCache[-4:]
        elif (operation == 'lw'):
            memread = '0x' + memCache[-8:]
    
    else:
        message[3] = '\nMEMORY ACCESS:   \nNo Action'
    
    if memread == "":
        memread = var

    memory_buffer.append([var, memread, variable])
    ##return memread

# register update


def int_to_signed(val):
    if (type(val)==str and len(val)==10 and val[:2]=='0x'):
        return val
    if (val < 0):
        s = bin(-1*val)[2:].zfill(32)
        s = s[-32:]
        rs = '0b'
        for bit in s:
            rs += str(int(1 ^ int(bit)))
        return '0x'+hex(int(rs, 2)+1)[2:].zfill(8)
        # return hex(val+(1<<32))
    return '0x'+hex(val)[2:].zfill(8)


def registerUpdate(parameters):
    [var, memread, variable] = parameters
    global registers
    global message
    global registers_bool
    ##################
    global number_of_load_store
    ########################33  
    if(variable["rd"] not in ["", "00000"] and registers_bool[int("0b"+variable["rd"],2)]==1):
        registers_bool[int("0b"+variable["rd"],2)] -= 1

    operation = variable['operation']
    instr_type = variable['instr_type']
    reg = get_signed(variable['rd'])

    if (instr_type == 'R'):
        registers[reg] = int_to_signed(var)
        message[4] = '\nREGISTER UPDATE: \nRegister x' + str(reg) + ' is updated.'
    elif (instr_type == 'S'):
        ###########################
        number_of_load_store+=1
        ###########################
        message[4] = '\nREGISTER UPDATE: \nNo Action'
    elif (instr_type == 'I'):
        message[4] = '\nREGISTER UPDATE: \nRegister x' + str(reg) + ' is updated.'
        if (operation == 'jalr'):
            registers[reg] = '0x' + \
                hex(var)[2:].zfill(8)
        elif (operation in ['lb', 'lh', 'lw']):
            registers[reg] = memread
            ###############################
            number_of_load_store+=1
            #############################
        elif (operation in ['andi', 'ori', 'addi']):
            registers[reg] = int_to_signed(var)
    elif (instr_type == 'SB'):
        message[4] = '\nREGISTER UPDATE: \nNo Action'
    elif (instr_type == 'U'):
        message[4] = '\nREGISTER UPDATE: \nRegister x' + str(reg) + ' is updated.'
        registers[reg] = '0x' + hex(var)[2:].zfill(8)
    elif (instr_type == 'UJ'):
        message[4] = '\nREGISTER UPDATE: \nRegister x' + str(reg) + ' is updated.'
        registers[reg] = '0x' + hex(var)[2:].zfill(8)

    # if(variable["rd"] != ""):
    #     registers_bool[int("0b"+variable["rd"],2)] = 0

    # ----------------------------------------------
    registers[0] = '0x00000000'
    return

# main function

reset_all()
readfile('test.txt')

def data_forwarding():
    global data_frwd
    global stall
    data_frwd = 1
    stall = False

import sys

fil = open("ksh3.out", "w")
sys.stdout = fil

def main1():
    
    # global stall
    # stall = False

    global PC
    global register_counter
    global memory_counter
    global execute_counter
    global decode_counter
    global fetch_counter
    '''if(forwarding==True):
        data_forwarding()'''
        
    global f
    global to_stall
    #f = 0
    #to_stall = False

        
    #print(registers)
    #print()
    #fetch()
    # print(f)
    if(f!=-2 and instructions[f]=="text_end"):
        # print("end of code")
        f=-2
        fetch_counter = -2
        # break
    ############
    global buffers
    global pc_to_status
    global status_to_pc
    global number_of_cycles
    global number_of_instrs
    global number_of_load_store
    global number_of_alu
    global number_of_control
    global number_of_stalls
    global branch_mis
    global number_of_control
    global num_of_stall_temp
    #global f
    #global to_stall
    number_of_cycles+=1
    for i in pc_to_status:
        pc_to_status[i]="-1"
    #############
    
    buffers = ["EMPTY" for _ in range(4)]
    if (register_counter >= 0 and len(memory_buffer)>0):
        b = memory_buffer[-1]
        buffers[3] = "Var: " + str(b[0]) + "\t Memread: " + str(b[1]) + "\n"
    if (memory_counter >= 0 and len(execute_buffer)>0):
        b = execute_buffer[-1]
        buffers[2] = "Var: " + str(b[0]) + "\n"
    if (execute_counter >= 0 and len(decode_buffer)>0):
        b = decode_buffer[-1]
        buffers[1] = ""
        for i in b[1]:
            buffers[1] += i + ": " + str(b[1][i]) + "\n"
    if (decode_counter >= 0 and len(fetch_buffer)>0):
        b =  "{0:032b}".format(int(fetch_buffer[-1], 16))
        buffers[0] = "Instruction: " + b[0] + "\n"
    buffers[0] = "Fetch Buffer => "+buffers[0]
    buffers[1] = "Decode Buffer => "+buffers[1]
    buffers[2] = "Execute Buffer => "+buffers[2]
    buffers[3] = "Memory Buffer => "+buffers[3]
    
    if(register_counter>=0 ):
        PC[register_counter] = register_counter
        registerUpdate(memory_buffer[0])
        ###############
        pc_to_status[register_counter]="Register_Update"
        status_to_pc["Register_Update"]=register_counter

        if(memory_buffer[0][2]['operation'] not in ["lw","sw","lb","sb","lh","sh"]):
            number_of_instrs+=1
        
        if(memory_buffer[0][2]['operation'] in ["add","addi","and","or","sll","slt","sra","srl","sub","xor","mul","div","rem","andi","ori","sb","sw","sh","lb","lh","lw"]):
            number_of_alu+=1
        
        
        ##################

    if(memory_counter>=0 ):
        PC[memory_counter] = memory_counter
        memoryAccess(execute_buffer[0])
        ###############
        pc_to_status[memory_counter]="Memory_Write"
        status_to_pc["Memory_Write"]=memory_counter
        ##################

    if(execute_counter>=0 ):
        PC[execute_counter] = execute_counter
        execute(decode_buffer[0])
        ###############
        pc_to_status[execute_counter]="Execute"
        status_to_pc["Execute"]=execute_counter
        ##################

    if(decode_counter>=0):
        PC[decode_counter] = decode_counter
        ###############
        pc_to_status[decode_counter]="Decode"
        status_to_pc["Decode"]=decode_counter
        ##################
        if stall:
            to_stall, reg = decode(fetch_buffer[0])
            if to_stall:
                num_of_stall_temp+=1
                number_of_stalls+=1
                if(register_counter>=0 ):
                    memory_buffer.pop(0)
                if(memory_counter>=0 ):
                    execute_buffer.pop(0)
                if(execute_counter>=0 ):
                    decode_buffer.pop(0)

                register_counter = memory_counter
                memory_counter = execute_counter
                execute_counter = -4
                if (memory_counter >= 0): # for jump instructions
                    if (PC_temp[memory_counter] != memory_counter+4):
                        # flush
                        decode_counter = -4
                        execute_counter = -8
                        fetch_buffer.pop(0)
                        decode_buffer.pop(0)
                        fetch_counter = PC[memory_counter]
                return
        else:
            to_stall, reg = decode(fetch_buffer[0])
        if (decode_counter >= 0): # for jump instructions
            if (PC_temp[decode_counter] != decode_counter+4):
                # flush
                if(register_counter>=0 ):
                    memory_buffer.pop(0)
                if(memory_counter>=0 ):
                    execute_buffer.pop(0)
                if(execute_counter>=0 ):
                    decode_buffer.pop(0)
                if(decode_counter>=0):
                    fetch_buffer.pop(0)
                register_counter = memory_counter
                memory_counter = execute_counter
                execute_counter = decode_counter
                fetch_counter = PC[decode_counter]
                decode_counter = -4
                # execute_counter = -8
                # decode_buffer.pop(0)
                # execute_buffer.pop(0)
                # fetch_buffer.pop(0)
                # decode_buffer.pop(0)
                return
        

    if(fetch_counter>=0):# and f!=-2):
        PC[fetch_counter] = fetch_counter
        fetch(fetch_counter)
        ###############
        pc_to_status[fetch_counter]="Fetch"
        status_to_pc["Fetch"]=fetch_counter
        ##################


    if(register_counter>=0 ):
       memory_buffer.pop(0)
    if(memory_counter>=0 ):
       execute_buffer.pop(0)
    if(execute_counter>=0 ):
       decode_buffer.pop(0)
    if(decode_counter>=0):
        fetch_buffer.pop(0)

    if (register_counter == -2):
        return


    # if(execute_counter < 0 ):   ## do only if execute operation is not performed
    #     PC= PC +4


    # if (f!=-2):
    if (fetch_counter>=0):
        f = PC_temp[fetch_counter]
    
    register_counter = memory_counter
    memory_counter = execute_counter
    execute_counter = decode_counter
    decode_counter = fetch_counter
    fetch_counter = f

    if (execute_counter >= 0): # for jump instructions
        if (PC_temp[execute_counter] != execute_counter+4):
            # flush
            decode_counter = -4
            # execute_counter = -8
            fetch_buffer.pop(0)
            # decode_buffer.pop(0)
            fetch_counter = PC[execute_counter]
    


def print_stmt():
    global number_of_instrs
    global stats
    print("Total number of cycles: ",number_of_cycles)
    number_of_instrs+=number_of_load_store
    print("Total instructions executed: ",number_of_instrs)
    print("CPI: ",number_of_cycles/number_of_instrs)
    print("Number of Data-transfer (load and store) instructions executed: ",number_of_load_store)
    print("Number of ALU instructions executed: ",number_of_alu)
    print("Number of Control instructions executed: ",number_of_control)
    print("Number of stalls/bubbles in the pipeline: ",number_of_stalls)
    print("Number of data hazards: ",number_of_data_hazards)
    print("Number of control hazards: ",branch_mis)
    print("number of mispredictions: ",branch_mis)
    print("number of stalls due to control hazards: ",number_of_stalls_ch)
    print("number of stalls due to data hazards: ",number_of_stalls-number_of_stalls_ch)
    stats=["Total number of cycles: "+str(number_of_cycles), "Total instructions executed: "+str(number_of_instrs), "CPI: "+str(number_of_cycles/number_of_instrs),"Number of Data-transfer (load and store) instructions executed: "+str(number_of_load_store),"Number of control hazards: "+str(branch_mis),
    "Number of ALU instructions executed: "+str(number_of_alu),"Number of Control instructions executed: "+str(number_of_control),"Number of stalls/bubbles in the pipeline: "+str(number_of_stalls),
    "Number of data hazards: "+str(number_of_data_hazards),"number of mispredictions: "+str(branch_mis)]
    print(registers)



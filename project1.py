# Reety Gyawali 1001803756
# Rakshav Patel – 10011941754

# Get input file and store it in a variable
input_file = "Input 4.txt"
# input_file = input("Enter input file name: ")

output_file = "Output " + input_file[6] + ".txt"

#array that will hold diffrent state of transaction
input_operation = []
A = "active"
B = "abort"
C = "committed"
E = "abort"

#array that will hold transaction table items 
transTableItem = []

#array to hold lock item
locTableItem = []

#will hold write and read transaction
RW_transaction = []
W = "write"
R = "Read"

# lock class this will hold diffrent elements of the lock tabel
class lock_table():
    def __init__(self, lock_sate, lock_item, t_id):
        self.lock_state = lock_sate # if its active or locked
        self.lock_item = lock_item  # if the item is already locked
        self.RW_transaction = []    # this is read or write transaction
        self.lockHoldBy = []        # holding lock for read or write
        self.lockHoldBy.append(t_id)
    def ChangeLock_State(self, lock_state):
        self.lock_state = lock_state
    def lockHoldBy(self, t_id):
        self.lockHoldBy.append(t_id)
    def waiting_transaction(self, t_id):
        self.RW_transaction.append(t_id) # waitinmg for items to be unlocked

# Reading and parsing each line in file 
try:
    with open(input_file, 'r') as input:
        lines = input.readlines()

    with open(output_file, 'w') as output:
        for line in lines:
            # Store transaction ID in variable
            t_id = line[1]
    
            if (line[0] == 'b'):
                # Begin transaction   
                modified_line = line.strip() + ' T' + t_id + ' begins.\n'
            elif (line[0] == 'e'):
                # Commit transaction 
                modified_line = line.strip() + ' T' + t_id + ' is committed.\n'
            elif (line[0] == 'r'):
                # Transaction readlocks item 
                item = line[3]
                modified_line = line.strip() + ' T' + t_id + ' reads item ' + item  + '\n'
            elif (line[0] == 'w'):
                # Transaction writelocks item 
                item = line[3]
                modified_line = line.strip() + ' T' + t_id + ' writes item ' + item  + '\n'
            
            output.write(modified_line)

    print("Output file created:", output_file)
except FileNotFoundError:
        print("Error: Input file not found.")



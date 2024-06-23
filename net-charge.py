#Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt" 
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr" 
insulin = bInsulin + aInsulin

#create a new dictionary with key pair and value
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}
#Note: Y, C, K, H, R, D, and E are the only amino acids that contribute to the net-charge calculation.

#seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
#print(seqCount)
ph = 0
while (ph <= 14):
    # netCharge = (
    # +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    # for x in ['k','h','r']}.values()))
    # -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    # for x in ['y','c','d','e']}.values())))
    
    #below stella code
    # netCharge = (
    # +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) for x in ['k','h','r']}.values()))
    #     -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) for x in ['y','c','d','e']}.values()))
    # )
    
    #below amer code
    netCharge = (
        +(sum({x: ((insulin.count(x)*(10**pKR[x]))/((10**ph)+(10**pKR[x]))) for x in ['k','h','r']}.values())) #positive charge
        -(sum({x: ((insulin.count(x)*(10**ph))/((10**ph)+(10**pKR[x]))) for x in ['y','c','d','e']}.values())) #negative charge
    )
    print('{0:.2f}'.format(ph), netCharge)
    ph +=1
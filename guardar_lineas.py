import sys
import random

        
    
def main(fileIN, fileOUT, porcentaje):
    with open(fileIN) as f_in:
        with open(fileOUT,'w') as f_out:
            for line in f_in:
                new_per=random.randint(1,100)
                if new_per<porcentaje:
                    f_out.write(line)
                        
                
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python3 {0} <name_file_in>  <name_file_out> <percentage>".format(sys.argv[0]))
    else:
        main(sys.argv[1],sys.argv[2],float(sys.argv[3]))

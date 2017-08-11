import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "a:b:c:d:e:")
    for op, value in opts:
        if op == "-a":
            a_valu = value
        elif op == "-b":
            b_value = value
        elif op == "-c":
            c_value = value
        elif op == "-d":
            d_value = value
        elif op == "-e":
            e_value = value
except getopt.GetoptError:
    print(sys.argv[0] + " : params are not defined well!")

print (a_valu, b_value, c_value, d_value, e_value)

'''
python CommandLineParameter.py -a "a-value"  -b "b-value" -c "c-value" -d "d-value" -e "e-value"
'''

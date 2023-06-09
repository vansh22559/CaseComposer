import os
import subprocess
n=0
for a in range(100):
    # Read the multi-line input from tc.py
    input_data = subprocess.run(["python3", "tc.py"], stdout=subprocess.PIPE, text=True).stdout
    print(a)
# Run the input data through working.out and store the output
    working_output = subprocess.check_output(["./working.out"], input=input_data, text=True).replace(" ", "").replace("\n", "")

# Run the input data through notworking.out and store the output
    not_working_output = subprocess.check_output(["./notworkin.out"], input=input_data, text=True).replace(" ", "").replace("\n", "")
    # print(not_working_output,working_output)
    # print(not_working_output==working_output)
# Write the output to separate files
    with open("tc1.csv", "a") as opfile:
        if working_output != not_working_output:
            opfile.write("{},{},{}\n".format(input_data.strip(), not_working_output.strip(), working_output.strip()))
            opfile.write("++++++++++++++++++++++++++++++++++++++++++++++\n")
            n += 1

print("number of failed TC = ",n)

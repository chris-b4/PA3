# Create trace files. Change bandwidth (bwd) and time as needed.

bwd = 60		# Change as needed
time = 60		# Change as needed
total_lines = time*1000

if int(bwd)>12:
	repeats = int(bwd/12)

	for t in range(total_lines):
		for n in range(repeats):
			print(t)

else:
	for t in range(0, total_lines, int(bwd)):
		print(t)

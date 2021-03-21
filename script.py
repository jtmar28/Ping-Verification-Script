import os
results_file = open("results.txt", "w")
ip_list = []
len(ip_list)
for ip in range(1,256):
  ip_list.append("192.168.1." + str(ip))
len(ip_list)
ip_list[0]
for ip in ip_list:
  response = os.popen(f"ping {ip} -n 1").read()
  if "Received = 1" and "Approximate" in response:
    results_file.write(f"UP {ip} Ping Successful" + "\n")
  else: 
    results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
results_file.close()

#cat ./results.txt
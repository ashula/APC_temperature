import paramiko

def ssh_cmd(ip,username,password,cmd):
       s=paramiko.SSHClient()
       s.set_missing_host_key_policy(paramiko.WarningPolicy())
       s.connect(ip,username=username,password=password,timeout=3.0)
       stdin,stdout,stderr = s.exec_command(cmd)
       for line in stdout:
           print line

if __name__ == "__main__":
    command = 'snmpwalk -c public -v 1 172.16.251.143   1.3.6.1.4.1.318.1.1.26.10.2.2.1.8.1'
    ssh_cmd(ip='172.16.251.152',username='nutanix',password='nutanix/4u',cmd=command)


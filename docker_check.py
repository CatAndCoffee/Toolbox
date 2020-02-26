#  -*-coding:utf8 -*-
import os
check_docker = {}
try:
   if os.path.isdir('/varlib/docker/etc/fstab'):
       check_docker['1.为容器创建独立的分区'] = os.popen('grep /varlib/docker/etc/fstab').read()
   else:
       check_docker['1.为容器创建独立的分区'] = '未找到file'
except:
   check_docker['1.为容器创建独立的分区'] = '在' + '/varlib/docker/etc/fstab' + '未找到'

try:
   check_docker['2.使用已更新过的Linux内核'] = os.popen('uname -r').read()
except:
   check_docker['2.使用已更新过的Linux内核'] = 'not found'

try:
   check_docker['3.只允许受信任的用户控制Docker deamon'] = os.popen('getent group docker').read()
except:
   check_docker['3.只允许受信任的用户控制Docker deamon'] = 'not found'

try:
   check_docker['4.审计Docker deamon'] = os.popen('auditctl -l | grep /usr/bin/docker').read()
except:
   check_docker['4.审计Docker deamon'] = '在' + '/usr/bin/docker' + '未找到'

try:
   check_docker['5.审计var/lib/docker'] = os.popen('auditctl -l | grep /usr/bin/docker').read()
except:
   check_docker['5.审计var/lib/docker'] = '在' + '/usr/bin/docker' + '未找到'

try:
   check_docker['6.审计/etc/docker'] = os.popen('auditctl -l | grep /etc/docker').read()
except:
   check_docker['6.审计/etc/docker'] = '在' + '/etc/docker' + '未找到'

try:
   f_dir_list = os.popen('systemctl show -p FragmentPath docker.service').read().split('=')[1]
   if f_dir_list == '\n':
       check_docker['7.审计docker.service'] = 'unqualified'
   else:
       infos = os.popen('auditctl -l | grep docker.service')
       check_docker['7.审计docker.service'] = infos
except:
   f_dir_list = os.popen('systemctl show -p FragmentPath docker.service').read().split('\n')
   check_docker['7.审计docker.service'] = '在' + str(f_dir_list) + '未找到'

try:
   f_dir_list = os.popen('systemctl show -p FragmentPath docker.socket').read().split('=')[1]
   if f_dir_list == '\n':
       check_docker['8.审计docker.socket'] = 'unqualified'
   else:
       infos = os.popen('auditctl -l | grep docker.socket')
       check_docker['8.审计docker.socket'] = infos
except:
   f_dir_list = os.popen('systemctl show -p FragmentPath docker.service').read().split('\n')
   check_docker['8.审计docker.socket'] = '在' + str(f_dir_list) + '未找到'

try:
   check_docker['9.审计/etc/default/docker'] = os.popen('auditctl -l | grep /etc/default/docker').read()
except:
   check_docker['9.审计/etc/default/docker'] = '在' + '/etc/default/docker' + '未找到'

try:
   check_docker['10.审计/etc/docker/daemon.json'] = os.popen('auditctl -l | grep /etc/docker/daemon.json').read()
except:
   check_docker['10.审计/etc/docker/daemon.json'] = '在' + '/etc/docker/daemon.json' + '未找到'


try:
   check_docker['11.审计/usr/bin/docker-containerd'] = os.popen('auditctl -l | grep /usr/bin/docker-containerd').read()
except:
   check_docker['11.审计/usr/bin/docker-containerd'] = '在' + '/usr/bin/docker-containerd' + '未找到'

try:
   check_docker['12.审计/usr/bin/docker-runc'] = os.popen('auditctl -l | grep /usr/bin/docker-runc').read()
except:
   check_docker['12.审计/usr/bin/docker-runc'] = '/usr/bin/docker-runc' + '未找到'

try:
   f = os.popen('ps -ef | grep docker').read()
   if 'icc=false' in f:
       check_docker['13.限制容器之间的网络流量'] = 'qualified'
   else:
       check_docker['13.限制容器之间的网络流量'] = 'unqualified'
except:
   check_docker['13.限制容器之间的网络流量'] = '未找到'

try:
   f = os.popen('ps -ef | grep docker').read()
   if 'iptables' in f or 'iptables=false':
       check_docker['14.允许Docker更改iptables'] = 'unqualified'
   else:
       check_docker['14.允许Docker更改iptables'] = 'qualified'
except:
   check_docker['14.允许Docker更改iptables'] = '未找到'

try:
   f = os.popen('ps -ef | grep docker').read()
   if 'insecure-registry' in f:
       check_docker['15.使用安全的镜像库'] = 'qualified'
   else:
       check_docker['15.使用安全的镜像库'] = 'unqualified'
except:
   check_docker['15.使用安全的镜像库'] = '未找到'

try:
   # check_docker['12.审计/usr/bin/docker-runc'] = os.popen('auditctl -l | grep /usr/bin/docker-runc').read()
   f_aufs = os.popen('docker info | grep -e "^Storage Driver:\s*aufs\s*$"').read()
   if f_aufs == '':
       check_docker['16.不使用aufs存储驱动'] = 'qualified'
   else:
       check_docker['16.不使用aufs存储驱动'] = 'unqualified'
except:
   check_docker['16.不使用aufs存储驱动'] = '未找到'

try:
   f_aufs = os.popen('ps -ef | grep docker').read()
   if '--tlsverify' in f_aufs and '--tlscacert' in f_aufs and '--tlscert' in f_aufs and '--tlskey' in f_aufs:
       check_docker['17.为Docker daemon配置TLS认证'] = 'qualified'
   else:
       check_docker['17.为Docker daemon配置TLS认证'] = 'unqualified'
except:
   check_docker['17.为Docker daemon配置TLS认证'] = '未找到'

# try:
   # check_docker['18.设置验证镜像库证书文件的权限'] = os.popen('stat -c %U:%G /etc/docker/certs.d/* | grep -v root:root').read()
# except:
#     check_docker['18.设置验证镜像库证书文件的权限'] = '在' + '/etc/docker/certs.d/*' + '未找到'

# try:
#     try:
#         check_docker['19.设置验证TLS CA证书文件的权限'] = os.popen('stat -c %U:%G <path to TLS CA certificate file> | grep -v root:root').read()
#     except:
#         check_docker['19.设置验证TLS CA证书文件的权限'] = os.popen('stat -c %a <path to TLS CA certificate file>').read()
# except:
#     check_docker['19.设置验证TLS CA证书文件的权限'] = 'not found'

# try:
#     try:
#         check_docker['20.设置验证Docker 服务器证书文件的权限'] = os.popen('stat -c %U:%G <path to Docker server certificate key file> | grep -v root:root').read()
#     except:
#         check_docker['20.设置验证Docker 服务器证书文件的权限'] = os.popen(
#             'stat -c %a <path to Docker server certificate key file>').read()
# except:
#     check_docker['20.设置验证Docker 服务器证书文件的权限'] = 'not found'

with open('check_docker.txt', 'w') as file:
   for v, k in check_docker.items():
       file.write('{v}:{k}'.format(v=v, k=k))
       file.write('\n')

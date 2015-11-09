def outside():
	x=5
	def inside():
		print x
	return inside
p=outside()
print type(p)
p()

def addone(myfunc):
	def addoneinside():
		return myfunc()+1
	return addoneinside
def oldie():
	return 3

newfunc=addone(oldie)
print oldie(),newfunc()


###finally

# def append_out(firstname):
# 	def append_in():
# 		print firstname() + ' khan'
# 	return append_in

# def firsty():
# 	return 'farhan'

# new=append_out(firsty)
# new()


def append_out(firstname):
	def append_in():
		print firstname() + ' khan'
	return append_in

@append_out
def firsty():
	return 'farhan'

firsty()
print __name__






     0      0 farhan:48117            104.16.105.204:http     ESTABLISHED
tcp        0      0 farhan:57458            del01s06-in-f20.1e:http ESTABLISHED
tcp      681      0 farhan.com:5000         farhan.com:59601        ESTABLISHED
tcp        0      0 farhan.com:27017        farhan.com:53647        ESTABLISHED
tcp        0      0 farhan:58700            kul06s14-in-f13.1:https ESTABLISHED
tcp        0      0 farhan.com:53647        farhan.com:27017        ESTABLISHED
tcp        0      0 farhan:60999            del01s06-in-f25.1:https ESTABLISHED
tcp        0      0 farhan:58614            104.16.104.204:http     ESTABLISHED
tcp        0      0 farhan:43473            104.16.12.8:http        ESTABLISHED
tcp        0      0 farhan:33716            sa-in-f95.1e100.n:https ESTABLISHED
tcp        0      0 farhan:43733            del01s06-in-f24.1:https ESTABLISHED
tcp        0      0 farhan:43016            104.16.36.249:http      ESTABLISHED
tcp        0      0 farhan:38723            ec2-50-19-86-168.:https CLOSE_WAIT 
tcp        0      0 farhan:39518            del01s06-in-f16.1:https ESTABLISHED
tcp        0      0 farhan.com:27017        farhan.com:53643        ESTABLISHED
tcp        0      0 farhan.com:53643        farhan.com:27017        ESTABLISHED
tcp        0      0 farhan:57192            68.232.44.121:https     ESTABLISHED
tcp        0      0 farhan:48664            del01s06-in-f13.1:https ESTABLISHED
tcp        0      0 farhan:57463            del01s06-in-f20.1e:http ESTABLISHED
tcp        0      1 farhan:38722            ec2-50-19-86-168.:https SYN_SENT   
tcp        0      0 farhan:50004            209-20-75-76.slice:http CLOSE_WAIT 
tcp        0      0 farhan:43476            104.16.12.8:http        ESTABLISHED
tcp        0      0 farhan:46242            ec2-54-80-241-137:45694 ESTABLISHED
tcp        0      1 farhan:38620            ec2-50-19-86-168.:https FIN_WAIT1  
tcp        0      0 farhan:43091            104.16.36.249:http      ESTABLISHED
tcp        0      0 farhan:46239            ec2-54-80-241-137:45694 ESTABLISHED
tcp        0      0 farhan:57465            del01s06-in-f20.1e:http ESTABLISHED
tcp        0      0 farhan:38194            del01s06-in-f3.1e1:http ESTABLISHED
tcp        0      0 farhan.com:59601        farhan.com:5000         ESTABLISHED
tcp        0      0 farhan:54786            del01s06-in-f5.1e1:http ESTABLISHED
tcp      682      0 farhan.com:5000         farhan.com:59416        CLOSE_WAIT 
tcp        0      0 farhan:43925            del01s06-in-f15.1:https ESTABLISHED
tcp        0      0 farhan:60142            del01s06-in-f7.1e1:http ESTABLISHED
tcp        0      0 farhan:49086            ec2-54-64-225-201.:http TIME_WAIT  
tcp        0      0 farhan:36652            productsearch.ubu:https ESTABLISHED
tcp        0      0 farhan:38282            del01s06-in-f14.1:https ESTABLISHED
tcp        0      0 farhan:39001            192.168.42.129:domain   TIME_WAIT  
tcp        0      0 farhan:57190            68.232.44.121:https     ESTABLISHED
tcp        0      0 farhan:53646            del01s07-in-f13.1:https ESTABLISHED
tcp        0      0 farhan:36743            ec2-50-17-236-38.c:http ESTABLISHED
tcp        0      0 farhan:42171            a23-205-213-177.de:http ESTABLISHED
tcp        0      0 farhan:56699            202.159.216.152:http    ESTABLISHED
tcp        0      0 farhan:57193            68.232.44.121:https     ESTABLISHED
tcp        0      0 farhan:39704            ord31s21-in-f3.1e:https ESTABLISHED
tcp        0      0 farhan:48107            104.16.105.204:http     ESTABLISHED
tcp        0      0 farhan:48667            del01s06-in-f13.1:https TIME_WAIT  
tcp        0      0 farhan:57194            68.232.44.121:https     ESTABLISHED
tcp        0      0 farhan.com:37086        khan.com:domain         TIME_WAIT  
tcp        0      0 farhan:46668            104.16.91.254:https     ESTABLISHED
tcp        0      0 farhan:50630            202.159.216.160:http    ESTABLISHED
tcp        0      0 farhan:36746            ec2-50-17-236-38.c:http ESTABLISHED
tcp        0      0 farhan:55446            a23-205-213-177.d:https ESTABLISHED
tcp        0      0 farhan:44874            104.16.118.182:http     ESTABLISHED
tcp        0      0 farhan:36784            ec2-50-17-236-38.c:http ESTABLISHED
tcp        0      0 farhan:36784            ec2-50-17-236-38.c:http ESTABLISHED
tcp6       1      0 ip6-localhost:56314     ip6-localhost:ipp       CLOSE_WAIT 
udp        0      0 farhan.com:47149        farhan.com:47149        ESTABLISHED
Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ]         DGRAM                    12483    /var/spool/postfix/dev/log
unix  29     [ ]         DGRAM                    11429    /dev/log
unix  3      [ ]         SEQPACKET  CONNECTED     21182    @00023
unix  2      [ ]         DGRAM                    119038   /var/run/wpa_supplicant/wlan0
unix  3      [ ]         STREAM     CONNECTED     24077    
unix  3      [ ]         STREAM     CONNECTED     11983    
unix  3      [ ]         STREAM     CONNECTED     1519     
unix  3      [ ]         STREAM     CONNECTED     20586    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     17725    
unix  3      [ ]         STREAM     CONNECTED     116666   
unix  3      [ ]         STREAM     CONNECTED     20064    
unix  3      [ ]         STREAM     CONNECTED     57114    @farhan-com.canonical.Unity.Scope.applications.T21415429563808
unix  3      [ ]         STREAM     CONNECTED     17035    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     17030    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     40540    
unix  3      [ ]         STREAM     CONNECTED     116699   
unix  3      [ ]         STREAM     CONNECTED     17407    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     17217    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15885    
unix  3      [ ]         STREAM     CONNECTED     13891    
unix  3      [ ]         STREAM     CONNECTED     22715    
unix  3      [ ]         STREAM     CONNECTED     18068    
unix  3      [ ]         STREAM     CONNECTED     17724    
unix  3      [ ]         STREAM     CONNECTED     16340    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     116685   
unix  2      [ ]         DGRAM                    99665    
unix  3      [ ]         STREAM     CONNECTED     17374    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     17019    
unix  3      [ ]         STREAM     CONNECTED     18342    
unix  2      [ ]         DGRAM                    10949    
unix  3      [ ]         STREAM     CONNECTED     116696   
unix  2      [ ]         STREAM     CONNECTED     47042    
unix  3      [ ]         STREAM     CONNECTED     40548    
unix  3      [ ]         STREAM     CONNECTED     23718    
unix  3      [ ]         STREAM     CONNECTED     18534    
unix  3      [ ]         STREAM     CONNECTED     116679   
unix  3      [ ]         STREAM     CONNECTED     16800    
unix  2      [ ]         STREAM     CONNECTED     71194    @/dbus-vfs-daemon/socket-1oaBGDwP
unix  2      [ ]         DGRAM                    19618    
unix  3      [ ]         STREAM     CONNECTED     18220    
unix  3      [ ]         STREAM     CONNECTED     116721   
unix  3      [ ]         STREAM     CONNECTED     40541    
unix  3      [ ]         STREAM     CONNECTED     18804    
unix  3      [ ]         STREAM     CONNECTED     15333    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     15947    
unix  3      [ ]         STREAM     CONNECTED     18336    
unix  3      [ ]         STREAM     CONNECTED     10952    
unix  3      [ ]         STREAM     CONNECTED     76516    
unix  3      [ ]         STREAM     CONNECTED     27990    
unix  3      [ ]         STREAM     CONNECTED     116663   
unix  3      [ ]         SEQPACKET  CONNECTED     21194    
unix  3      [ ]         STREAM     CONNECTED     56174    
unix  3      [ ]         STREAM     CONNECTED     17162    
unix  3      [ ]         STREAM     CONNECTED     36531    
unix  3      [ ]         STREAM     CONNECTED     28155    
unix  3      [ ]         STREAM     CONNECTED     19609    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     116697   
unix  3      [ ]         STREAM     CONNECTED     17332    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     16001    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23695    
unix  3      [ ]         STREAM     CONNECTED     22717    
unix  2      [ ]         DGRAM                    18879    
unix  3      [ ]         STREAM     CONNECTED     18806    
unix  3      [ ]         STREAM     CONNECTED     17933    @/com/ubuntu/upstart-session/1000/2313
unix  3      [ ]         STREAM     CONNECTED     15227    @/com/ubuntu/upstart-session/1000/2313
unix  3      [ ]         STREAM     CONNECTED     15992    
unix  2      [ ]         DGRAM                    18535    
unix  3      [ ]         STREAM     CONNECTED     116688   
unix  2      [ ]         DGRAM                    119554   
unix  3      [ ]         STREAM     CONNECTED     116661   
unix  3      [ ]         SEQPACKET  CONNECTED     21198    
unix  3      [ ]         STREAM     CONNECTED     22718    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     19646    
unix  3      [ ]         STREAM     CONNECTED     116695   
unix  3      [ ]         STREAM     CONNECTED     56175    
unix  3      [ ]         STREAM     CONNECTED     116675   
unix  3      [ ]         SEQPACKET  CONNECTED     21183    
unix  3      [ ]         STREAM     CONNECTED     19247    
unix  3      [ ]         STREAM     CONNECTED     12347    
unix  3      [ ]         STREAM     CONNECTED     1522     @/com/ubuntu/upstart
unix  3      [ ]         STREAM     CONNECTED     28184    
unix  3      [ ]         STREAM     CONNECTED     16339    
unix  3      [ ]         STREAM     CONNECTED     16877    
unix  3      [ ]         STREAM     CONNECTED     24367    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         SEQPACKET  CONNECTED     21180    
unix  3      [ ]         STREAM     CONNECTED     22716    
unix  3      [ ]         STREAM     CONNECTED     20506    
unix  3      [ ]         STREAM     CONNECTED     17223    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     16862    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     78386    
unix  3      [ ]         STREAM     CONNECTED     40539    
unix  3      [ ]         STREAM     CONNECTED     78887    
unix  2      [ ]         STREAM     CONNECTED     50201    
unix  3      [ ]         STREAM     CONNECTED     41088    
unix  3      [ ]         STREAM     CONNECTED     41199    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     23222    
unix  3      [ ]         STREAM     CONNECTED     17944    @/tmp/dbus-GNCrQc6P6n
unix  2      [ ]         STREAM     CONNECTED     118317   
unix  3      [ ]         STREAM     CONNECTED     15828    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     20509    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     19875    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     15899    @/tmp/dbus-GNCrQc6P6n
unix  2      [ ]         DGRAM                    10214    
unix  2      [ ]         DGRAM                    11018    
unix  3      [ ]         STREAM     CONNECTED     116704   
unix  3      [ ]         STREAM     CONNECTED     116682   
unix  3      [ ]         STREAM     CONNECTED     9870     /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     74301    
unix  3      [ ]         STREAM     CONNECTED     16872    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     15337    
unix  2      [ ]         DGRAM                    14002    
unix  3      [ ]         STREAM     CONNECTED     17134    /run/user/1000/keyring-ROWCKa/pkcs11
unix  3      [ ]         STREAM     CONNECTED     18235    
unix  3      [ ]         STREAM     CONNECTED     75095    
unix  3      [ ]         STREAM     CONNECTED     20526    
unix  3      [ ]         STREAM     CONNECTED     17157    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     76310    
unix  3      [ ]         STREAM     CONNECTED     20524    
unix  3      [ ]         STREAM     CONNECTED     17213    
unix  3      [ ]         STREAM     CONNECTED     16859    
unix  3      [ ]         STREAM     CONNECTED     10050    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     116683   
unix  3      [ ]         STREAM     CONNECTED     16153    
unix  3      [ ]         STREAM     CONNECTED     74293    
unix  2      [ ]         DGRAM                    64348    
unix  3      [ ]         STREAM     CONNECTED     18526    
unix  3      [ ]         STREAM     CONNECTED     23223    
unix  3      [ ]         STREAM     CONNECTED     18803    
unix  3      [ ]         STREAM     CONNECTED     15777    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15201    
unix  3      [ ]         STREAM     CONNECTED     116722   
unix  3      [ ]         STREAM     CONNECTED     28180    
unix  3      [ ]         STREAM     CONNECTED     16162    
unix  3      [ ]         STREAM     CONNECTED     18669    
unix  3      [ ]         STREAM     CONNECTED     21190    
unix  3      [ ]         STREAM     CONNECTED     14641    
unix  3      [ ]         STREAM     CONNECTED     116702   
unix  3      [ ]         STREAM     CONNECTED     116684   
unix  3      [ ]         STREAM     CONNECTED     15278    
unix  3      [ ]         STREAM     CONNECTED     17070    
unix  3      [ ]         STREAM     CONNECTED     28179    
unix  3      [ ]         STREAM     CONNECTED     18527    
unix  3      [ ]         STREAM     CONNECTED     23733    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     19257    
unix  3      [ ]         STREAM     CONNECTED     15204    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     18384    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     18667    
unix  2      [ ]         DGRAM                    10992    
unix  3      [ ]         STREAM     CONNECTED     12346    @/com/ubuntu/upstart
unix  3      [ ]         STREAM     CONNECTED     28062    
unix  3      [ ]         STREAM     CONNECTED     22722    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     16869    @/tmp/dbus-GNCrQc6P6n
unix  2      [ ]         DGRAM                    118339   
unix  3      [ ]         SEQPACKET  CONNECTED     21216    
unix  3      [ ]         STREAM     CONNECTED     18699    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     56195    
unix  3      [ ]         STREAM     CONNECTED     41425    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     16879    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     16852    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     18343    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     116706   
unix  3      [ ]         STREAM     CONNECTED     116671   
unix  3      [ ]         STREAM     CONNECTED     19605    
unix  2      [ ]         STREAM     CONNECTED     69116    @/dbus-vfs-daemon/socket-ZC83wmHK
unix  3      [ ]         STREAM     CONNECTED     24368    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     16383    @/dbus-vfs-daemon/socket-XeUjAeAF
unix  3      [ ]         STREAM     CONNECTED     18019    
unix  3      [ ]         STREAM     CONNECTED     16804    @/com/ubuntu/upstart-session/1000/2313
unix  3      [ ]         STREAM     CONNECTED     15202    
unix  3      [ ]         STREAM     CONNECTED     116716   
unix  3      [ ]         STREAM     CONNECTED     19340    
unix  3      [ ]         STREAM     CONNECTED     17267    
unix  3      [ ]         STREAM     CONNECTED     17079    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     11183    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     10961    
unix  3      [ ]         STREAM     CONNECTED     11459    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     119436   /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     100485   /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     16230    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     15956    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15424    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     13080    
unix  3      [ ]         STREAM     CONNECTED     12717    
unix  3      [ ]         STREAM     CONNECTED     116662   
unix  3      [ ]         STREAM     CONNECTED     21192    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     19922    
unix  3      [ ]         STREAM     CONNECTED     11497    
unix  3      [ ]         STREAM     CONNECTED     122243   
unix  3      [ ]         STREAM     CONNECTED     116691   
unix  3      [ ]         STREAM     CONNECTED     16163    
unix  3      [ ]         STREAM     CONNECTED     18338    
unix  3      [ ]         STREAM     CONNECTED     15741    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     16673    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     58709    
unix  3      [ ]         STREAM     CONNECTED     28132    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     56194    
unix  3      [ ]         STREAM     CONNECTED     28533    
unix  3      [ ]         STREAM     CONNECTED     17242    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     17963    
unix  3      [ ]         STREAM     CONNECTED     75573    
unix  3      [ ]         STREAM     CONNECTED     22140    
unix  3      [ ]         STREAM     CONNECTED     21532    @/tmp/dbus-GNCrQc6P6n
unix  2      [ ]         DGRAM                    12442    
unix  3      [ ]         STREAM     CONNECTED     116717   
unix  2      [ ]         STREAM     CONNECTED     105964   
unix  3      [ ]         STREAM     CONNECTED     24360    
unix  3      [ ]         STREAM     CONNECTED     58717    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     18875    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     15275    
unix  3      [ ]         STREAM     CONNECTED     80155    
unix  3      [ ]         STREAM     CONNECTED     22853    
unix  3      [ ]         STREAM     CONNECTED     18016    
unix  3      [ ]         STREAM     CONNECTED     17266    
unix  3      [ ]         STREAM     CONNECTED     18672    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     11014    
unix  3      [ ]         STREAM     CONNECTED     17141    
unix  3      [ ]         STREAM     CONNECTED     116672   
unix  3      [ ]         STREAM     CONNECTED     15262    
unix  3      [ ]         STREAM     CONNECTED     59591    
unix  3      [ ]         STREAM     CONNECTED     15822    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     22872    
unix  3      [ ]         STREAM     CONNECTED     12689    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     12348    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     28143    
unix  3      [ ]         STREAM     CONNECTED     20066    
unix  3      [ ]         STREAM     CONNECTED     9879     /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     82219    
unix  3      [ ]         STREAM     CONNECTED     76529    
unix  3      [ ]         STREAM     CONNECTED     18067    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     18064    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     74291    
unix  3      [ ]         STREAM     CONNECTED     17265    
unix  3      [ ]         STREAM     CONNECTED     82554    
unix  3      [ ]         STREAM     CONNECTED     42241    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     15310    
unix  3      [ ]         STREAM     CONNECTED     15867    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     86490    
unix  3      [ ]         STREAM     CONNECTED     16089    
unix  3      [ ]         STREAM     CONNECTED     21903    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     17077    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     76526    
unix  3      [ ]         STREAM     CONNECTED     19248    @/dbus-vfs-daemon/socket-jl99Spjd
unix  3      [ ]         STREAM     CONNECTED     16803    @/com/ubuntu/upstart-session/1000/2313
unix  2      [ ]         STREAM     CONNECTED     70409    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     28191    
unix  3      [ ]         STREAM     CONNECTED     18069    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     9876     /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     18737    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     121312   
unix  3      [ ]         STREAM     CONNECTED     17959    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     116673   
unix  3      [ ]         STREAM     CONNECTED     74302    
unix  3      [ ]         STREAM     CONNECTED     59588    
unix  3      [ ]         STREAM     CONNECTED     16882    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     13136    /var/run/acpid.socket
unix  3      [ ]         STREAM     CONNECTED     24341    
unix  3      [ ]         STREAM     CONNECTED     18347    
unix  3      [ ]         STREAM     CONNECTED     15672    
unix  3      [ ]         STREAM     CONNECTED     80156    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     17247    
unix  3      [ ]         STREAM     CONNECTED     15265    
unix  3      [ ]         STREAM     CONNECTED     15217    
unix  3      [ ]         STREAM     CONNECTED     41211    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     17249    
unix  3      [ ]         STREAM     CONNECTED     15887    
unix  3      [ ]         STREAM     CONNECTED     15674    /var/run/dbus/system_bus_socket
unix  2      [ ]         DGRAM                    16495    
unix  2      [ ]         DGRAM                    84975    
unix  3      [ ]         STREAM     CONNECTED     18726    
unix  3      [ ]         STREAM     CONNECTED     15264    @/tmp/dbus-GNCrQc6P6n
unix  2      [ ]         DGRAM                    12540    
unix  3      [ ]         STREAM     CONNECTED     116690   
unix  3      [ ]         STREAM     CONNECTED     28144    
unix  3      [ ]         STREAM     CONNECTED     23734    
unix  3      [ ]         STREAM     CONNECTED     20217    
unix  3      [ ]         STREAM     CONNECTED     19617    
unix  3      [ ]         STREAM     CONNECTED     122489   
unix  2      [ ]         STREAM     CONNECTED     50197    
unix  3      [ ]         STREAM     CONNECTED     19601    
unix  3      [ ]         STREAM     CONNECTED     12716    
unix  3      [ ]         STREAM     CONNECTED     82221    
unix  2      [ ]         STREAM     CONNECTED     69114    @/dbus-vfs-daemon/socket-Vmede8BG
unix  3      [ ]         STREAM     CONNECTED     16228    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     15263    
unix  3      [ ]         STREAM     CONNECTED     15211    
unix  3      [ ]         STREAM     CONNECTED     24342    
unix  3      [ ]         STREAM     CONNECTED     16152    
unix  3      [ ]         STREAM     CONNECTED     18700    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     18880    
unix  3      [ ]         STREAM     CONNECTED     116693   
unix  2      [ ]         DGRAM                    24085    
unix  2      [ ]         DGRAM                    117491   
unix  3      [ ]         STREAM     CONNECTED     17193    
unix  3      [ ]         STREAM     CONNECTED     15504    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     11486    
unix  3      [ ]         STREAM     CONNECTED     20518    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     16164    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     15848    
unix  3      [ ]         STREAM     CONNECTED     11323    
unix  3      [ ]         STREAM     CONNECTED     76517    
unix  3      [ ]         STREAM     CONNECTED     18882    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     16844    
unix  3      [ ]         STREAM     CONNECTED     15212    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     16858    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     11747    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     18554    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     18187    @/tmp/.ICE-unix/2437
unix  3      [ ]         STREAM     CONNECTED     16961    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     116711   
unix  2      [ ]         STREAM     CONNECTED     71191    @/dbus-vfs-daemon/socket-4uYJ5tzb
unix  3      [ ]         STREAM     CONNECTED     22143    
unix  3      [ ]         STREAM     CONNECTED     18213    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     116707   
unix  3      [ ]         STREAM     CONNECTED     28190    
unix  3      [ ]         STREAM     CONNECTED     18670    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     116718   
unix  3      [ ]         STREAM     CONNECTED     82222    
unix  3      [ ]         STREAM     CONNECTED     75571    
unix  3      [ ]         STREAM     CONNECTED     22051    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     21630    
unix  2      [ ]         DGRAM                    17230    
unix  3      [ ]         STREAM     CONNECTED     13958    
unix  3      [ ]         STREAM     CONNECTED     24348    
unix  3      [ ]         STREAM     CONNECTED     18295    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     18137    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     18802    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     59590    
unix  3      [ ]         STREAM     CONNECTED     15946    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     18329    
unix  3      [ ]         STREAM     CONNECTED     116668   
unix  3      [ ]         STREAM     CONNECTED     28189    
unix  3      [ ]         STREAM     CONNECTED     16960    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     27994    
unix  3      [ ]         STREAM     CONNECTED     15889    
unix  3      [ ]         STREAM     CONNECTED     17225    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     116694   
unix  3      [ ]         STREAM     CONNECTED     74306    
unix  3      [ ]         STREAM     CONNECTED     42060    @/tmp/.X11-unix/X0
unix  3      [ ]         SEQPACKET  CONNECTED     21179    
unix  3      [ ]         STREAM     CONNECTED     19939    
unix  3      [ ]         STREAM     CONNECTED     15223    
unix  2      [ ]         DGRAM                    14170    
unix  2      [ ]         DGRAM                    12660    
unix  3      [ ]         STREAM     CONNECTED     27980    
unix  3      [ ]         STREAM     CONNECTED     28182    
unix  3      [ ]         STREAM     CONNECTED     18344    
unix  3      [ ]         STREAM     CONNECTED     17034    
unix  3      [ ]         STREAM     CONNECTED     17020    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     15272    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     17932    
unix  2      [ ]         DGRAM                    12415    
unix  3      [ ]         STREAM     CONNECTED     116700   
unix  3      [ ]         STREAM     CONNECTED     116669   
unix  3      [ ]         STREAM     CONNECTED     19230    
unix  3      [ ]         STREAM     CONNECTED     19610    
unix  3      [ ]         STREAM     CONNECTED     15891    
unix  3      [ ]         STREAM     CONNECTED     116667   
unix  3      [ ]         STREAM     CONNECTED     74307    
unix  3      [ ]         STREAM     CONNECTED     42061    
unix  3      [ ]         STREAM     CONNECTED     19923    
unix  3      [ ]         STREAM     CONNECTED     15181    
unix  2      [ ]         DGRAM                    13951    
unix  2      [ ]         DGRAM                    118393   
unix  3      [ ]         STREAM     CONNECTED     76518    
unix  3      [ ]         STREAM     CONNECTED     27988    
unix  3      [ ]         STREAM     CONNECTED     20523    
unix  3      [ ]         STREAM     CONNECTED     18390    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     18321    
unix  3      [ ]         STREAM     CONNECTED     15872    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     9723     @/com/ubuntu/upstart
unix  3      [ ]         STREAM     CONNECTED     82556    
unix  3      [ ]         STREAM     CONNECTED     42063    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     116701   
unix  3      [ ]         STREAM     CONNECTED     116678   
unix  3      [ ]         STREAM     CONNECTED     74303    
unix  3      [ ]         STREAM     CONNECTED     18697    
unix  3      [ ]         STREAM     CONNECTED     9739     
unix  3      [ ]         STREAM     CONNECTED     20063    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     19178    
unix  3      [ ]         STREAM     CONNECTED     19606    
unix  3      [ ]         STREAM     CONNECTED     13256    
unix  3      [ ]         STREAM     CONNECTED     28183    
unix  3      [ ]         STREAM     CONNECTED     19981    @/dbus-vfs-daemon/socket-dzSv5N0J
unix  3      [ ]         STREAM     CONNECTED     17163    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     10951    
unix  3      [ ]         SEQPACKET  CONNECTED     21195    
unix  3      [ ]         STREAM     CONNECTED     17953    
unix  3      [ ]         STREAM     CONNECTED     116703   
unix  2      [ ]         STREAM     CONNECTED     119405   
unix  3      [ ]         STREAM     CONNECTED     18406    @/tmp/.ICE-unix/2437
unix  3      [ ]         STREAM     CONNECTED     16955    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     10047    /var/run/dbus/system_bus_socket
unix  3      [ ]         DGRAM                    1567     
unix  3      [ ]         STREAM     CONNECTED     20519    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     18212    
unix  3      [ ]         STREAM     CONNECTED     18158    
unix  3      [ ]         STREAM     CONNECTED     17928    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     41086    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     11503    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     116710   
unix  2      [ ]         STREAM     CONNECTED     117590   
unix  3      [ ]         STREAM     CONNECTED     21558    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     20508    
unix  3      [ ]         SEQPACKET  CONNECTED     21199    
unix  3      [ ]         STREAM     CONNECTED     15317    
unix  3      [ ]         STREAM     CONNECTED     19528    
unix  3      [ ]         STREAM     CONNECTED     116664   
unix  3      [ ]         STREAM     CONNECTED     22145    
unix  3      [ ]         STREAM     CONNECTED     16786    
unix  3      [ ]         STREAM     CONNECTED     15700    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     16474    
unix  3      [ ]         STREAM     CONNECTED     116713   
unix  3      [ ]         STREAM     CONNECTED     18324    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     73991    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     16344    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     16871    
unix  3      [ ]         STREAM     CONNECTED     16840    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     17406    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     116674   
unix  3      [ ]         STREAM     CONNECTED     56173    
unix  3      [ ]         STREAM     CONNECTED     40933    
unix  3      [ ]         STREAM     CONNECTED     27987    
unix  3      [ ]         STREAM     CONNECTED     15241    
unix  3      [ ]         STREAM     CONNECTED     42239    
unix  3      [ ]         STREAM     CONNECTED     21535    
unix  3      [ ]         STREAM     CONNECTED     15270    @/tmp/dbus-GNCrQc6P6n
unix  2      [ ]         STREAM     CONNECTED     15928    
unix  3      [ ]         STREAM     CONNECTED     75574    
unix  3      [ ]         STREAM     CONNECTED     76309    
unix  3      [ ]         STREAM     CONNECTED     19243    
unix  3      [ ]         STREAM     CONNECTED     18454    @/com/ubuntu/upstart-session/1000/2313
unix  3      [ ]         STREAM     CONNECTED     18323    
unix  3      [ ]         STREAM     CONNECTED     9835     /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     56172    
unix  3      [ ]         STREAM     CONNECTED     42335    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     18677    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     116712   
unix  3      [ ]         STREAM     CONNECTED     16915    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     22725    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     16881    
unix  3      [ ]         STREAM     CONNECTED     15219    /var/run/dbus/system_bus_socket
unix  2      [ ]         STREAM     CONNECTED     21567    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     15927    
unix  3      [ ]         STREAM     CONNECTED     11592    
unix  3      [ ]         STREAM     CONNECTED     16863    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     116698   
unix  3      [ ]         STREAM     CONNECTED     15760    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     116681   
unix  3      [ ]         STREAM     CONNECTED     80733    
unix  3      [ ]         STREAM     CONNECTED     58035    
unix  3      [ ]         STREAM     CONNECTED     18337    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     17142    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     15838    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     121794   
unix  3      [ ]         STREAM     CONNECTED     116687   
unix  2      [ ]         STREAM     CONNECTED     21568    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     18498    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     16845    
unix  3      [ ]         STREAM     CONNECTED     82220    
unix  3      [ ]         STREAM     CONNECTED     10064    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     15953    
unix  3      [ ]         SEQPACKET  CONNECTED     21215    
unix  3      [ ]         STREAM     CONNECTED     20507    @/dbus-vfs-daemon/socket-obIhRtoR
unix  3      [ ]         STREAM     CONNECTED     17066    
unix  3      [ ]         STREAM     CONNECTED     16471    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     10958    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     82557    
unix  3      [ ]         STREAM     CONNECTED     59586    
unix  3      [ ]         STREAM     CONNECTED     116719   
unix  3      [ ]         STREAM     CONNECTED     116677   
unix  3      [ ]         SEQPACKET  CONNECTED     22147    
unix  3      [ ]         STREAM     CONNECTED     19177    
unix  3      [ ]         STREAM     CONNECTED     18805    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     15218    
unix  3      [ ]         STREAM     CONNECTED     18339    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     27991    
unix  3      [ ]         STREAM     CONNECTED     27802    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15929    
unix  3      [ ]         STREAM     CONNECTED     121792   
unix  3      [ ]         STREAM     CONNECTED     28181    
unix  3      [ ]         STREAM     CONNECTED     21559    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15759    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     19611    
unix  3      [ ]         STREAM     CONNECTED     15881    
unix  3      [ ]         STREAM     CONNECTED     116689   
unix  3      [ ]         STREAM     CONNECTED     80734    
unix  3      [ ]         STREAM     CONNECTED     75094    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     21624    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     74309    
unix  3      [ ]         STREAM     CONNECTED     24355    
unix  3      [ ]         STREAM     CONNECTED     15260    
unix  3      [ ]         STREAM     CONNECTED     121795   
unix  3      [ ]         STREAM     CONNECTED     122242   
unix  3      [ ]         STREAM     CONNECTED     16234    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     121793   
unix  3      [ ]         STREAM     CONNECTED     76527    
unix  3      [ ]         STREAM     CONNECTED     21631    
unix  3      [ ]         STREAM     CONNECTED     18893    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     17981    
unix  3      [ ]         STREAM     CONNECTED     116715   
unix  3      [ ]         STREAM     CONNECTED     21839    @/dbus-vfs-daemon/socket-7WjTKTuj
unix  3      [ ]         STREAM     CONNECTED     19274    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     10957    
unix  3      [ ]         STREAM     CONNECTED     24339    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     12434    
unix  2      [ ]         STREAM     CONNECTED     98567    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     74294    
unix  3      [ ]         STREAM     CONNECTED     20218    
unix  3      [ ]         STREAM     CONNECTED     17159    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     17237    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     116680   
unix  3      [ ]         STREAM     CONNECTED     57115    @farhan-com.canonical.Unity.Scope.scopes.T21415449617251
unix  3      [ ]         STREAM     CONNECTED     57101    /run/user/1000/keyring-ROWCKa/pkcs11
unix  3      [ ]         STREAM     CONNECTED     15332    
unix  3      [ ]         STREAM     CONNECTED     15259    
unix  3      [ ]         STREAM     CONNECTED     16233    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     18322    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     11017    
unix  3      [ ]         STREAM     CONNECTED     24359    
unix  3      [ ]         STREAM     CONNECTED     18387    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     17078    /var/run/dbus/system_bus_socket
unix  3      [ ]         DGRAM                    1566     
unix  3      [ ]         STREAM     CONNECTED     74308    
unix  3      [ ]         STREAM     CONNECTED     57105    @farhan-com.canonical.Unity.Master.Scope.applications.T21405242347373
unix  3      [ ]         STREAM     CONNECTED     19978    
unix  3      [ ]         STREAM     CONNECTED     18890    
unix  3      [ ]         STREAM     CONNECTED     18676    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     40786    
unix  3      [ ]         STREAM     CONNECTED     12541    
unix  3      [ ]         STREAM     CONNECTED     15331    
unix  3      [ ]         STREAM     CONNECTED     75572    
unix  3      [ ]         STREAM     CONNECTED     23162    @/tmp/dbus-sSkOMWhc
unix  2      [ ]         STREAM     CONNECTED     19250    @/dbus-vfs-daemon/socket-aGF5Qw7J
unix  3      [ ]         STREAM     CONNECTED     17216    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     74292    
unix  2      [ ]         DGRAM                    11011    
unix  3      [ ]         STREAM     CONNECTED     78385    
unix  3      [ ]         STREAM     CONNECTED     15311    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     122240   
unix  3      [ ]         STREAM     CONNECTED     16964    
unix  3      [ ]         STREAM     CONNECTED     21627    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     116714   
unix  3      [ ]         STREAM     CONNECTED     23719    @/dbus-vfs-daemon/socket-B0aR89ac
unix  3      [ ]         STREAM     CONNECTED     19575    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     18506    
unix  3      [ ]         STREAM     CONNECTED     116709   
unix  3      [ ]         STREAM     CONNECTED     76519    
unix  3      [ ]         STREAM     CONNECTED     21902    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     20723    
unix  3      [ ]         STREAM     CONNECTED     22851    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     17199    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     17031    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     116720   
unix  3      [ ]         STREAM     CONNECTED     74304    
unix  3      [ ]         STREAM     CONNECTED     18521    
unix  3      [ ]         STREAM     CONNECTED     122241   
unix  2      [ ]         STREAM     CONNECTED     106939   
unix  3      [ ]         STREAM     CONNECTED     18853    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     119435   
unix  3      [ ]         STREAM     CONNECTED     18675    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     18018    
unix  2      [ ]         STREAM     CONNECTED     104358   
unix  3      [ ]         STREAM     CONNECTED     11597    
unix  3      [ ]         STREAM     CONNECTED     86491    
unix  3      [ ]         STREAM     CONNECTED     72179    
unix  3      [ ]         STREAM     CONNECTED     28192    
unix  3      [ ]         STREAM     CONNECTED     27993    
unix  3      [ ]         STREAM     CONNECTED     13081    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     76528    
unix  2      [ ]         STREAM     CONNECTED     70129    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         SEQPACKET  CONNECTED     22148    
unix  3      [ ]         STREAM     CONNECTED     16496    
unix  2      [ ]         STREAM     CONNECTED     84973    
unix  3      [ ]         STREAM     CONNECTED     18729    @/tmp/.X11-unix/X0
unix  2      [ ]         STREAM     CONNECTED     47102    
unix  3      [ ]         STREAM     CONNECTED     16154    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     17146    
unix  3      [ ]         STREAM     CONNECTED     29789    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     19557    
unix  2      [ ]         DGRAM                    12708    
unix  3      [ ]         STREAM     CONNECTED     122488   
unix  3      [ ]         STREAM     CONNECTED     116676   
unix  3      [ ]         STREAM     CONNECTED     28063    
unix  3      [ ]         STREAM     CONNECTED     116708   
unix  2      [ ]         STREAM     CONNECTED     48520    
unix  3      [ ]         STREAM     CONNECTED     27978    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     15871    
unix  3      [ ]         STREAM     CONNECTED     18065    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     15749    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     121311   
unix  3      [ ]         STREAM     CONNECTED     17248    
unix  3      [ ]         STREAM     CONNECTED     15113    
unix  3      [ ]         STREAM     CONNECTED     19940    
unix  3      [ ]         STREAM     CONNECTED     82555    
unix  3      [ ]         STREAM     CONNECTED     17961    
unix  2      [ ]         DGRAM                    9965     
unix  3      [ ]         STREAM     CONNECTED     116705   
unix  3      [ ]         STREAM     CONNECTED     18874    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     15779    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     78886    
unix  2      [ ]         STREAM     CONNECTED     49453    
unix  3      [ ]         STREAM     CONNECTED     18876    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15776    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     27808    
unix  3      [ ]         STREAM     CONNECTED     15748    @/tmp/dbus-36b1dmw3CX
unix  3      [ ]         STREAM     CONNECTED     20512    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     17246    
unix  3      [ ]         STREAM     CONNECTED     17954    
unix  3      [ ]         STREAM     CONNECTED     21191    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     17212    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     16952    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     16919    
unix  3      [ ]         STREAM     CONNECTED     22142    
unix  3      [ ]         STREAM     CONNECTED     27979    
unix  3      [ ]         STREAM     CONNECTED     16868    
unix  3      [ ]         STREAM     CONNECTED     9770     
unix  3      [ ]         STREAM     CONNECTED     116692   
unix  3      [ ]         STREAM     CONNECTED     20481    @/dbus-vfs-daemon/socket-WeJEb9Zk
unix  3      [ ]         STREAM     CONNECTED     16151    
unix  3      [ ]         STREAM     CONNECTED     15895    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     15843    
unix  3      [ ]         STREAM     CONNECTED     42065    @/tmp/dbus-sSkOMWhc
unix  3      [ ]         STREAM     CONNECTED     42062    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     17245    
unix  3      [ ]         STREAM     CONNECTED     18889    
unix  3      [ ]         STREAM     CONNECTED     15216    
unix  3      [ ]         STREAM     CONNECTED     40549    
unix  3      [ ]         STREAM     CONNECTED     16878    
unix  3      [ ]         STREAM     CONNECTED     57098    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     101488   
unix  3      [ ]         STREAM     CONNECTED     17143    
unix  2      [ ]         DGRAM                    16025    
unix  3      [ ]         STREAM     CONNECTED     18461    
unix  3      [ ]         STREAM     CONNECTED     116686   
unix  3      [ ]         STREAM     CONNECTED     40921    
unix  3      [ ]         STREAM     CONNECTED     18888    
unix  3      [ ]         STREAM     CONNECTED     17232    
unix  3      [ ]         STREAM     CONNECTED     15882    
unix  3      [ ]         STREAM     CONNECTED     17980    
unix  3      [ ]         STREAM     CONNECTED     13171    
unix  3      [ ]         STREAM     CONNECTED     9769     
unix  3      [ ]         STREAM     CONNECTED     27986    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     18881    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15876    
unix  3      [ ]         STREAM     CONNECTED     16870    
unix  3      [ ]         STREAM     CONNECTED     9880     /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     17135    
unix  3      [ ]         STREAM     CONNECTED     17238    @/tmp/dbus-GNCrQc6P6n
unix  3      [ ]         STREAM     CONNECTED     15266    @/tmp/dbus-GNCrQc6P6n
farhan@farhan:~/Desktop/AWS/Bespoke DTH packages from Tata Sky (DTH) ‘Make My Pa
ck’ service_files$ netstat | grep 45694
tcp        0      0 farhan:46242            ec2-54-80-241-137:45694 ESTABLISHED
tcp        0      0 farhan:46239            ec2-54-80-241-137:45694 ESTABLISHED
farhan@farhan:~/Desktop/AWS/Bespoke DTH packages from Tata Sky (DTH) ‘Make My Pa
ck’ service_files$ sudo su
[sudo] passwo
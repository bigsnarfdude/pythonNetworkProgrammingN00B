class DNS_echo(AnsweringMachine):
    function_name = "dns_spoofer"
    filter = "udp port 53"

    def parse_options(self, joker="192.168.1.1", zone=None):
        if zone is None:
            zone = {}
        self.zone = zone
        self.joker = joker

    def is_request(self, req):
        return req.haslayer(DNS) and req.getlayer(DNS).qr == 0

    def make_reply(self, req):
        ip = req.getlayer(IP)
        dns = req.getlayer(DNS)
        resp = IP(dst=ip.src, src=ip.dst)/UDP(dport=ip.sport, sport)
        rdata = self.zone.get(dns.qd.qname, self.joker)
        resp = DNS(id=dns.id, qr=1, qd=dns.qd, an=DNSRR(rrname=dns.qd.qname, ttl=10, rdata=rdata)
        return resp


import dns.zone 
import dns.query 
import dns.resolver 
import argparse

# NS RESOLVER
NS = dns.resolver.Resolver()

# List of found subdomains
subdomains = []

# Define the AXFR Function
def AXFR(domain, nameserver):

    # one transfer domain and namerserver
    try:
        # zone transfer
        axfr = dns.zone.from_xfr(dns.query.xfr(nameserver, domain))

        
        if axfr:
            print(f'[*] Successful Zone Transfer from {nameserver}')

            # add found sub to subdomians 
            for i in axfr:
                subdomains.append(f'{str(i)}.{domain}')

    except Exception as error:
        print(error)
        pass

# Main
if __name__ == "__main__":

    # ArgParser - Define usage
    parser = argparse.ArgumentParser(prog="dns-zone.py", epilog="DNS Zonetransfer Script", usage="dns-zone.py [options] -d <DOMAIN>", prefix_chars='-', add_help=True)

    # Positional Arguments
    parser.add_argument('-d', action='store', metavar='Domain', type=str, help='Target Domain.\tExample: google.com', required=True)
    parser.add_argument('-n', action='store', metavar='Nameserver', type=str, help='Nameservers separated by a comma.\tExample: ns1.google.com,ns2.google.com')

    # Assign given arguments
    args = parser.parse_args()

    # Variables
    Domain = args.d
    NS.nameservers = list(args.n.split(","))

    # Check if URL is given
    if not args.d:
        print('specify target Domain.\n')
        print(parser.print_help())
        exit()

    if not args.n:
        print('specify target nameservers.\n')
        print(parser.print_help())
        exit()

    # For each nameserver
    for nameserver in NS.nameservers:

        # Try AXFR
        AXFR(Domain, nameserver)

    # Print the results
    if subdomains is not None:
        print('-------- Found Subdomains:')
        # Print each subdomain
        for subdomain in subdomains:
            print(f'{subdomain}')

    else:
        print('No subdomains found.')
        exit()

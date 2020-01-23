import hgm.host_guest_match as hgm
import pdb

def main():
	matched_hosts, unpaired_guests = hgm.match()
	hgm.write_matches(matched_hosts)
	hgm.write_unpaired(unpaired_guests)
	print("Matching complete")

if __name__ == '__main__':
	main()
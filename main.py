import hgm.host_guest_match as hgm
import pdb

def main():
	host_csv = "csv_files/3-6-hosts.csv"
	guest_csv = "csv_files/3-6-guests.csv"
	matched_hosts, unpaired_guests = hgm.match(host_csv, guest_csv)
	hgm.write_matches(matched_hosts, "csv_files/match.csv")
	hgm.write_unpaired(unpaired_guests, "csv_files/unpaired_guests.csv")
	print("Matching complete")

if __name__ == '__main__':
	main()

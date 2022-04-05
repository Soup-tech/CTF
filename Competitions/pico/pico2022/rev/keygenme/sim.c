#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>
/*
 * Compile:
 * 	gcc sim.c -o sim -lcrypto
*/

int main() {

	// Parts of flag
	char * first_part = "picoCTF{";
	char * second_part = "br1ng_y0";
	char * third_part = "ur_0wn_k";
	char * fourth_part = "3y_";
	char * close_curly = "}";

	// Comput MD5 hashes
	char first_part_hash[16];
	size_t length = strlen(first_part);
	MD5(first_part, length, first_part_hash);

	char second_part_hash[16];
	length = strlen(second_part);
	MD5(second_part, length, second_part_hash);

	int hex_bytes_counter = 0;
	char first_part_hex[14];
	for (int q = 0; q < 16; q++) {
		sprintf(first_part_hex + hex_bytes_counter, "%02x", first_part_hash[q]);
		hex_bytes_counter = hex_bytes_counter + 2;
	}

	printf("%s\n",first_part_hex);

	return 0;
}

/* WARNING: Could not reconcile some variable overlaps */

undefined8 keygen_function(char *user_input)

{
  size_t length_of_flag_parts;
  undefined8 returned_value;
  long in_FS_OFFSET;
  int local_d0;
  int q;
  int w;
  int e;
  int i;
  undefined2 close_curly;
  byte local_b8 [16];
  byte local_a8 [16];
  undefined8 first_part;
  undefined8 second_part;
  undefined8 third_part;
  undefined4 fourth_part;
  char local_78 [14];
  undefined local_6a;
  undefined local_62;
  undefined local_60;
  undefined local_5b;
  char local_58 [21];
  undefined local_43;
  char acStack56 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  first_part = 0x7b4654436f636970;    // picoCTF{
  second_part = 0x30795f676e317262;   // br1ng_y0
  third_part = 0x6b5f6e77305f7275;    // ur_0wn_k
  fourth_part = 0x5f7933;             // 3y_
  close_curly = 0x7d;                 // }


  length_of_flag_parts = strlen((char *)&first_part);               // 8
  MD5((uchar *)&first_part,length_of_flag_parts,local_b8);

  length_of_flag_parts = strlen((char *)&close_curly);              // 1
  MD5((uchar *)&close_curly,length_of_flag_parts,local_a8);

  local_d0 = 0;
  for (q = 0; q < 16; q = q + 1) {
    sprintf(local_78 + local_d0,"%02x",(uint)local_b8[q]);
    local_d0 = local_d0 + 2;
  }
  local_d0 = 0;
  for (w = 0; w < 16; w = w + 1) {
    sprintf(local_58 + local_d0,"%02x",(uint)local_a8[w]);
    local_d0 = local_d0 + 2;
  }
  for (e = 0; e < 27; e = e + 1) {
    acStack56[e] = *(char *)((long)&first_part + (long)e);
  }
  acStack56[27] = local_43;
  acStack56[28] = local_62;
  acStack56[29] = local_62;
  acStack56[30] = local_78[0];
  acStack56[31] = local_5b;
  acStack56[32] = local_43;
  acStack56[33] = local_6a;
  acStack56[34] = local_60;
  acStack56[35] = (undefined)close_curly;
  length_of_flag_parts = strlen(user_input);
  if (length_of_flag_parts == 36) {
    for (i = 0; i < 36; i = i + 1) {
      if (user_input[i] != acStack56[i]) {
        returned_value = 0;
        goto LAB_00101475;
      }
    }
    returned_value = 1;
  }
  else {
    returned_value = 0;
  }
LAB_00101475:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return returned_value;
}


<?php

function xor_encrypt($in) {
    $plain_text = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $encrypted_text = $in;
    $key = '';

    // Iterate through each character
    for($i=0; $i < strlen($encrypted_text); $i++) {
    	$key .= $plain_text[$i] ^ $encrypted_text[$i % strlen($encrypted_text)];
    }

    return $key;
}

$encoded_data = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
$encoded_data = base64_decode($encoded_data);
$encoded_data = xor_encrypt($encoded_data);
echo $encoded_data;
?>

#File was built so I could pipe output into it for a specific result

<?php

$plaintext = stream_get_contents(fopen("php://stdin", "r"));;
$key = "eb1a3227cdc3fedbaec2fe38bf6c044a";
$cipher = "aes-256-ctr";
$iv = "TESTINGTESTING";


$ciphertext = openssl_encrypt($plaintext, $cipher, $key, $options=0, $iv);
echo $ciphertext;

?>

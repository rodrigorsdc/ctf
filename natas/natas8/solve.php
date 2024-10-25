<?php
$encoded = '3d3d516343746d4d6d6c315669563362';
echo base64_decode(strrev(hex2bin($encoded)));
echo "\n";
echo hex2bin($encoded);
echo "\n";
echo strrev(hex2bin($encoded));
	
?>
